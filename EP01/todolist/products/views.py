from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import ProductsModel
from .serializers import ProductsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


#  ----- APIView -----
class ApiViewAllProducts(APIView):
    def get(self, request):
        queryset = ProductsModel.objects.all()
        serializer = ProductsSerializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = ProductsSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'message': 'data is created'}, status=status.HTTP_201_CREATED)


class ApiViewProductsById(APIView):
    def get(self, request, pk):
        queryset = ProductsModel.objects.get(pk=pk)
        serializer = ProductsSerializer(queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        instance = get_object_or_404(ProductsModel.objects.all(), pk=pk)
        data = request.data
        serializer = ProductsSerializer(instance=instance, data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'success': 'update is successfully'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        instance = get_object_or_404(ProductsModel.objects.all(), pk=pk)
        instance.delete()
        return Response({'message': 'delete is successfully'}, status=status.HTTP_200_OK)


#  ----- GENERICS APIVIEW -----
class GenericsProductsListCreate(generics.ListCreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializer


class GenericsProductsById(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializer
