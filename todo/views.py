from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Post, Hotel, Review, Comment, Reaction 
from django.db.models import Count, Q
from django.contrib import messages
from todo import views
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from todo.models import CustomUser
from .forms import ReviewForm
from django.http import Http404  


def get_index(request):
    return render(request, 'todo/index.html')


def contact_view(request):
    return render(request, 'todo/contact.html')


     
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
    context_object_name = 'post_list'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotels'] = Hotel.objects.all()
        context['comments'] = Comment.objects.all()
        context['reactions'] = Reaction.objects.all()
        return context

    def get_queryset(self):
        return Post.objects.annotate(
            num_thumbs_up=Count('reactions', filter=Q(reactions__is_thumb_up=True)),
            num_thumbs_down=Count('reactions', filter=Q(reactions__is_thumb_up=False))
        ).order_by('-post_date')

class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.all().order_by("-review_date")
    template_name = "todo/posts.html"  
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotels'] = Hotel.objects.all()
        return context

@login_required
def add_post(request):
    if request.method == 'POST':
        # Retrieve form data
        title = request.POST.get('title')
        content = request.POST.get('content')
        hotel_id = request.POST.get('hotel')
        image = request.FILES.get('image')

        # Validation (you can add more complex validation as needed)
        if not title or not content or not hotel_id:
            messages.error(request, "Please fill in all required fields.")
            return redirect('post_list')

        # Create a new Post instance
        post = Post(
            title=title,
            content=content,
            user=request.user,
            hotel_id=hotel_id,  # Assuming hotel_id is the primary key of a hotel
            image=image  # Handle image file upload
        )

        # Save the new post
        post.save()
        messages.success(request, 'Your post has been successfully added!')
        return redirect('post_list')

    # Context for GET request
    context = {
        'hotels': Hotel.objects.all()
    }
    return render(request, 'todo/posts.html', context)

@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        comment_content = request.POST.get('comment')
        if comment_content:
            Comment.objects.create(user=request.user, post=post, content=comment_content)
            messages.success(request, 'Comment added successfully!')
        else:
            messages.error(request, 'Comment cannot be empty.')
    return redirect('post_list')


def add_review_view(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        form.fields['hotel'].queryset = Hotel.objects.all()  # Include all hotels in the queryset
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.hotel = hotel
            review.save()
            # Redirect to the hotel detail page or another appropriate view
            return redirect('hotel_detail', hotel_id=hotel_id)
    else:
        # Handle the case where 'hotel_id' is not provided in the URL or form data
        raise Http404("Hotel not found")


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user:  # Check if the logged-in user is the post creator
        post.delete()
        messages.success(request, 'Post deleted successfully!')
    else:
        messages.error(request, 'You do not have permission to delete this post.')
    return redirect('post_list')

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if review.user == request.user:
        review.delete()
        messages.success(request, 'Review deleted successfully!')
        return redirect('review_list')  # Redirect to the review list page
    else:
        messages.error(request, 'You do not have permission to delete this review.')
        return redirect('review_list')  # Redirect to the review list page

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.user == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted successfully!')
    else:
        messages.error(request, 'You do not have permission to delete this comment.')
    return redirect('post_list')  # Redirects to the post list without any arguments
