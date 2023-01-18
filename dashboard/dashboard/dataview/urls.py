from django.urls import path, re_path
from .views import readouts, index, readouts_time

# Routers provide an easy way of automatically determining the URL conf.

urlpatterns = [
    path('', index, name='index'),
    path('readouts', readouts, name='readouts'),
    re_path(r'^t=(\d{2}):(\d{2}):(\d{2})$', readouts_time),
]