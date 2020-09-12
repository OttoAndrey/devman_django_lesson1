from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Place, Image


def index(request):
    places = Place.objects.all()

    geo_json = {
        "type": "FeatureCollection",
        "features": []
    }

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
                "detailsUrl": f"places/{place.pk}/"
            }
        }
        geo_json['features'].append(point)

    return render(request, 'where_to_go/index.html', context={'places': geo_json})


def place_detail_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    imgs = Image.objects.filter(place=place_id)

    data = {
        "title": place.title,
        "imgs": [img.image.url for img in imgs
                 ],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }

    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 4})
