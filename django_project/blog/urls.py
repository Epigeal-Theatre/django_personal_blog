from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    UserPostListView
)
from .import views

# URL patterns for the blog application.
# These patterns map specific URL paths to their corresponding views.

urlpatterns = [
    # Home page that displays a list of all posts using the PostListView class-based view.
    path('', PostListView.as_view(), name='blog-home'),
    
    # Displays posts from a specific user. The <str:username> captures the username from the URL
    # and passes it to UserPostListView, which will handle the filtering.
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    
    # Detailed view of a specific post. The <int:pk> captures the primary key (ID) of the post.
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    
    # Create a new post. This view renders the form for creating posts.
    # No primary key is needed since this is for new posts.
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    
    # Update an existing post. The <int:pk> captures the primary key of the post to be updated.
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    
    # Delete an existing post. The <int:pk> captures the primary key of the post to be deleted.
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    
    # A simple 'About' page handled by a function-based view 'about' in the views module.
    path('about/', views.about, name='blog-about')
]
