# myApp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('post/', views.post, name="post"),
    path('update/<int:post_id>', views.update, name="update"),
    path('delete/<int:post_id>', views.delete, name="delete"),
    path('c_post/<int:post_id>', views.c_post, name="c_post"),
]