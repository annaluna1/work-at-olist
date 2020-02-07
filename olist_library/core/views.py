from rest_framework import viewsets, generics, pagination, mixins

from .models import Authors, Books
from .serializers import BooksSerializer, AuthorsSerializer


# Create your views here.
class Authors(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    pagination_class = pagination.LimitOffsetPagination
