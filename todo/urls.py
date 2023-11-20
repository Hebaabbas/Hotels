from . import views
from django.urls import path
from .views import PostList 
from .views import sign_in_view



urlpatterns = [
    path('', views.get_index, name='home'),  # Home page
    path('posts/', views.PostList.as_view(), name='post_list'),  # List of posts
    path('reviews/', views.ReviewList.as_view(), name='review_list'),  # List of reviews
    path('contact/', views.contact_view, name='contact'),
    path('posts/', PostList.as_view(), name='post_list'),
    path('sign-in/', sign_in_view, name='signIn'), 
]