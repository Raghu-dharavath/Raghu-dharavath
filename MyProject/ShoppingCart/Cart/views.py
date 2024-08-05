
from django.http import request
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect,render
from django.views.decorators.http import require_POST
from rest_framework import status,viewsets
from .models import Product
from .serializers import ProductSerializer




# class ProductDetails(APIView):
#     serializer_class = ProductSerializer
#     def get(self, request):
#         data = Product.objects.all()
#         serializer = ProductSerializer(data, many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer = ProductSerializer(data=request.data)
#         if(serializer.is_valid()):
#             Product.objects.all(
#                                  id=serializer.data.get("id"),
#                                  name=serializer.data.get("name"),
#                                  sku = serializer.data.get("sku"),
#                                  price = serializer.data.get("Price"),
#                                  quantity_in_stock = serializer.data.get("Quantity")
#                                 )
#         product = Product.objects.all().filter(id=request.data['id']).values()
#         return Response({'Message':'New Product added!','New_Product':product})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def add_to_cart(request, sku):
    product = get_object_or_404(Product, sku=sku)
    quantity = int(request.POST.get('quantity',1))

    cart = request.session.get('cart', {})
    cart[sku] = cart.get(sku, 0) + quantity
    request.session['cart'] = cart
    return redirect('cart')

def view_cart(request):
    cart = request.session.get('cart')
    product_in_cart = []
    total_cost = 0

    for sku, quantity in cart.items():
        product = get_object_or_404(Product,sku=sku)
        total_cost += product.price*quantity
        product_in_cart.append({
            'product':product,
            'quantity':quantity,
            'subtotal':product.price*quantity
        })

    context = {
        "product_in_cart":product_in_cart,
        "total_cost":total_cost
    }
    return render(request, 'cart.html', context)