from django.contrib import admin
from .models import Pizza

class PizzaAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingrediants','vegetarian', 'price')
    search_fields = ['name']

# register the models here
admin.site.register(Pizza, PizzaAdmin)
