from django.contrib import admin

from .models import Place, Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    fields = ('image', 'title', 'headshot_image', 'number',)
    readonly_fields = ('headshot_image',)


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'title', 'headshot_image', 'number',)
    readonly_fields = ('headshot_image',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
