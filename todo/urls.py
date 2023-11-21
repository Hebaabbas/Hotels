from . import views
from django.urls import path
from .views import sign_in_view, sign_up_view


urlpatterns = [
    path('', views.get_index, name='home'),  # Home page
    path('posts/', views.PostList.as_view(), name='post_list'),  # List of posts
    path('reviews/', views.ReviewList.as_view(), name='review_list'),  # List of reviews
    path('contact/', views.contact_view, name='contact'),
    path('signin/', sign_in_view, name='signIn'),
    path('signup/', sign_up_view, name='signUp'),

]

