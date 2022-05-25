from django.test import TestCase
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
import pandas as pd
from community.models import Tour
from community.tag_crawling import get_tour_tag

# Create your tests here.

all = Tour.objects.all()
print(all[0].__str__())
tourname = all[0].__str__()
tag = get_tour_tag(tourname)
print(tag)
# for tourname in all:
#     print(index)