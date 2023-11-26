from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Review, Hotel
from todo.models import CustomUser


        
class PostForm(forms.ModelForm):
    hotel = forms.ModelChoiceField(queryset=Hotel.objects.all(), required=True, label="Hotel")
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'hotel'] 

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'firstname', 'lastname', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please use a different email.")
        return email

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        if commit:
            user.save()
        return user

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'room_type', 'duration', 'spa', 'breakfast']

hotel_id = forms.IntegerField(widget=forms.HiddenInput())
