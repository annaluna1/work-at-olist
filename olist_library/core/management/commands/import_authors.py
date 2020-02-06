from core.models import Authors
from django.core.management.base import BaseCommand, CommandError
from pymongo import MongoClient
import csv


class Command(BaseCommand):
    help = 'Import the authors CSV files'

    def add_arguments(self, parser):
        parser.add_argument('authors', type=str, help='Indicate the CSV file to be imported')

    def handle(self, *args, **options):
        try:
            file = open(options['authors'])
            open_file = csv.reader(file)
            client = Authors.get_client(self)
            authors = []
            for line in open_file:
                result = client.find_one({'authors_name': line})
                if result:
                    next
                else:
                    authors.append(line)
            client.insert_many([{'authors_name': name} for name in authors])
            client.delete_one({'authors_name': 'name'})
        except:
            self.stdout.write('The file are not updated on database, check the format file ou if the file are created')
        else:
            self.stdout.write('The file was imported')


