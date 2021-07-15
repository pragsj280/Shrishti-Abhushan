from django.urls import path
from .import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("about/", views.about, name = 'about'),
    path("contact/", views.contact, name = 'contact'),
   
    path("shop-details/<int:pk>", views.shop_details, name = 'shop-details'),
    path("subcategory/<int:cpk>/<int:pk>", views.sub_category, name = 'sub_category'),
    path("shop/", views.shop, name = 'shop'),
    path("cart/", views.cart1, name = 'cart'),
    path("pluscart/", views.plus_cart),
    path("removecart/", views.remove_cart),   
    path("minuscart/", views.minus_cart),   
    path("checkout/", views.checkout, name = 'checkout'),
    path("add_to_cart/", views.add_to_cart),
    path("search/", views.search,name='search'),
    path("update_address/", views.update_address,name='update_address'),
    path("orderplaced/", views.orderplaced,name='orderplaced'),
    path("policy/", views.policy,name='policy'),
]