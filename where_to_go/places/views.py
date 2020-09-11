from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Place


def index(request):
    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

    places = Place.objects.all()

    for place in places:
        point = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.point_title,
                    "placeId": place.place_id,
                    "detailsUrl": "./places/roofs24.json"
                }
            }
        geo_json['features'].append(point)

    return render(request, 'where_to_go/index.html', context={'places': geo_json})


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)

    return HttpResponse(place.title)
