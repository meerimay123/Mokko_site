from django.contrib import admin
from menu.models import Coffee
from menu.models import Publication


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']
