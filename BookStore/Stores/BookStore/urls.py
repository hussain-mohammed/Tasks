from django.urls import path, include
from . import views


urlpatterns = [
    path('list/', views.ListBooks.as_view()),
    path('Create/',views.CreateBooks.as_view()),
    path('list/<str:pk>/',views.detailBook.as_view()),
    path('update/<str:pk>/',views.UpdateBook.as_view()),
    path('api-auth/',include('rest_framework.urls')),
]