from django.contrib import admin
from .models import (
    Perfume,
    PerfumeSize,
    Cart,
    Wishlist,
    Order,
)


# =====================================
# PERFUME ADMIN
# =====================================

class PerfumeSizeInline(admin.TabularInline):
    model = PerfumeSize
    extra = 3


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "brand",
        "category",
        "stock",
        "created_at",
    )

    search_fields = (
        "name",
        "brand",
        "category",
    )

    list_filter = (
        "category",
        "brand",
    )

    inlines = [
        PerfumeSizeInline,
    ]


# =====================================
# PERFUME SIZE ADMIN
# =====================================

@admin.register(PerfumeSize)
class PerfumeSizeAdmin(admin.ModelAdmin):

    list_display = (
        "perfume",
        "size",
        "price",
    )

    search_fields = (
        "perfume__name",
        "size",
    )

    list_filter = (
        "size",
    )


# =====================================
# CART ADMIN
# =====================================

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        "perfume",
        "size",
        "price",
        "quantity",
        "subtotal",
    )

    search_fields = (
        "perfume__name",
    )


# =====================================
# WISHLIST ADMIN
# =====================================

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):

    list_display = (
        "perfume",
    )


# =====================================
# ORDER ADMIN
# =====================================

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "order_number",
        "customer_name",
        "phone",
        "perfume",
        "size",
        "quantity",
        "total_price",
        "payment_method",
        "payment_status",
        "status",
        "ordered_at",
    )

    search_fields = (
        "order_number",
        "customer_name",
        "phone",
        "perfume__name",
    )

    list_filter = (
        "payment_method",
        "payment_status",
        "status",
    )

    list_editable = (
        "payment_status",
        "status",
    )

    readonly_fields = (
        "order_number",
        "ordered_at",
    )

    ordering = (
        "-ordered_at",
    )

    list_per_page = 20
    