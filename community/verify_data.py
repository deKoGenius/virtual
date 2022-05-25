import pandas as pd
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from community.models import Tour


data = pd.read_csv('./data/tour.csv')
data.dropna(axis=0, inplace=True)


for idx in data.index:
    tour_name = data.loc[idx,'1']
    if '(' in tour_name:
        index = tour_name.find('(')
        tour_name = tour_name[:index]
    if ',' in tour_name:
        index = tour_name.find(',')
        tour_name = tour_name[:index]
    if '/' in tour_name:
        index = tour_name.find('/')
        tour_name = tour_name[:index]
    if '&' in tour_name:
        index = tour_name.find('&')
        tour_name = tour_name[:index]
    if '-' in tour_name:
        index = tour_name.find('-')
        tour_name = tour_name[:index]
    data.loc[idx,'1'] = tour_name

for idx in data.index:
    latitude = data.loc[idx,'2']
    longitude = data.loc[idx,'3']
    if (latitude <= 30) | (latitude >=40):
        data.drop(idx, inplace=True)
    if (longitude <= 125) | (longitude >= 135):
        data.drop(idx, inplace=True)

for idx in data.index:
    Tour.objects.create(name = data.loc[idx,'1'], tourTime = 2, tourLatitude = data.loc[idx,'2'], tourLongitude = data.loc[idx,'3'], tour_url = data.loc[idx,'4'], visitCnt=0)

print(Tour.objects.all())