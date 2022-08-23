from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from cart.models import Cart
from product.models import Product, ProductCategory  
from .serializers import CartSerializer, CustomerSerializer, ProductCategorySerializer, ProductSerializer
from api import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication




from rest_framework.permissions import IsAuthenticated
from order.models import Order, OrderDetails
from datetime import datetime

class ProductCategoryViews(ModelViewSet):
    http_method_names = ['get']
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.filter(status=True)


class ProductView(ModelViewSet):
    http_method_names = ['get']
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(status=True)

    def get_serializer_class(self):
        if self.kwargs.get('pk'):
            return serializers.GetProductSerializer
        return self.serializer_class

    def list(self,request):
        filterDict = {
            'status' : True
        }
        if request.GET.get('category_id'):
            filterDict['product_category_id'] = request.GET.get('category_id')
            
            if request.GET.get('search'):
                filterDict['name__contains'] = request.GET.get('search')
        queryset2 = Product.objects.filter(**filterDict)
        serializer = self.serializer_class(queryset2, many=True)
        return Response(serializer.data)


class CustomerView(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = User.objects.filter(is_superuser=False, is_staff=False)
    

class LoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES








class CartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer

    def get(self,request):
        queryset = Cart.objects.filter(user=request.user)
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)


    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            quantity = serializer.validated_data.get('quantity')
            product = serializer.validated_data.get('product')
            cart, _ = Cart.objects.get_or_create(user=request.user,product=product)
            
            if int(quantity) == 0:
                cart.delete()
            else:
                cart.quantity = quantity
                cart.save()
            return Response({'message' : 'success'})
        return Response(serializer.errors, status=400)


class CheckoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CheckoutSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            payment_id = serializer.validated_data.get('payment_id')
            transaction_id = serializer.validated_data.get('transaction_id')

            order = Order.objects.create(
                user=request.user,
                date_time = datetime.now()
                )
            carts =  Cart.objects.filter(user=request.user)
            for cart in carts:
                OrderDetails.objects.create(
                    order=order,
                    product=cart.product,
                    quantity=cart.quantity,
                    price=cart.product.price
                )
                cart.delete()
            return Response({'order_id':order.id}) 
        return Response(serializer.errors,status=400)


# New
class OrderView(ModelViewSet):
    http_method_names = ['get']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.OrderSerializer
    queryset = Order.objects.all()

  
  
    def get_serializer_class(self):
        if self.kwargs.get('id'):
            return serializers.OrderDetailsSerializer
        return self.serializer_class
        
   
   
   
   
   
   

   
   
   
   
   
   
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
