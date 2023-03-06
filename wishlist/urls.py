from django.urls import path
from . import views

urlpatterns = [
    path('', views.wishlist, name='wishlist'),
    path('get-wishlists/', get_wishlists, name='get-wishlists'),
]
