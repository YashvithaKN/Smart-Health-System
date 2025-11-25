from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView

app_name = 'accounts'
urlpatterns = [
path('register/', views.register, name='register'),
path('profile/', views.profile, name='profile'),
path('login/', CustomLoginView.as_view(), name='login'),
path('logout/', auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
path('delete_profile/', views.delete_profile, name='delete_profile'),

]