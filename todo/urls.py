from . import views
from django.urls import path


urlpatterns = [
    path('', views.get_index, name='home'),  # Home page
    path('posts/', views.PostList.as_view(), name='post_list'),  # List of posts
    path('reviews/', views.ReviewList.as_view(), name='review_list'),  # List of reviews
    path('contact/', views.contact_view, name='contact'),
    path('signIn/', views.sign_in_view, name='signIn'),  # Sign in page
]
