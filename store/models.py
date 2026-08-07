from django.db import models
import random


# =====================================
# PAYMENT CHOICES
# =====================================

PAYMENT_CHOICES = (
    ("COD", "Cash On Delivery"),
    ("EasyPaisa", "EasyPaisa"),
    ("Allied Bank", "Allied Bank"),
)


PAYMENT_STATUS = (
    ("Pending", "Pending"),
    ("Paid", "Paid"),
    ("Rejected", "Rejected"),
)



# =====================================
# PERFUME
# =====================================

class Perfume(models.Model):

    name = models.CharField(max_length=200)

    brand = models.CharField(max_length=200)

    category = models.CharField(max_length=100)

    description = models.TextField()

    image = models.ImageField(
        upload_to="products/"
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        ordering = ["-created_at"]


    def __str__(self):
        return self.name




# =====================================
# PERFUME SIZE
# =====================================

class PerfumeSize(models.Model):

    perfume = models.ForeignKey(
        Perfume,
        on_delete=models.CASCADE,
        related_name="sizes"
    )


    size = models.CharField(
        max_length=20
    )


    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    class Meta:
        ordering = ["price"]


    def __str__(self):
        return f"{self.perfume.name} - {self.size}"





# =====================================
# CART
# =====================================

class Cart(models.Model):

    perfume = models.ForeignKey(
        Perfume,
        on_delete=models.CASCADE
    )


    size = models.ForeignKey(
        PerfumeSize,
        on_delete=models.CASCADE
    )


    quantity = models.PositiveIntegerField(
        default=1
    )


    @property
    def price(self):
        return self.size.price


    @property
    def subtotal(self):
        return self.size.price * self.quantity


    def __str__(self):
        return f"{self.perfume.name} ({self.size.size})"





# =====================================
# ORDER
# =====================================

class Order(models.Model):

    STATUS = (
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Processing", "Processing"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    )


    order_number = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )


    customer_name = models.CharField(
        max_length=150
    )


    phone = models.CharField(
        max_length=20
    )


    email = models.EmailField(
        blank=True,
        null=True
    )


    address = models.TextField()


    perfume = models.ForeignKey(
        Perfume,
        on_delete=models.CASCADE
    )


    size = models.ForeignKey(
        PerfumeSize,
        on_delete=models.CASCADE
    )


    quantity = models.PositiveIntegerField(
        default=1
    )


    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )


    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT_CHOICES,
        default="COD"
    )


    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="Pending"
    )


    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default="Pending"
    )


    ordered_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        ordering = ["-ordered_at"]



    def save(self, *args, **kwargs):

        if not self.order_number:

            self.order_number = (
                "DAO" +
                str(random.randint(100000, 999999))
            )

        super().save(*args, **kwargs)



    def __str__(self):
        return self.order_number





# =====================================
# WISHLIST
# =====================================

class Wishlist(models.Model):

    perfume = models.ForeignKey(
        Perfume,
        on_delete=models.CASCADE,
        related_name="wishlist_items"
    )


    def __str__(self):
        return self.perfume.name