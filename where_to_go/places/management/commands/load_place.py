import requests
from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('place_json', nargs='+', type=str)

    def handle(self, *args, **options):
        self.stdout.write('Command execution')
        r = requests.get(options['place_json'][0])

        if r.status_code == 200:
            data = r.json()
            place, place_created = Place.objects.get_or_create(
                point_title=data['title'],
                title=data['title'],
                description_short=data['description_short'],
                description_long=data['description_long'],
                lng=data['coordinates']['lng'],
                lat=data['coordinates']['lat'],
            )

            if place_created:
                for img in data['imgs']:
                    img_response = requests.get(img)

                    if img_response.status_code == 200:
                        name = img.split('/')[-1]
                        image = Image.objects.create(
                            title=place.title,
                            place=place,
                        )
                        image.image.save(name, ContentFile(img_response.content), save=True)

                self.stdout.write(self.style.SUCCESS(f'Successfully create place "{place}"'))

            else:
                self.stdout.write(self.style.WARNING('The object has already been created'))

        else:
            self.stdout.write(self.style.ERROR('Request failed'))
