from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.home, name="home"),
	path('blog/', views.blog, name="blog"),
	path('projects/', views.projects, name="projects"),
]