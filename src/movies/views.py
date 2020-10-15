from django.http import HttpResponse
from django.shortcuts import render

from movies.models import Movie


def hello_world(request):
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello world")
    else:
        return HttpResponse("Hello " + name)

def home(request):
    latest_movies = Movie.objects.all().order_by("-release_date")
    context={'movies': latest_movies[:5]}
    return render(request, "home.html", context)

def movie_detail(request, pk):
    possible_movies = Movie.objects.filter(pk=pk).select_related("category")
    if len(possible_movies) == 0:
        # pelicula no existe
        return render(request, "404.html", status=404)
    else:
        movie = possible_movies[0]
        context = {'movie': movie}
        return render(request, "movie_detail.html", context)