from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, Box, Order
from .serializers import ProductSerializer, BoxSerializer, OrderSerializer
from .services import recommend_box


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class BoxListCreateView(generics.ListCreateAPIView):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class RecommendBoxView(APIView):
    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        products = order.products.all()
        box = recommend_box(products)
        if box is None:
            return Response({
                "success": False,
                "message": "No suitable box found."
            })

        return Response({
            "success": True,
            "recommended_box": {
                "id": box.id,
                "name": box.name,
                "length": box.length,
                "width": box.width,
                "height": box.height,
                "max_weight": box.max_weight,
                "cost": str(box.cost)
            }
        })