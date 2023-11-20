from django.shortcuts import render
from django.views import generic
from .models import Post, Hotel
from .models import Review
from django.db.models import Count, Q
def get_index(request):
    return render(request, 'todo/index.html')

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-post_date")
    template_name = "posts.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotels'] = Hotel.objects.all()
        return context

        def get_queryset(self):
            return Post.objects.annotate(
            num_thumbs_up=Count('reactions', filter=Q(reactions__is_thumb_up=True)),
            num_thumbs_down=Count('reactions', filter=Q(reactions__is_thumb_up=False))
        ).order_by('-post_date')

class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.all().order_by("-review_date")
    template_name = "posts.html"  
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hotels'] = Hotel.objects.all()
        return context