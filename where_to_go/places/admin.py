from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin

from .models import Place, Image


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    fields = ('image', 'title', 'headshot_image', )
    readonly_fields = ('headshot_image',)


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    fields = ('image', 'title', 'headshot_image',)
    readonly_fields = ('headshot_image',)
    extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = (
        ImageInline,
    )
    search_fields = ('title',)
