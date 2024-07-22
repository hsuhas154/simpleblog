# simpleblog\posts\urls.py:

from . import views
from django.urls import path 

urlpatterns = [
    path('homepage/', views.homepage, name = 'posts-home'),
    path('', views.PostListCreateView.as_view(), name = 'list-posts'),
    path('<int:pk>/', views.PostRetrieveUpdateDeleteView.as_view(), name = 'post-detail'),
]