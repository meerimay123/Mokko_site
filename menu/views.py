from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from menu.models import Coffee, ClientContact
from menu.models import Publication, Feedback, MokkoContact


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'coffee_list': Coffee.objects.all(),
            'feedback_list': Feedback.objects.all(),
            'blog_list': Publication.objects.all(),
            'mokko_contact': MokkoContact.objects.first()
        }
        return context


class CoffeesView(TemplateView):
    template_name = 'coffees.html'

    def get_context_data(self, **kwargs):
        context = {
            'coffee_list': Coffee.objects.all(),
            'mokko_contact': MokkoContact.objects.first()

        }
        return context


class CoffeeView(TemplateView):
    template_name = 'coffee.html'

    def get_context_data(self, **kwargs):
        coffee_pk =kwargs['pk']
        context = {
            'coffee': Coffee.objects.get(id=coffee_pk),
            'mokko_contact': MokkoContact.objects.first()
        }
        return context


class BlogView(TemplateView):
    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = {
          'blog_list': Publication.objects.all(),
          'mokko_contact': MokkoContact.objects.first()
        }
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = {
            'mokko_contact': MokkoContact.objects.first()
        }
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = {
            'mokko_contact': MokkoContact.objects.first()
        }
        return context


class BlogDetailView(TemplateView):
    template_name = 'blog-detail.html'

    def get_context_data(self, **kwargs):
        blog_pk = kwargs['pk']
        context = {
            'publication': Publication.objects.get(id=blog_pk),
            'mokko_contact': MokkoContact.objects.first()
        }
        return context


def client_contact_create_view(request):
    print('это ваши данные от ПОСТ запроса', request.POST)
    input_name = request.POST['Your Name']
    input_email = request.POST['Your Email']
    input_phone = request.POST['Your Phone']
    input_message = request.POST['Massage']
    ClientContact.objects.create(name=input_name, email=input_email, phone=input_phone, message=input_message)

    return HttpResponse("<h1>Ваше сообщение было создано</h1>")


