from django.shortcuts import render

# Create your views here.
def home(request):
     context = {}
     return render(request, 'portfolio/home.html', context)

def blog(request):
     context = {}
     return render(request, 'portfolio/blog.html', context)

def projects(request):
      context = {}
      return render(request, 'portfolio/projects.html', context)
