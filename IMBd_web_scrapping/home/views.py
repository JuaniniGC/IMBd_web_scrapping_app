from django.shortcuts import render
from .scraper_util import fetch_data
from .whoosh_util import get_index, list_filtered_elements, list_all_elements_sorted, list_all_elements

def home(request):
    return render(request, 'home.html')

def load_data(request):
    data = fetch_data()
    return render(request, 'load.html', {'movies': data, 'sorted': 'nota media'})

def order_by_rate(request):
    index = get_index()
    data = list_all_elements_sorted(index, 'rate', reverse=True)
    return render(request, 'load.html', {'movies': data, 'sorted': 'nota media'})

def order_by_votes(request):
    index = get_index()
    data = list_all_elements_sorted(index, 'votes', reverse=True)
    return render(request, 'load.html', {'movies': data, 'sorted': 'votos'})

def order_by_duration(request):
    index = get_index()
    data = list_all_elements_sorted(index, 'duration')
    return render(request, 'load.html', {'movies': data, 'sorted': 'duración'})

def order_by_year(request):
    index = get_index()
    data = list_all_elements_sorted(index, 'year')
    return render(request, 'load.html', {'movies': data, 'sorted': 'año'})

def order_by_recommended_age(request):
    index = get_index()
    data = list_all_elements_sorted(index, 'recommended_age')
    return render(request, 'load.html', {'movies': data, 'sorted': 'edad recomendada'})

def order_by_title(request):
    index = get_index()
    data = list_all_elements_sorted(index, 'title')
    return render(request, 'load.html', {'movies': data, 'sorted': 'título'})

