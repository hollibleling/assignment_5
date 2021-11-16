import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "humanscape.settings")
django.setup()

from app.develope.models import *

CSV_PATH_PRODUCTS = "develope.csv"

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        kind = Kind.objects.get(id = row[6])
        phase = Phase.objects.get(id = row[7])
        scope = Scope.objects.get(id = row[8])

        if row[4] == '':
            row[4] = 0

        develope_list = DevelopeList.objects.create(
            number = row[0],
            name = row[1],
            subject = row[2],
            agency = row[3],
            target_count = row[4],
            period = row[5],
            kind = kind,
            phase = phase,
            scope = scope
        )
