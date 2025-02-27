from rest_framework import serializers
from .models import Category, Product, Order, Product_Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class Product_OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Order
        fields = '__all__'

'''
class TestSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ''
'''
    
class MenuSerializer(serializers.Serializer):
    떡볶이류 = Product.objects.filter(category=1 )
    사이드류 = Product.objects.filter(category=2 )
    세트메뉴 = Product.objects.filter(category=3 )
    모든메뉴 = Product.objects.all()
    
    class Meta:
        model = Category
        fields = ["떡볶이류", "사이드류","세트메뉴","모든메뉴"]