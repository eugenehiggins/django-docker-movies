from rest_framework.viewsets import ModelViewSet

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    http_method_names = ["get", "post"]
