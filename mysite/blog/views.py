from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PostForm

def home(request):
    return HttpResponse("Добро пожаловать на мой сайт!")

def about(request):
    return HttpResponse("About page")

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
