from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Spam Detector API. Navigate to /api/ for API endpoints.")