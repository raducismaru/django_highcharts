from django.urls import path
from .views import *

urlpatterns = [
    path('games/', games, name='games'),
    path('favorites/', game_sales, name='favorites'),
]
