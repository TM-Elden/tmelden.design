from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name="home_page"),
    path('blog/', views.blog),
    path('projects/', views.projects),
    path('contact/', views.contact),
    path('bio/', views.bio)
]
