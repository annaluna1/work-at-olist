from django.contrib import admin
from django.urls import path, include
from .views import Authors, Books

urlpatterns = [
    path('', Authors.as_view(), name='Authors'),
    path('books/<pk>', Books.as_view(), name='Books'),
]
