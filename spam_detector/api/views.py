from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Contact, SpamNumber
from .serializers import UserSerializer, RegisterSerializer, ContactSerializer, SpamNumberSerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ContactListView(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SpamNumberView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        spam_number, created = SpamNumber.objects.get_or_create(phone_number=phone_number)
        spam_number.reports += 1
        spam_number.save()
        
        return Response({'message': 'Number marked as spam'}, status=status.HTTP_200_OK)

class SearchView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        query = request.query_params.get('query')
        search_by = request.query_params.get('search_by')
        if not query or not search_by:
            return Response({'error': 'Query and search_by are required'}, status=status.HTTP_400_BAD_REQUEST)

        if search_by == 'name':
            contacts = Contact.objects.filter(Q(name__startswith(query)) | Q(name__icontains(query))).order_by('name')
        elif search_by == 'phone_number':
            contacts = Contact.objects.filter(phone_number=query)
        else:
            return Response({'error': 'Invalid search_by value'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
