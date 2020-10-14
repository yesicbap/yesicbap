from django.urls import path
from contact import views

urlpatterns = [
    path('contact_home/', views.contact_home, name='contact_home'),
    path('contact_thanks/', views.contact_thanks, name='contact_thanks'),
]


