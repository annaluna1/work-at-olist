from djongo import models
from pymongo import MongoClient
from config import mongo_port, mongo_host

MONGO_HOST = f'mongodb://{mongo_host}:{mongo_port}/test'


class Authors(models.Model):
    '''
    This authors represent all imported authors by csv
    '''
    authors_name = models.CharField(max_length=50, blank=False)

    def get_client(self):
        self.db = MongoClient(host=MONGO_HOST)
        client = self.db.library_books.core_filter

        return client


class Books(models.Model):
    '''
    This books represent all books created
    '''
    book_name = models.CharField(max_length=70, blank=False)
    book_edition = models.CharField(max_length=5, blank=False)
    book_year = models.CharField(max_length=4, blank=False)
    book_author = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name='book_author', blank=False)

    def get_client(self):
        self.db = MongoClient(host=MONGO_HOST)
        client = self.db.library_books.core_filter

        return client

    def get_book(self, str_book):
        client = self.get_client()
        result = client.find_one({'id': str_book})

        return result['book_name']