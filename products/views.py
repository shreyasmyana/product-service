from django.http import HttpResponse
from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

# Create your views here.
def servicehealth(request):
    return HttpResponse("Products app is running")

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def search(self, request):
        name_query = request.query_params.get('name', None)
        if name_query:
            products = Product.objects.filter(name__icontains=name_query)
            serializer = self.get_serializer(products, many=True)
            return Response(serializer.data)
        return Response({"error": "Please provide a title to search for."}, status=400)