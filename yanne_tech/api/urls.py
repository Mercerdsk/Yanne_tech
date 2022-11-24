from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('api/v1/bookledger/', views.BookRegisterAPIView.as_view()),
    path('api/v1/searchbyid/<int:book_id>/',views.booksearchbyidAPIView.as_view()),
    path('api/v1/searchbygenre/<str:genre>/',views.booksearchbygenreAPIView.as_view()),
]