from django.contrib import admin
from django.utils.html import format_html

from rent_house.models import AboutCard, Album, HeroText, Photo, WithUsCard


@admin.register(HeroText)
class HeroTextAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "image_preview", "is_active")
    list_editable = ("is_active",)
    list_filter = ("is_active",)
    search_fields = ("title", "text")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="100" />', obj.image.url)
        return "Нет фотографии"

    image_preview.short_description = "Предпросмотр фотографии"


@admin.register(AboutCard)
class AboutCardAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "image_preview",
    )
    search_fields = ("title", "description")
    fields = (
        "title",
        "description",
        "image",
        "image_preview",
    )
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "Нет изображения"

    image_preview.short_description = "Превью изображения"


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 10
    fields = ("image", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "Нет изображения"

    image_preview.short_description = "Превью изображения"


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fields = ("title", "is_active")
    list_display = ("title", "is_active")
    list_editable = ("is_active",)
    inlines = [PhotoInline]


@admin.register(WithUsCard)
class WithUsCardAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "image_preview", "link")
    search_fields = ("title", "description")
    fields = ("title", "description", "image", "image_preview", "link")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "Нет изображения"

    image_preview.short_description = "Превью изображения"
