from django.views import View
from . import views
from django.urls import path,include
from rest_framework import routers


router = routers.DefaultRouter()
router.register('product-categories',views.ProductCategoryViews)
router.register('products',views.ProductView)
router.register('customers',views.CustomerView)
router.register('order',views.OrderView)

urlpatterns = [
    path('',include(router.urls)),
    path('login/',views.LoginView.as_view()),
    # path('register/',views.registerUser,name='register'),
    path('carts/',views.CartView.as_view()),
    path('checkout/',views.CheckoutView.as_view()),
    # path('order/',views.OrderView.as_view())
 ]


