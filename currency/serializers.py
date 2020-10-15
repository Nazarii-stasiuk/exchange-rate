from rest_framework.serializers import ModelSerializer
from currency.models import CurrencyRate

class CurrencySerializer(ModelSerializer):
    
    class Meta:
        model = CurrencyRate
        fields = '__all__'