from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from stocks.models import Stock
from stocks.serializers import StockSerializer

class StockViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Stock.objects.all()
        serializer = StockSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        stock = get_object_or_404(Stock, pk=pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = StockSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        stock = get_object_or_404(Stock, pk=pk)
        serializer = StockSerializer(stock, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        stock = get_object_or_404(Stock, pk=pk)
        stock.delete()
        return Response({})
