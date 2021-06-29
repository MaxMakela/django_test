from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from typing import Optional, List
from .forms import PostForm, PostEditForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from functools import reduce
import operator


class Home(ListView):
    """Render posts list page with object_list context."""
    model: Optional[Post] = Post
    template_name: str = 'home.html'
    ordering: List[str] = ['-date']

    def get_queryset(self):
        """Filter list by search key."""
        search_word: str = self.request.GET.get('search')
        if search_word:
            # Our search key can consist of several words,
            # so we generate a complex search query for each word separately.
            qs = reduce(operator.or_, (Q(title__icontains=word) for word in search_word.split()))
            return Post.objects.filter(qs).order_by('-date')
        else:
            return Post.objects.all().order_by('-date')


class PostDetails(DetailView):
    """Render post details page with object_list context."""
    model: Optional[Post] = Post
    template_name: str = 'post.html'


class PostAdding(LoginRequiredMixin, CreateView):
    """Render post creation page. Ser a login requirement for this action."""
    model: Optional[Post] = Post
    form_class: Optional[PostForm] = PostForm
    template_name: str = 'new_post.html'

    def form_valid(self, form):
        """Override form_valid method to set current authenticated user as post author."""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdating(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Render post updating page."""
    model: Optional[Post] = Post
    form_class: Optional[PostEditForm] = PostEditForm
    template_name: str = 'update_post.html'

    def test_func(self):
        """Check current user is a post author."""
        return self.request.user == self.get_object().author


class PostDeleting(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Render post deleting confirm page."""
    model: Optional[Post] = Post
    template_name: str = 'delete_post.html'
    # Redirect to home page.
    success_url = reverse_lazy('home')

    def test_func(self):
        """Check current user is a post author."""
        return self.request.user == self.get_object().author

