import requests
from rest_framework import generics

from eventActorsApp.models import City
from eventActorsApp.serializers import CitySerializer


class FillCitiesView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get(self, request, *args, **kwargs):
        url = 'https://api-colombia.com/api/v1/City'
        response = requests.get(url)
        data = response.json()
        for city in data:
            City.objects.create(name=city['name'])
            print(f'City {city["name"]} created')
        return self.list(request, *args, **kwargs)
