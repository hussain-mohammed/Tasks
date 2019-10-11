from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ListBooks.as_view()),
    path('<str:bookname>/',views.BookDetail.as_view()),
    path('api-auth/',include('rest_framework.urls')),
]