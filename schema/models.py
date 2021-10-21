
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Customer(models.Model):
    pending = 'Pending'
    verified = 'Verified'

    STATUS = (
        (pending,pending),
        (verified,verified),
    )
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField()
    contact = models.CharField(max_length = 10)
    orders = models.IntegerField(default=0)
    total_sale = models.IntegerField(default=0)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    def __str__(self):
        return self.customer.first_name + " " + self.customer.last_name

class Staff(models.Model):
    admin = 'Admin'
    deliveryboy = 'Delivery Boy'
    chef = 'Chef'

    ROLES = (
        (admin,admin),
        (chef,chef),
        (deliveryboy,deliveryboy),
    )
    
    staff_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.TextField()
    contact = models.CharField(max_length = 10)
    email = User.email
    salary = models.IntegerField()
    role = models.CharField(max_length = 30, choices = ROLES)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    def __str__(self):
        return self.staff_id.first_name + " " + self.staff_id.last_name

class Order(models.Model):
    pending = 'Pending'
    completed = 'Completed'

    STATUS = (
        (pending,pending),
        (completed,completed),
    )

    cod = 'Cash On Delivery'
    card = 'Card Payment'
    upi = 'UPI Payment'

    PAYMENT = (
        (cod,cod),
        (card,card),
        (upi,upi),
    )

    pickup = 'PickUp'
    delivery = 'Delivery'

    TYPE = (
        (pickup, pickup),
        (delivery, delivery),
    )
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_timestamp = models.CharField(max_length=100, blank=True)
    delivery_timestamp = models.CharField(max_length=100, blank=True)
    payment_status = models.CharField(max_length = 100, choices = STATUS)
    delivery_status = models.CharField(max_length = 100, choices = STATUS)
    if_cancelled = models.BooleanField(default = False)
    total_amount = models.IntegerField()
    payment_method = models.CharField(max_length = 100, choices = PAYMENT)
    location = models.CharField(max_length=200, blank=True, null=True)
    delivery_boy = models.ForeignKey(Staff,on_delete=models.CASCADE, null=True, blank=True)

    def confirmOrder(self):
        self.order_timestamp = timezone.localtime().__str__()[:19]
        self.payment_status = self.completed
        self.save()

    def confirmDelivery(self):
        self.delivery_timestamp = timezone.localtime().__str__()[:19]
        self.delivery_status = self.completed
        self.save()
    
    def __str__(self):
        return self.customer.__str__()

class Food(models.Model):
    Tunisia = 'Tunisia Food'
    Ghana = 'Ghana Food'
    Somalian = 'Somalian Food'
    Kenyan = 'Kenyan Food'
    fast = 'Food'
    COURSE = (
        (Tunisia,Tunisia),
        (Ghana,Ghana),
        (Somalian,Somalian ),
        ( Kenyan,Kenyan),
        (fast,fast),
    )

    disabled = 'Disabled'
    enabled = 'Enabled'

    STATUS = (
        (disabled, disabled),
        (enabled, enabled),
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    course = models.CharField(max_length = 50, choices = COURSE)
    status = models.CharField(max_length=50, choices=STATUS)
    content_description = models.TextField()
    price = models.FloatField()
    image = CloudinaryField('image')
    location = models.CharField(max_length=200, blank=True, null=True)
    num_order = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    #def calculateSalePrice(self):
     #   self.sale_price = (100.0 - self.discount)/100.0 * self.base_price
    

class Comment(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)

class Data(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    sales = models.IntegerField()
    expenses = models.IntegerField()

class OrderContent(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=1)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    image = CloudinaryField('image')
    amount = models.IntegerField(default=1)
    quantity = models.IntegerField(default=1)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class DeliveryBoy(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    delivery_boy = models.ForeignKey(Staff, on_delete=models.CASCADE)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=144)
    description = models.TextField()
    image = CloudinaryField('image')
    posted_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    

