from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('table/<uuid:post_id>/', ochish, name='post'),
    path('add/', Add, name='add'),
]
