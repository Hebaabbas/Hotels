from django.contrib import admin
from django.contrib.auth.models import User
from .models import Hotel, Post, Comment, Reaction, Review
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'post_date', 'user', 'hotel')
    search_fields = ['title', 'content']
    list_filter = ('post_date', 'user')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'city', 'average_rating')
    search_fields = ['name', 'country', 'city']
    list_filter = ('country', 'city')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'post', 'comment_date')
    list_filter = ('comment_date', 'user')
    search_fields = ('user__username', 'content')

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'is_thumb_up')
    list_filter = ('is_thumb_up', 'user')
    search_fields = ('user__username', 'post__title')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'user', 'review_date', 'content', 'room_type', 'duration', 'spa', 'breakfast')
    list_filter = ('hotel', 'user', 'review_date', 'spa', 'breakfast')
    search_fields = ('user__username', 'hotel__name', 'content')
