from django.db.models import (
    Model, CharField, FloatField, DateTimeField, SlugField, SET_NULL, CASCADE)


class CurrencyRate(Model):
    name = CharField(max_length=50)
    slug = SlugField(blank=True)
    price = FloatField()
    date = DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name
    
    class Meta: 
        ordering = ['-date']
        db_table = "currency_rate"
    

        