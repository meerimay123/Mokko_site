from django.contrib import admin
from menu.models import Coffee


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    pass
