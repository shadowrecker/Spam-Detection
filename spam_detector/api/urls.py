from django.urls import path
from .views import RegisterView, UserDetailView, ContactListView, SpamNumberView, SearchView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('spam/', SpamNumberView.as_view(), name='spam'),
    path('search/', SearchView.as_view(), name='search'),
]
