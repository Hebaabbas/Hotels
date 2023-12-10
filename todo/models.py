from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models

# Custom manager for CustomUser model
class CustomUserManager(BaseUserManager):
    # Function to create a standard user
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    # Function to create a superuser
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, email, password, **extra_fields)

# Custom user model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    class Meta:
        db_table = 'customuser'  

    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD + '__iexact': username})

    def __str__(self):
        return self.username

# Model for hotels
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    average_rating = models.FloatField()

    class Meta:
        db_table = 'hotels'

    def __str__(self):
        return self.name

# Model for posts
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)


    class Meta:
        db_table = 'posts'

    # Methods to count thumbs up and down
    def number_of_thumbs_up(self):
        return self.reactions.filter(is_thumb_up=True).count()

    def number_of_thumbs_down(self):
        return self.reactions.filter(is_thumb_up=False).count()

    def __str__(self):
        return self.title

# Model for reactions (likes/dislikes)
class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_thumb_up = models.BooleanField(default=True)

    class Meta:
        db_table = 'reactions'

# Model for comments on posts
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"

# Model for reviews on hotels
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="reviews")
    review_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    room_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    spa = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)

    class Meta:
        db_table = 'reviews'

    def __str__(self):
        return f"Review by {self.user.username} for {self.hotel.name}"