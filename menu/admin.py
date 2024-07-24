from django.contrib import admin
from menu.models import Coffee
from menu.models import Publication, Feedback, MokkoContact


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']


@admin.register(Feedback)
class FeedbackAAdmin(admin.ModelAdmin):
    list_display = ['full_name']


@admin.register(MokkoContact)
class MokkoContact(admin.ModelAdmin):
    list_display = ('address', 'phone')

