from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Function-based view for the home page, displays all posts.
def home(request):
    context = {
        'posts': Post.objects.all()  # Fetch all posts and pass them to the template
    }
    return render(request, 'blog/home.html', context)

# Class-based view for listing posts, with pagination.
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # Template for displaying the post list
    context_object_name = 'posts'  # Name used to reference posts in the template
    ordering = ['-date_posted']  # Order posts by most recent first
    paginate_by = 5  # Number of posts per page

# Class-based view to list posts by a specific user, with pagination.
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    # Override to filter posts by the selected user.
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# Class-based view to display post details.
class PostDetailView(DetailView):
    model = Post

# Class-based view to create a new post (login required).
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  # Fields displayed in the form

    # Set the current user as the author before saving the form.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Class-based view to update a post (login required, and user must be the author).
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Set the current user as the author before updating the form.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Test whether the current user is the author of the post.
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Class-based view to delete a post (login required, and user must be the author).
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'  # Redirect to home after successful deletion

    # Test whether the current user is the author of the post.
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Function-based view for the About page.
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
