from django.views import generic

from .models import AboutCard, Album, HeroText


class HomePageView(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        data["hero_texts"] = HeroText.objects.all()
        data["about_cards"] = AboutCard.objects.all()
        data["albums"] = Album.objects.filter(is_published=True).prefetch_related("photos")

        return data


class DevPageView(generic.TemplateView):
    template_name = "dev.html"
