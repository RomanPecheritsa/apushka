from django.urls import path

from rent_house.views import DevPageView, HomePageView

app_name = "rent_house"


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("dev/", DevPageView.as_view(), name="home"),
]
