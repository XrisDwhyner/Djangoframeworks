from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, status
from .models import Moviedata
from .serializers import MovieSerializer


# Create your views here.
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     # ... Additional logic
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(category="Action")
    serializer_class = MovieSerializer
