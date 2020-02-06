from core.models import Author
from django.core.management.base import BaseCommand,CommandError
import csv


class Command(BaseCommand):
    help = 'Import the authors CSV files'

    def add_arguments(self, parser):
        parser.add_argument('authors', type=str, help='Indicate the CSV file to be imported')


