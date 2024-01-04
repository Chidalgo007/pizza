from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza

# Create your views here.
def index(request):
    ''' this is an example of display 
    pizzas = Pizza.objects.all()
    pizza_inf = [f'{i.name}: ${i.price}' for i in pizzas]
    pizza_name_str = ', '.join(pizza_inf)
    return HttpResponse(f"Our Pizza: {pizza_name_str}")
    '''
    pizzas = Pizza.objects.all().order_by('price')
    return render(request, 'menu/index.html', {'pizzas':pizzas})

def api_get_pizza(request):
    pizzas = Pizza.objects.all().order_by('price')
    json = serializers.serialize("json",pizzas)
    return HttpResponse(json)