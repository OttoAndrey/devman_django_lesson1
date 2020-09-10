from django.shortcuts import render

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
