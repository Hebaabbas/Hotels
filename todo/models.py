from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    average_rating = models.FloatField()

    class Meta:
        db_table = 'hotels'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(unique=True, null=True)

    def number_of_thumbs_up(self):
        return self.reactions.filter(is_thumb_up=True).count()

    def number_of_thumbs_down(self):
        return self.reactions.filter(is_thumb_up=False).count()


    def __str__(self):
        return self.title

class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_thumb_up = models.BooleanField(default=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="reviews")
    review_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    room_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    spa = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)

    def __str__(self):
        return f"Review by {self.user.username} for {self.hotel.name}"

