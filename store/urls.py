from django.urls import path
from store.views import store_view,checkout_view,cart_view

urlpatterns = [
    path("store/",store_view, name='store'),
    path("checkout/",checkout_view, name='checkout'),
    path("cart/",cart_view, name='cart'),
]
