from . import views
from django.urls import path

from .views import HolidayListView

urlpatterns = [

    path('', views.index, name="index"),
    path('api/holidays/', HolidayListView.as_view(), name='holiday-list'),
]