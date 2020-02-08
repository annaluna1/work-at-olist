from rest_framework import viewsets, generics, pagination, mixins
from django_filters import rest_framework as filters

from .models import Authors, Books
from .serializers import BooksSerializer, AuthorsSerializer


# Create your views here.

class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="authors_name")

    class Meta:
        model = Authors
        fields = ['name']


class Authors(generics.ListAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AuthorFilter


class BookFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name")
    edition = filters.NumberFilter(field_name="edition")
    publication_year = filters.NumberFilter(field_name="publication_year")
    author = filters.CharFilter(field_name='author')

    class Meta:
        model = Books
        fields = ['name', 'edition', 'publication_year', 'author']


class Books(generics.ListCreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter
