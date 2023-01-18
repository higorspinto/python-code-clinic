from csv import DictReader
from datetime import datetime
from pytz import UTC

from django.core.management.base import BaseCommand, CommandError

from dataview.models import Readout

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

class Command(BaseCommand):
    help = 'Loads all readouts from a csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs='+', type=str)

    def handle(self, *args, **options):
        print("Loading readouts.")
        for row in DictReader(open(options['file_path'][0])):
            data = Readout()
            data.pulsometer = row['Pulsometer_readout']
            data.efficiency = float(row['Engine_efficiency'])
            data.red_value = row['red_Value']
            data.blue_value = row['blue_Value']
            data.green_value = row['green_Value']

            raw_timestamp = row['time_stamp']
            timestamp = UTC.localize(
                datetime.strptime(raw_timestamp, DATETIME_FORMAT))
            data.time = timestamp
            data.save()
        print("Dashboard data finished loading")