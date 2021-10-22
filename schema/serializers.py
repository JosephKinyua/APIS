
  
from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title', 'description','image', 'posted_on', 'user')
        model = Post
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields =('customer','address','contact','orders','total_sale')
        model = Customer

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        fields =('id','name', 'course', 'status', 'price', 'image', 'num_order', 'content_description', 'location')
        model = Food

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        fields =('staff_id', 'address', 'contact', 'salary', 'role')
        model = Staff

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields =('customer_id','customer', 'order_timestamp', 'delivery_timestamp', 'payment_status', 'delivery_status', 'if_cancelled', 'total_amount', 'payment_method', 'location', 'delivery_boy')
        model = Order

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields =('user','content')
        model = Comment

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        fields =('id','date','sales','expenses')
        model = Data

class OrderContentSerializer(serializers.ModelSerializer):
    class Meta:
        fields =('id','food','order')
        model = OrderContent

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        fields =('id','food','user', 'amount', 'image')
        model = Cart

class DeliveryBoySerializer(serializers.ModelSerializer):
    class Meta:
        fields =('order','delivery_boy')
        model = DeliveryBoy  