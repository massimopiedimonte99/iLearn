from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('<int:pk>', views.DetailView.as_view(), name="detail"),
    path('book/add', views.AddBook.as_view(), name="add-book"),
    path('book/edit/<int:pk>', views.EditBook.as_view(), name="edit-book"),
    path('book/delete/<int:pk>', views.DeleteBook.as_view(), name="delete-book"),
    path('author/add', views.AddAuthor.as_view(), name="add-author"),
]
