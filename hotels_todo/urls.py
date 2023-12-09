from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from todo.views import get_index, sign_up_view
from todo import views as todo_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.get_index, name="home"),  # Home page URL
    path('todo/', include('todo.urls')),  # Include all URLs from the todo app
    path('summernote/', include('django_summernote.urls')),  # Summernote URL
    path('accounts/', include('allauth.urls')),  # Allauth URL patterns



    # Authentication URLs
    path('signin/', auth_views.LoginView.as_view(template_name='todo/signIn.html'), name='sign_in'),
    path('signup/', sign_up_view, name='sign_up'),
    path('signout/', auth_views.LogoutView.as_view(next_page='home'), name='sign_out'),
]
