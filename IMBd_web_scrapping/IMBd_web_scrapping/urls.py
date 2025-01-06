from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
import home.views as views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("load", views.load_data, name="load_data"),
    path("order_by_rate", views.order_by_rate, name="order_by_rate"),
    path("order_by_votes", views.order_by_votes, name="order_by_votes"),
    path("order_by_duration", views.order_by_duration, name="order_by_duration"),
    path("order_by_year", views.order_by_year, name="order_by_year"),
    path("order_by_recommended_age", views.order_by_recommended_age, name="order_by_recommended_age"),
    path("order_by_title", views.order_by_title, name="order_by_title"),
    path('search/', views.search_page, name='search_page'),  # Página del formulario
    path('search/results/', views.search_results, name='search_results'),
    path('comparison/year', views.movies_year_comparison, name='movies_comparison_year'),
    path('comparison/age', views.movies_duration_by_age, name='movies_comparison_age'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
