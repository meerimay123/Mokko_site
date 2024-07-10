from django.shortcuts import render
from django.views.generic import TemplateView
from menu.models import Coffee
from menu.models import Publication


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

    def get_context_data(self, **kwargs):
        coffee_pk =kwargs['pk']
        context = {
            'coffee': Coffee.objects.get(id=coffee_pk)
        }
        return context


class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = {
          'blog_list': Publication.objects.all()
        }
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'





