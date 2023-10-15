from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add-todo", views.addTodo, name="add-todo"),
    path("delete/<str:id>", views.deleteTodo, name="delete"),
    path("edit/<str:id>", views.editTodo, name="edit"),
    path("complete/<str:id>", views.todoMarkCompleted, name="complete"),
]