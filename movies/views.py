from django.shortcuts import render
from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.generics import ListAPIView

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer