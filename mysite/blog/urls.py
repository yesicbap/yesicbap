from django.urls import path
from blog import views

urlpatterns = [
    path('blog_home/', views.BlogListView.as_view(), name='blog_home'),
    path('blog_home/<int:pk>', views.BlogDetailView.as_view(), name='blog_home_item'),
]

