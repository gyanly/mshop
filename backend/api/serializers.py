from hashlib import new
from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from pyexpat import model
from rest_framework import serializers
from order.models import Order, OrderDetails
from product.models import Product, ProductCategory, ProductImage
from cart.models import Cart


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'   


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']

class ProductSerializer(serializers.ModelSerializer):
    # ProductImages = ProductImagesSerializer(many=True)
    class Meta:
        model = Product
        fields =  ['id','name','price','cover_image']
        
class GetProductSerializer(serializers.ModelSerializer):
    ProductImages = ProductImagesSerializer(many=True)
    class Meta:
        model = Product
        fields =  '__all__'
        depth = 1


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ['id','first_name','last_name','email','username','password']
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }


    def create(self,validatedData):
        user = User.objects.create(
            username = validatedData['username'],
            first_name = validatedData['first_name'],
            last_name = validatedData['last_name'],
            email = validatedData['email']
        )
        user.set_password(validatedData['password'])
        user.save() 
        return user 
       
    def update(self, userObject, validatedData):
        if validatedData.get('username'):
            userObject.username = validatedData.get('username',userObject.username)
        if validatedData.get('first_name'):
            userObject.first_name = validatedData.get('first_name',userObject.first_name)
        if validatedData.get('last_name'):    
            userObject.last_name = validatedData.get('last_name',userObject.last_name)
        if validatedData.get('email'):    
            userObject.email = validatedData.get('email',userObject.email)
        if validatedData.get('password'):
            userObject.set_password(validatedData.get('password'))
        userObject.save()
        return validatedData


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','product','quantity']


class CheckoutSerializer(serializers.Serializer):
    payment_id = serializers.CharField(max_length=40)
    transaction_id = serializers.CharField(max_length=40)


# New
class OrderDetailsSerializer(serializers.ModelSerializer):
    # Product = ProductSerializer(many=True)
    class Meta:
        model = OrderDetails
        fields = '__all__'
        depth = 1

class OrderSerializer(serializers.ModelSerializer):
    OrderDetails = OrderDetailsSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'
