from django.shortcuts import render
from django.views.generic import TemplateView
from menu.models import Coffee


class HomeView(TemplateView):
    template_name = 'index.html'


class CoffeesView(TemplateView):
    template_name = 'coffees.html'

    def get_context_data(self, **kwargs):
        context = {
            'coffee_list': Coffee.objects.all()

        }
        return context


class CoffeeView(TemplateView):
    template_name = 'coffee.html'


class BlogView(TemplateView):
    template_name = 'blog.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'



