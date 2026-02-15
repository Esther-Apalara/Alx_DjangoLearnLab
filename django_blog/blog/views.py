from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.shortcuts import redirect

# -------------------
# List all posts
# -------------------
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # blog/templates/blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-created_at']  # newest first

# -------------------
# View single post
# -------------------
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# -------------------
# Create new post
# -------------------
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# -------------------
# Update post
# -------------------
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Only author can update
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# -------------------
# Delete post
# -------------------
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/posts/'

    # Only author can delete
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


@login_required
def profile(request):
    if request.method == "POST":
        user = request.user
        user.email = request.POST.get("email")
        user.save()
        return redirect("profile")

    return render(request, "blog/profile.html")        