# pages/urls.py
from django.urls import path

from filehandle.views import home_page_view
from filehandle.views import home1

urlpatterns = [
    path("", home_page_view, name="home"),
    path("home1", home1, name="home"),
]