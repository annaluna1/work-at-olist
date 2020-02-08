from rest_framework import viewsets, generics, pagination, mixins, filters
from django_filters import rest_framework as filters

from .models import Authors, Books
from .serializers import BooksSerializer, AuthorsSerializer


# Create your views here.

class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="authors_name")

    class Meta:
        model = Authors
        fields = ['name']


class Authors(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    pagination_class = pagination.LimitOffsetPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AuthorFilter


class Books(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    pagination_class = pagination.LimitOffsetPagination



