from djongo import models
from pymongo import MongoClient
from config import mongo_port, mongo_host

MONGO_HOST = f'mongodb://{mongo_host}:{mongo_port}/test'


class Authors(models.Model):
    '''
    This authors represent all imported authors by csv
    '''
    authors_name = models.CharField(max_length=100, blank=False, unique=True)


class Books(models.Model):
    '''
    This books represent all books created
    '''
    name = models.CharField(max_length=100, blank=False)
    edition = models.PositiveIntegerField(blank=False)
    publication_year = models.PositiveIntegerField(blank=False)
    author = models.ManyToManyField(Authors, related_name='books', blank=False)




