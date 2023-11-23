from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import generic
from .models import Post, Hotel, Review, Comment, Reaction 
from django.db.models import Count, Q
from django.contrib import messages
from todo import views
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import PostForm

def your_view_function(request):
    hotels = Hotel.objects.all()  
    context = {
        'hotels': hotels,
    }
    return render(request, 'posts.html', context)


def get_index(request):
    return render(request, 'todo/index.html')


def contact_view(request):
    return render(request, 'todo/contact.html')


def posts_view(request):
    hotels = Hotel.objects.all() 
    posts = Post.objects.all() 
    context = {
        'hotels': hotels,
        'posts': posts,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,    
    }
    return render(request, 'todo/posts.html', context)

def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('post_list')  
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'todo/signIn.html')


def sign_up_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'todo/signIn.html', {'form': form})



class PostList(generic.ListView):
    model = Post
    template_name = "todo/posts.html"  
    queryset = Post.objects.all().order_by("-post_date")
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['reactions'] = Reaction.objects.all()
        context['reviews'] = Review.objects.all()
        return context

    def get_queryset(self):
        return Post.objects.annotate(
            num_thumbs_up=Count('reactions', filter=Q(reactions__is_thumb_up=True)),
            num_thumbs_down=Count('reactions', filter=Q(reactions__is_thumb_up=False))
        ).order_by('-post_date')

class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.all().order_by("-review_date")
    template_name = "todo/reviews.html"  
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotels'] = Hotel.objects.all()
        return context

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            selected_hotel_id = request.POST.get('hotel') 
            post.hotel = Hotel.objects.get(id=selected_hotel_id)  
            post.save()
            messages.success(request, 'Your post has been successfully added!')
            return redirect('post_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PostForm()

    return render(request, 'todo/posts.html', {'form': form})


@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        comment_content = request.POST.get('comment')
        Comment.objects.create(user=request.user, post=post, content=comment_content)
        return redirect('post_list')

