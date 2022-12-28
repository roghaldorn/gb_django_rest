from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author


class AuthorModelSerializer(HyperlinkedModelSerializer): # сериализатор будет выдавать json на основании модели
    class Meta:
        model = Author  # этой модели)
        fields = '__all__'  # какие модели будут в json
