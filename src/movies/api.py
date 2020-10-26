from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie
from movies.serializers import MovieSerializer, MoviesListSerializer


# enpoint creacion y listado de peliculas
class MoviesListAPI(ListCreateAPIView):

    queryset = Movie.objects.all()

    def get_serializer_class(self):
        return MoviesListSerializer if self.request.method == "GET" else MovieSerializer

class MovieDetailAPI(RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer