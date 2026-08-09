from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from store import views


urlpatterns = [

    # =====================================
    # ADMIN
    # =====================================

    path(
        "admin/",
        admin.site.urls,
    ),


    # =====================================
    # HOME
    # =====================================

    path(
        "",
        views.home,
        name="home",
    ),


    # =====================================
    # SEARCH
    # =====================================

    path(
        "search/",
        views.search,
        name="search",
    ),


    # =====================================
    # PRODUCT DETAIL
    # =====================================

    path(
        "product/<int:pk>/",
        views.product_detail,
        name="product_detail",
    ),


    # =====================================
    # CART
    # =====================================

    path(
        "add-to-cart/<int:pk>/",
        views.add_to_cart,
        name="add_to_cart",
    ),

    path(
        "cart/",
        views.cart,
        name="cart",
    ),

    path(
        "increase-quantity/<int:pk>/",
        views.increase_quantity,
        name="increase_quantity",
    ),

    path(
        "decrease-quantity/<int:pk>/",
        views.decrease_quantity,
        name="decrease_quantity",
    ),

    path(
        "remove-cart/<int:pk>/",
        views.remove_from_cart,
        name="remove_from_cart",
    ),


    # =====================================
    # CHECKOUT
    # =====================================

    path(
        "checkout/",
        views.checkout,
        name="checkout",
    ),

    path(
        "place-order/",
        views.place_order,
        name="place_order",
    ),


    # =====================================
    # SUCCESS
    # =====================================

    path(
        "success/",
        views.success,
        name="success",
    ),


    # =====================================
    # ORDER TRACKING
    # =====================================

    path(
        "track-order/",
        views.track_order,
        name="track_order",
    ),


    # =====================================
    # WISHLIST
    # =====================================

    path(
        "wishlist/",
        views.wishlist,
        name="wishlist",
    ),

    path(
        "add-to-wishlist/<int:pk>/",
        views.add_to_wishlist,
        name="add_to_wishlist",
    ),

    path(
        "remove-wishlist/<int:pk>/",
        views.remove_wishlist,
        name="remove_wishlist",
    ),
]


# =====================================
# MEDIA FILES
# =====================================

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )