from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from .models import Books
from .serializer import BooksSerailizer
from rest_framework import permissions
# Create your views here.


class CreateBooks(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerailizer
    permission_classes = (permissions.IsAdminUser,)


class UpdateBook(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerailizer
    permission_classes = (permissions.IsAdminUser,)


class ListBooks(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerailizer


class detailBook(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerailizer
    permission_classes = (permissions.IsAuthenticated,)
