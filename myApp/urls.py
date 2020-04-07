# myApp/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('post/', views.post, name="post"),
    path('detail/<int:post_id>/', views.detail, name="detail"),
    path('update/<int:post_id>', views.update, name="update"),
    path('delete/<int:post_id>', views.delete, name="delete"),
    path('c_post/<int:post_id>', views.c_post, name="c_post"),
    path('c_post/<int:post_id>/<int:comment_id>', views.c_delete, name="c_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)