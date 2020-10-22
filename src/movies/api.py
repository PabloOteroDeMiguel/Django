from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie
from movies.serializers import MovieSerializer

# enpoint creacion y listado de peliculas
class MoviesListAPI(ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
