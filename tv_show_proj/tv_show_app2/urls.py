from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("shows",views.shows),
    path("shows/new",views.new),
    path("shows/create",views.create),
    path("shows/<int:id>",views.read),
    path("shows/<int:id>/edit",views.edit),
    path("shows/<int:id>/update",views.update),
    path("shows/<int:id>/destroy",views.delete)
]