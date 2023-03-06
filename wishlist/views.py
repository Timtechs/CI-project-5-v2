from django.shortcuts import render
from django.http import JsonResponse
from . import models
from django.views.generic.list import ListView
from wishlist.models import Wishlist
from django.contrib.auth.mixins import LoginRequiredMixin
from products.models import Product


def get_wishlists(request, *args, **kwargs):
    qs = Wishlist.objects.all()
    wishlist = [x.serialize() for x in qs]
    data = {
        "response": wishlist
    }
    return JsonResponse(data)


def add_to_wishlist(request, slug):
    product = get_object_or_404(Product, slug=slug)
    desired_product, created = Wishlist.objects.get_or_create(desired_product=product, slug=product.slug, user=request.user,)
    return redirect(get_wishlists)


class WishListView(ListView):
    model = Wishlist
    template_name = 'templates/wishlist.html'
    paginate_by = 10
    context_object_name = 'wishlist'

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 10
    template_name = 'products/products.html'
    context_object_name = 'mygroups'

    def get_queryset(self, **kwargs):
        user = get_object_or_404(User, username=self.request.user.username)
        return user.products.all()
