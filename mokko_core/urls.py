"""
URL configuration for mokko_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from menu.views import HomeView, CoffeeView, BlogView, AboutView, ContactView, CoffeesView, BlogDetailView, client_contact_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home_list'),
    path('coffees/', CoffeesView.as_view(), name='coffee_list'),
    path('coffee/<int:pk>/', CoffeeView.as_view(), name='coffee_detail_url'),
    path('blog/', BlogView.as_view(), name='blog_list'),
    path('about/', AboutView.as_view(), name='about_list'),
    path('contact/', ContactView.as_view(), name='contact_list'),
    path('blog-detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail_url'),
    path('home/client-contact-create/', client_contact_create_view)


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
