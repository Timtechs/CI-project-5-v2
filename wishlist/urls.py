from django.urls import path
from . import views

urlpatterns = [
    path('', views.WishListView, name='wishlist'),
    path('get-wishlists/', views.get_wishlists, name='get-wishlists'),
]
