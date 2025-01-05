"""
URL configuration for IMBd_web_scrapping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from home.views import home, load_data, order_by_rate, order_by_votes, order_by_duration, order_by_year, order_by_recommended_age, order_by_title

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path("load", load_data, name="load_data"),
    path("order_by_rate", order_by_rate, name="order_by_rate"),
    path("order_by_votes", order_by_votes, name="order_by_votes"),
    path("order_by_duration", order_by_duration, name="order_by_duration"),
    path("order_by_year", order_by_year, name="order_by_year"),
    path("order_by_recommended_age", order_by_recommended_age, name="order_by_recommended_age"),
    path("order_by_title", order_by_title, name="order_by_title")
]
