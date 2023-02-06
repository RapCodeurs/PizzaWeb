from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Pizza


# Create your views here.
def index(request):
    """pizzas = Pizza.objects.all()
    pizzas_names = [pizza.nom + " : " + str(pizza.prix) + "£" for pizza in pizzas]
    pizzas_names_str = ", ".join(pizzas_names)
    return HttpResponse("Les pizzas : " + pizzas_names_str)"""
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {'pizzas': pizzas})


def api_get_pizzas(request):
    pizzas = Pizza.objects.all()
    json = serializers.serialize("json", pizzas)
    return HttpResponse(json)
