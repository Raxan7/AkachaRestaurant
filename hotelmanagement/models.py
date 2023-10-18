from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class User_type(models.Model):
    id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=50)

    def __str__(self):
        return self.user_type


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    profile = models.ImageField(upload_to="profiles/", default='profiles/default_profile.jpg')
    user_type = models.ForeignKey(User_type, on_delete=models.SET_NULL, null=True, default=None)
    is_active = models.BooleanField(default=False)


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()


class Table(models.Model):
    id = models.AutoField(primary_key=True)
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()


class MenuCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

class MenuItemRating(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Link the rating to a user
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()


class MenuImage(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="menus/")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    guest_name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
    party_size = models.PositiveIntegerField()


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    # menu_items = models.ManyToManyField(MenuItem, through='OrderItem')
    menu_items = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True)
    ordered_time = models.DateTimeField(default=datetime.datetime.now())
    start_processing_time = models.DateTimeField(null=True, blank=True)
    received_time = models.DateTimeField(null=True, blank=True)
    order_processor = models.ForeignKey(CustomUser, related_name="processor", on_delete=models.DO_NOTHING, null=True)
    order_receiver = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    send = models.BooleanField(default=False)

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    guest_name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField()
    date = models.DateTimeField()


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    role = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField()
    payment_method = models.CharField(max_length=255)


class Messages(models.Model):

    MESSAGE_TYPE = (
        ("Authorization", "Authorization"),
        ("Request", "Request"),
        ("Denial", "Denial"),
        ("Information", "Information"),
        ("Unknown", "Unknown")
    )

    USER_CATEGORY = (
        ("CEO", "CEO"),
        ("storekeeper", "Storekeeper"),
        ("chef", "Chef"),
        ("waiter", "Waiter"),
        ("customer", "Customer"),
        ("None", "None")
    )

    objects = models.Manager()
    sender = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name="message_sender")
    receiver_category = models.ForeignKey(User_type, on_delete=models.CASCADE, null=True)
    # receiver = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name="message_receiver")
    # receiver_category = models.CharField(choices=USER_CATEGORY, max_length=255, default=USER_CATEGORY[5])
    time_sent = models.DateTimeField(auto_now=True)
    time_opened = models.DateTimeField(null=True, blank=True)
    opened = models.BooleanField(default=False)
    message = models.TextField()
    message_type = models.CharField(choices=MESSAGE_TYPE, max_length=255, default=MESSAGE_TYPE[3])
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.message}"
