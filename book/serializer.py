from rest_framework import serializers
from book.models import BookInfo

class BookSer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'
