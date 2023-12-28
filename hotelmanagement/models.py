from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from cloudinary.models import CloudinaryField


# Create your models here.
class User_type(models.Model):
    id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=50)

    def __str__(self):
        return self.user_type


class CustomUser(AbstractUser):
    # objects = models.Manager()
    id = models.AutoField(primary_key=True)
    profile = CloudinaryField("image")
    # profile = models.ImageField(upload_to="profiles/", default='profiles/default_profile.jpg')
    user_type = models.ForeignKey(User_type, on_delete=models.SET_NULL, null=True, default=None)
    is_active = models.BooleanField(default=True)
    customer_profit = models.DecimalField(decimal_places = 2, max_digits = 12, default=0.00)

    def update_customer_profit(instance):
        order = instance
        total_profit = Order.objects.filter(order_receiver=order).aggregate(Sum('menu_items__item_profit'))[
                           'menu_items__item_profit__sum'] or 0
        order.customer_profit = total_profit
        order.save()

class Restaurant(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default = 0.0)
    description = models.TextField()


class Table(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()


class MenuCategory(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class Cupon(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    ammount = models.DecimalField(max_digits = 7, decimal_places = 2)
    menu_item = models.ForeignKey('MenuItem', on_delete = models.CASCADE, null=True)
    used = models.BooleanField(default = False)

class MenuItem(models.Model):
    # objects = models.Manager()
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places = 2, max_digits = 12)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    ingredient_cost = models.DecimalField(decimal_places = 2, max_digits = 12, default = 0.0)
    item_profit = models.DecimalField(decimal_places = 2, max_digits = 12, default = 0.0)
    orders_number = models.IntegerField(default = 0)
    # image_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.item_profit = self.price - self.ingredient_cost
        super(MenuItem, self).save(*args, **kwargs)

    def update_cost(instance):
        menu_item = instance
        total_cost = Ingredient.objects.filter(menu_item=menu_item).aggregate(Sum('price'))['price__sum'] or 0
        menu_item.ingredient_cost = total_cost
        menu_item.save()

    def update_orders_number(instance):
        menu_item = instance
        total_number = Order.objects.filter(menu_items=menu_item).count()
        menu_item.orders_number = total_number
        menu_item.save()


class MenuItemRating(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)  # Link the rating to a user
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, default=None)
    rating = models.DecimalField(decimal_places=1, max_digits=2, default = 0.0)
    comment = models.TextField(max_length=200, default="No comment")


class MenuImage(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    image = CloudinaryField("image")
#     image = models.ImageField(upload_to="menus/")
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)


class Reservation(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    guest_name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
    party_size = models.PositiveIntegerField()


class Order(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    # menu_items = models.ManyToManyField(MenuItem, through='OrderItem')
    menu_items = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True)
    ordered_time = models.DateTimeField(auto_now = True)
    start_processing_time = models.DateTimeField(null=True, blank=True)
    received_time = models.DateTimeField(null=True, blank=True)
    order_processor = models.ForeignKey(CustomUser, related_name="processor", on_delete=models.DO_NOTHING, null=True)
    order_receiver = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)
    send = models.BooleanField(default=False)
    latitude = models.DecimalField(max_digits = 18, decimal_places = 15, default=-6.216848786038759)
    longitude = models.DecimalField(max_digits = 18, decimal_places = 15, default=35.810966491699226)


class OrderItem(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Review(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    guest_name = models.CharField(max_length=255)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default = 0.0)
    comment = models.TextField()
    date = models.DateTimeField()


class Ingredient(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=50)
    measured_in = models.CharField(max_length=50)
    quantity = models.FloatField()
    price = models.DecimalField(decimal_places = 2, max_digits = 12)


class Employee(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    role = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default = 0.0)


class Payment(models.Model):
    objects = models.Manager()
    id = models.AutoField(primary_key=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default = 0.0)
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
        ("Waiter", "Waiter"),
        ("customer", "Customer"),
        ("None", "None")
    )

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


@receiver(post_save, sender=Ingredient)
@receiver(post_delete, sender=Ingredient)
def update_menu_item(sender, instance, **kwargs):
    instance.menu_item.update_cost()


@receiver(post_save, sender=Order)
def update_menu_item(sender, instance, **kwargs):
    instance.order_receiver.update_customer_profit()


@receiver(post_save, sender=Order)
@receiver(post_delete, sender=Order)
def update_menu_item(sender, instance, **kwargs):
    instance.menu_items.update_orders_number()

# @receiver(post_save, sender = MenuImage)
# @receiver(post_delete, sender = MenuImage)
# def copy_image(instance):
#     id = instance.menu_item
#     menu_image = MenuImage.objects.filter(menu_item = instance).first()
#     instance.menu_item.image_url = menu_image.image.url
#     instance.menu_item.save()
    