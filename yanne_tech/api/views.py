from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from . import models
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class BookRegisterAPIView(APIView):
    serializer_class = serializers.bookSerializer
    def get(self, request):
        try:
            articles = models.bookModels.objects.all()
            serializer = serializers.bookSerializer(articles,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status":"failure","description":str(e)},status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=serializers.bookSerializer )
    def post(self, request):
        try:
            serializer = serializers.bookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status":"failure","description":str(e)},status=status.HTTP_400_BAD_REQUEST)


class booksearchbyidAPIView(APIView):
    serializer_class = serializers.bookSerializer

    def get(self, request, book_id):
        try:
            article = models.bookModels.objects.get(book_id=book_id)
            serializer = serializers.bookSerializer(article)
            return Response(serializer.data)
        except Exception as e:
            return Response({"status": "failure", "description": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, book_id):
        try:
            article = models.bookModels.objects.get(book_id=book_id)
            serializer = serializers.bookSerializer(article,
                                                       request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "failure", "description": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, book_id):
        try:
            article = models.bookModels.objects.get(book_id=book_id)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "failure", "description": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class booksearchbygenreAPIView(APIView):
    serializer_class = serializers.bookSerializer

    def get(self, request, genre):
        try:
            article = models.bookModels.objects.get(genre=genre)
            serializer = serializers.bookSerializer(article)
            return Response(serializer.data)
        except Exception as e:
            return Response({"status": "failure", "description": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, genre):
        try:
            article = models.bookModels.objects.get(genre=genre)
            serializer = serializers.bookSerializer(article,
                                                       request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "failure", "description": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, genre):
        try:
            article = models.bookModels.objects.get(genre=genre)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "failure", "description": str(e)}, status=status.HTTP_400_BAD_REQUEST)

