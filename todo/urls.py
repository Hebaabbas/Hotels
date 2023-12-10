from . import views
from django.urls import path
from .views import sign_in_view, sign_up_view, delete_post, delete_review, delete_comment, add_review, PostReaction


urlpatterns = [
    path('', views.get_index, name='home'),  # Home page
    path('posts/', views.PostList.as_view(), name='post_list'),  # List of posts
    path('contact/', views.contact_view, name='contact'),
    path('signin/', sign_in_view, name='signIn'),
    path('signup/', sign_up_view, name='signUp'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_review/', add_review, name='add_review'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('post/<int:post_id>/react/<str:reaction_type>/', PostReaction.as_view(), name='post_reaction'),
]