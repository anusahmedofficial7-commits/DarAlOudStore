from django.shortcuts import render, redirect, get_object_or_404
from .models import Perfume, PerfumeSize, Cart, Wishlist, Order
import random
import string


# =====================================
# HOME
# =====================================

def home(request):

    query = request.GET.get("q", "")

    perfumes = (
        Perfume.objects
        .prefetch_related("sizes")
        .order_by("-created_at")
    )

    if query:
        perfumes = perfumes.filter(
            name__icontains=query
        )

    return render(
        request,
        "home.html",
        {
            "perfumes": perfumes,
            "query": query,
        }
    )


# =====================================
# PRODUCT DETAIL
# =====================================

def product_detail(request, pk):

    perfume = get_object_or_404(
        Perfume,
        pk=pk
    )

    sizes = perfume.sizes.all()

    related_products = (
        Perfume.objects
        .exclude(pk=pk)
        .prefetch_related("sizes")
        .order_by("-created_at")[:4]
    )

    return render(
        request,
        "product_detail.html",
        {
            "perfume": perfume,
            "sizes": sizes,
            "related_products": related_products,
        }
    )
# =====================================
# WISHLIST
# =====================================

def wishlist(request):

    items = (
        Wishlist.objects
        .select_related("perfume")
        .prefetch_related("perfume__sizes")
    )

    return render(
        request,
        "wishlist.html",
        {
            "items": items,
        }
    )


def add_to_wishlist(request, pk):

    perfume = get_object_or_404(
        Perfume,
        pk=pk
    )

    Wishlist.objects.get_or_create(
        perfume=perfume
    )

    return redirect("wishlist")


def remove_wishlist(request, pk):

    item = get_object_or_404(
        Wishlist,
        pk=pk
    )

    item.delete()

    return redirect("wishlist")


# =====================================
# ADD TO CART
# =====================================

def add_to_cart(request, pk):

    perfume = get_object_or_404(
        Perfume,
        pk=pk
    )

    if request.method != "POST":
        return redirect(
            "product_detail",
            pk=pk
        )

    size_id = request.POST.get("size_id")

    if not size_id:
        return redirect(
            "product_detail",
            pk=pk
        )

    perfume_size = get_object_or_404(
        PerfumeSize,
        pk=size_id,
        perfume=perfume
    )

    cart_item, created = Cart.objects.get_or_create(
        perfume=perfume,
        size=perfume_size,
        defaults={
            "quantity": 1,
        }
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")
# =====================================
# CART
# =====================================

def cart(request):

    items = (
        Cart.objects
        .select_related(
            "perfume",
            "size"
        )
    )

    total = sum(
        item.subtotal
        for item in items
    )

    return render(
        request,
        "cart.html",
        {
            "items": items,
            "total": total,
        }
    )


# =====================================
# INCREASE QUANTITY
# =====================================

def increase_quantity(request, pk):

    item = get_object_or_404(
        Cart,
        pk=pk
    )

    item.quantity += 1
    item.save()

    return redirect("cart")


# =====================================
# DECREASE QUANTITY
# =====================================

def decrease_quantity(request, pk):

    item = get_object_or_404(
        Cart,
        pk=pk
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect("cart")


# =====================================
# REMOVE CART
# =====================================

def remove_cart(request, pk):

    item = get_object_or_404(
        Cart,
        pk=pk
    )

    item.delete()

    return redirect("cart")
# =====================================
# CHECKOUT
# =====================================

def checkout(request):

    items = Cart.objects.select_related(
        "perfume",
        "size"
    )

    total = sum(
        item.subtotal for item in items
    )

    return render(
        request,
        "checkout.html",
        {
            "items": items,
            "total": total,

            # EasyPaisa
            "easypaisa_name": "Talha Ahmed",
            "easypaisa_number": "03134292967",

            # Allied Bank
            "bank_name": "Allied Bank",
            "account_name": "Sumaira",
            "account_number": "01270011583826180022",
        }
    )


# =====================================
# PLACE ORDER
# =====================================

def place_order(request):

    if request.method != "POST":
        return redirect("checkout")

    customer_name = request.POST.get("customer_name")
    phone = request.POST.get("phone")
    email = request.POST.get("email")
    address = request.POST.get("address")

    payment_method = request.POST.get(
        "payment_method",
        "COD"
    )

    transaction_id = request.POST.get(
        "transaction_id",
        ""
    )

    cart_items = Cart.objects.select_related(
        "perfume",
        "size"
    )

    if not cart_items.exists():
        return redirect("cart")

    order_number = "DAO-" + "".join(
        random.choices(
            string.digits,
            k=8
        )
    )

    for item in cart_items:

        Order.objects.create(

            order_number=order_number,

            customer_name=customer_name,
            phone=phone,
            email=email,
            address=address,

            perfume=item.perfume,
            size=item.size,

            quantity=item.quantity,
            total_price=item.subtotal,

            payment_method=payment_method,
            transaction_id=transaction_id,

            payment_status="Pending",
            status="Pending",
        )

    cart_items.delete()

    return redirect("success")
# =====================================
# SUCCESS
# =====================================

def success(request):

    return render(
        request,
        "success.html"
    )


# =====================================
# TRACK ORDER
# =====================================

def track_order(request):

    order = None
    error = None

    if request.method == "POST":

        order_number = request.POST.get("order_number")
        phone = request.POST.get("phone")

        try:

            order = Order.objects.get(
                order_number=order_number,
                phone=phone
            )

        except Order.DoesNotExist:

            error = "Order not found. Please check your Order Number and Phone."

    return render(
        request,
        "track_order.html",
        {
            "order": order,
            "error": error,
        }
    )


# =====================================
# SEARCH
# =====================================

def search(request):

    query = request.GET.get("q", "")

    perfumes = (
        Perfume.objects
        .prefetch_related("sizes")
        .order_by("-created_at")
    )

    if query:
        perfumes = perfumes.filter(
            name__icontains=query
        )

    return render(
        request,
        "home.html",
        {
            "perfumes": perfumes,
            "query": query,
        }
    )# =====================================
# SUCCESS
# =====================================

def success(request):

    return render(
        request,
        "success.html"
    )


# =====================================
# TRACK ORDER
# =====================================

def track_order(request):

    order = None
    error = None

    if request.method == "POST":

        order_number = request.POST.get("order_number")
        phone = request.POST.get("phone")

        try:

            order = Order.objects.get(
                order_number=order_number,
                phone=phone
            )

        except Order.DoesNotExist:

            error = "Order not found. Please check your Order Number and Phone."

    return render(
        request,
        "track_order.html",
        {
            "order": order,
            "error": error,
        }
    )


# =====================================
# SEARCH
# =====================================

def search(request):

    query = request.GET.get("q", "")

    perfumes = (
        Perfume.objects
        .prefetch_related("sizes")
        .order_by("-created_at")
    )

    if query:
        perfumes = perfumes.filter(
            name__icontains=query
        )

    return render(
        request,
        "home.html",
        {
            "perfumes": perfumes,
            "query": query,
        }
    )
