from django.shortcuts import render, redirect
from post.models import Post
from django.contrib.auth.decorators import login_required


def home(request):
    posts = Post.objects.all()
    return render(request, 'pages/content.html', {'posts': posts})

@login_required 
def myblog(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(author=request.user)
        return render(request, 'pages/my_blog.html', {'username': request.user.username, 'posts': posts})
    else:

        return redirect('login')  
    


