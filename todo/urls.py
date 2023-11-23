from . import views
from django.urls import path
from .views import sign_in_view, sign_up_view, posts_view


urlpatterns = [
    path('', views.get_index, name='home'),  # Home page
    path('posts/', views.PostList.as_view(), name='post_list'),  # List of posts
    path('reviews/', views.ReviewList.as_view(), name='review_list'),  # List of reviews
    path('contact/', views.contact_view, name='contact'),
    path('signin/', sign_in_view, name='signIn'),
    path('signup/', sign_up_view, name='signUp'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('todo/posts/', posts_view, name='post_list'),


]

