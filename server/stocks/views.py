from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action


from stocks.models import Stock
from stocks.serializers import StockSerializer
from rest_framework.views import APIView


class StockViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Stock.objects.filter(is_good_character=True)
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

class StockUpdateListAPIView(APIView):
    
    def post(self, request, format=None):
        some_string = self.request.data.get('strSymbols')
        # x = 3
        # list_symbols = [some_string[y-x:y] for y in range(x, len(some_string)+x,x)]

        list_all = Stock.objects.all().values_list('symbol', flat=True)
        
        list_create = []
        list_update = []
        for i in some_string:
            if i not in list_all:
                list_create.append(i)
            else:
                list_update.append(i)
        
        Stock.objects.all().update(is_high_liquidity=False)
        for i in list_update:                
            Stock.objects.filter(symbol__in=list_update).update(is_high_liquidity=True)
        
        for i in list_create:                
            Stock.objects.create(symbol=i, is_high_liquidity=True)
            
        
        # [i.update_or_create(is_high_liquidity=True) for i in list_to_update]
        

        return Response({})
