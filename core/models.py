from djongo import models
from pymongo import MongoClient
from config import mongo_host

MONGO_HOST = mongo_host


class Authors(models.Model):
    '''
    This authors represent all imported authors by csv
    '''
    authors_name = models.CharField(max_length=100, blank=False, unique=True)

    def get_client(self):
        self.db = MongoClient(host=MONGO_HOST)
        client = self.db.librarybooks.core_authors

        return client

    def __str__(self):
        return self.authors_name


class Books(models.Model):
    '''
    This books represent all books created
    '''
    name = models.CharField(max_length=100, blank=False)
    edition = models.PositiveIntegerField(blank=False)
    publication_year = models.PositiveIntegerField(blank=False)
    author = models.ManyToManyField(Authors, related_name='books', blank=False)

    def get_client(self):
        db = MongoClient(host=MONGO_HOST)
        client = db.librarybooks.core_books

        return client

    def __str__(self):
        return self.name
