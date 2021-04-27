from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create_message', views.create_message,name='create_message'),
    path('login', views.login, name='login'),
    path('login_form', views.login_form, name='login'),
    path('register', views.register, name='register'),
    path('register_form', views.register_form, name='register_form'),
    path('logout', views.logout, name='logout'),
    path('wall', views.wall, name='wall'),
    path('create_comment/<int:id>', views.create_comment, name='create_comment'),
    path('delete_message/<int:id>', views.delete_message, name='delete_message')
  
]
