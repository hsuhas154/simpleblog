from . import views
from django.urls import path 

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name = 'sign-up'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]