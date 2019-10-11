from django.shortcuts import render
from rest_framework import generics,status
from django.http import HttpResponse
from .models import Books
from .serializer import BooksSerailizer
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class ListBooks(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get(self,request):
        data = Books.objects.all()
        serializer = BooksSerailizer(data,many=True)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = BooksSerailizer(data=data)
        if serializer.is_valid():
            Books.objects.create(**data)
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)


class BookDetail(APIView):
    permission_classes = (permissions.IsAdminUser,)
    def get(self,request,bookname):
        try:
            data = Books.objects.get(pk=bookname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BooksSerailizer(data)
        return Response(serializer.data)

    def put(self,request,bookname):
        try:
            BookInstance = Books.objects.get(pk=bookname)
        except:

            return Response({'msg': "Record Not Found for Update."},status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serializer = BooksSerailizer(BookInstance,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=202)
        return Response(serializer.errors,status=406)

    def delete(self,request,bookname):
        try:
            BookInstance = Books.objects.get(pk=bookname)
        except:
            return Response({'msg': "Record Not Found for Update."}, status=status.HTTP_404_NOT_FOUND)
        if request.method == "DELETE":
            if BookInstance.delete():
                return Response("Deleted Successfully")
            return Response("Delete Failed")


