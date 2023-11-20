from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),  # Home page showing posts
    path("posts/", views.PostList.as_view(), name="post_list"),  # List of posts
    path("reviews/", views.ReviewList.as_view(), name="review_list"),  # List of reviews
]
