from django.shortcuts import render
from rest_framework import viewsets
from book.serializer import BookSer
from book.models import BookInfo

# Create your views here.

class BookViewSet (viewsets.ModelViewSet):
    serializer_class = BookSer
    queryset = BookInfo.objects.all()
