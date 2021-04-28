from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("my_list",views.mylist),
    path("register",views.register),
    path("login",views.login),
    path("books",views.books),
    path("logout",views.logout),
    path("add_book",views.add_book),
    path("add_to_fav/<int:id>",views.add_to_fav),
    path("books/<int:id>",views.get_book),
    path("update_book/<int:id>",views.update_book),
    path("delete/<int:id>",views.delete_book),
    path("unfav/<int:id>",views.unfav_book),
]