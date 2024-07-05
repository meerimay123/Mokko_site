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
from menu.views import HomeView, CoffeesView, CoffeeView, BlogView, AboutView, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view()),
    path('coffees/', CoffeesView.as_view()),
    path('coffee/', CoffeeView.as_view()),
    path('blog/', BlogView.as_view()),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)