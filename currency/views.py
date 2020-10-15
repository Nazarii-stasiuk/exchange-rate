from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .utils import get_rate
from .models import CurrencyRate
from .serializers import CurrencySerializer
from .permissions import CURREMCY_NAME, IsAvailable
from datetime import datetime


class UpdateCurrency(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, *args, **kwargs):
        rate = get_rate(kwargs['symbol'])
        if rate:
            CurrencyRate(name=CURREMCY_NAME[kwargs['symbol']], slug=kwargs['symbol'], price=rate).save()
        return Response({'status': 'ok'})


class Rate(APIView):
    permission_classes = (IsAvailable, )
    serializer_class = CurrencySerializer

    def get(self, request):
        data = request.data
        symbol = data.get('symbol', None)
        date = data.get('date', None)
        if symbol is None:
            return Response({'msg': "Symbol is required parametr"}, status=400)
        if date is not None:
            date = datetime.strptime(date, '%m-%d-%Y').date()
            rate = CurrencyRate.objects.filter(slug=symbol, date__date=date)
            serializer = CurrencySerializer(rate, many=True)
        else:
            rate = CurrencyRate.objects.filter(slug=symbol).first()
            serializer = CurrencySerializer(rate)
        if serializer.data == []:
            return Response({'msg': "No data"}, status=400)
        return Response(serializer.data)

