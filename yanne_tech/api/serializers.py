from rest_framework import serializers
from .models import *


class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookModels
        fields = ('book_id', 'title', 'author', 'ratings', 'genre', 'price')
