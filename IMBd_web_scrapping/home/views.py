from django.shortcuts import render
from .scraper_util import fetch_data
from .whoosh_util import get_index, list_filtered_elements, list_all_elements_sorted, list_all_elements, search_in_index
from django.shortcuts import render
from whoosh.index import open_dir


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

def search_results(request):
    """
    Vista para procesar la búsqueda en el índice de Whoosh.
    """
    query = request.GET.get('query', '')  # Nombre ingresado
    field = request.GET.get('field', '')  # Categoría seleccionada
    results = []

    if query and field:
        try:
            # Abre el índice
            index_dir = "index"
            index = open_dir(index_dir)

            # Realiza la búsqueda
            results = search_in_index(index, field, query)
        except Exception as e:
            print(f"Error durante la búsqueda: {e}")

    return render(request, 'search_results.html', {'results': results, 'query': query, 'field': field})

def search_page(request):
    """
    Vista para mostrar el formulario de búsqueda.
    """
    return render(request, 'search.html')
