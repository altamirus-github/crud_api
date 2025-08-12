from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.allow import GlobalAllowAny
from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    # Use custom permission here
    permission_classes = (IsAuthenticated, GlobalAllowAny,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalAllowAny,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
