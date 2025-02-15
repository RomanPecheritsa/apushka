from django.urls import path

from rent_house.views import HomePageView

app_name = "rent_house"


urlpatterns = [path("", HomePageView.as_view(), name="home")]
