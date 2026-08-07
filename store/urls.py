from django.urls import path
from . import views

urlpatterns = [

    # =========================
    # HOME
    # =========================
    path(
        "",
        views.home,
        name="home",
    ),

    # =========================
    # SEARCH
    # =========================
    path(
        "search/",
        views.search,
        name="search",
    ),

    # =========================
    # PRODUCT DETAIL
    # =========================
    path(
        "product/<int:pk>/",
        views.product_detail,
        name="product_detail",
    ),

    # =========================
    # CART
    # =========================
    path(
        "cart/",
        views.cart,
        name="cart",
    ),

    path(
        "add-to-cart/<int:pk>/",
        views.add_to_cart,
        name="add_to_cart",
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
        views.remove_cart,
        name="remove_cart",
    ),
    # =========================
    # WISHLIST
    # =========================

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

    # =========================
    # CHECKOUT
    # =========================

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

    # =========================
    # SUCCESS
    # =========================

    path(
        "success/",
        views.success,
        name="success",
    ),

    # =========================
    # TRACK ORDER
    # =========================

    path(
        "track-order/",
        views.track_order,
        name="track_order",
    ),

]
