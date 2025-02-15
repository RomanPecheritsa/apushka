from django.views import generic

from .models import AboutCard, Album, HeroText, Photo, WithUsCard


class HomePageView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data["hero_texts"] = HeroText.objects.all()
        data["about_cards"] = AboutCard.objects.all().order_by("?")
        data["withas_cards"] = WithUsCard.objects.all()
        album = Album.objects.filter(is_active=True).first()

        if album:
            data["photos"] = album.photos.all().order_by("?")[:18]
        else:
            data["photos"] = Photo.objects.none()

        return data
