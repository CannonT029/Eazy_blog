from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView
from pages.views import home
from .forms import CommentForm
from .models import Post, Category
from .forms import PostEdit


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', category_slug=post.category.slug,slug=slug)
        
    else:
        form = CommentForm()
    return render(request, 'post/post_detail.html', {'post': post, 'form':form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'pages/category.html', {'category':category})

def search(request):
    query = request.GET.get('query')
    print(f'Received query:{query}')# check the console or log 
    if query:
        posts = Post.objects.filter(Q(title__icontains=query)) | Post.objects.filter(Q(body__icontains=query))
    else:
        posts = None

    return render(request, 'post/search.html', {'posts':posts, 'query':query})


@login_required  # Ensure that the user is logged in to access this view 
def add_post(request, category_slug, slug):
    category = get_object_or_404(Category, slug=slug)
    
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            # Save the post with the currently logged-in user as the author
            post = form.save(commit=False)
            post.author = request.user
            post.category = category
            post.save()     

            messages.success(request, 'Post added successfully.')

            return redirect('post_detail', category_slug=post.category.slug, slug=post.slug)
    else:
        form = AddPost()

    return render(request, 'post/post_form.html', {'form': form, 'category': category})



def edit_post(request, slug):
     post = get_object_or_404(Post, slug=slug)
     
     if request.method == 'POST':
        form = PostEdit(request.POST, request.FILES, instance=post)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, '{}  edited.'.format(comment.post))

            return redirect('post_detail', category_slug=post.category.slug, slug=post.slug)
     else:
          form = PostEdit(instance=post)

     return render(request, 'post/edit_blog_post.html', {'post': post, 'form':form})


def delete(request, slug):
     post = get_object_or_404(Post, slug=slug)
     
     if request.method == 'POST':
        post.delete()
        return redirect('my_blog')

     return render(request, 'post/delete_post.html', {'post': post})



class AddPost(LoginRequiredMixin,CreateView):
    model = Post
    template = 'post_form.html'
    fields = ['title', 'image', 'category', 'body']
    exclude = ['author']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)