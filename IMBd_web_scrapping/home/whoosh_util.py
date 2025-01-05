from whoosh.fields import Schema, TEXT, NUMERIC, STORED
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
import os
import random
import requests
from bs4 import BeautifulSoup

def get_schema():
    return Schema(
        title=TEXT(stored=True),  # Título de la película
        year=NUMERIC(stored=True),  # Año de lanzamiento
        duration=NUMERIC(stored=True),  # Duración en minutos
        rate=NUMERIC(stored=True, decimal_places=1),  # Calificación
        votes=NUMERIC(stored=True),  # Número de votos
        recommended_age=TEXT(stored=True)  # Edad recomendada
    )

def create_index(index_dir="index"):
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    schema = get_schema()
    return create_in(index_dir, schema)

def add_to_index(index_writer, title, year, duration, rate, votes, recommended_age):
    index_writer.add_document(
        title=title,
        year=year,
        duration=duration,
        rate=rate,
        votes=votes,
        recommended_age=recommended_age
    )
    
def get_index(index_dir="index"):
    if not os.path.exists(index_dir) or not os.listdir(index_dir):
        print(f"Índice no encontrado en '{index_dir}', creando uno nuevo...")
        return create_index(index_dir)
    else:
        print(f"Índice encontrado en '{index_dir}'.")
        return open_dir(index_dir)

def list_filtered_elements(index, field_name, filter_value):
    results_list = []

    with index.searcher() as searcher:
        parser = QueryParser(field_name, index.schema)
        
        query = parser.parse(filter_value)

        results = searcher.search(query, limit=None) 
    
        for result in results:
            results_list.append(dict(result))
    
    return results_list

def list_all_elements_sorted(index, sort_field, reverse=False):
    results_list = []

    with index.searcher() as searcher:
        if sort_field not in index.schema.names():
            raise ValueError(f"El campo '{sort_field}' no existe en el esquema del índice.")

        results = searcher.documents()  
        sorted_results = sorted(results, key=lambda doc: doc.get(sort_field), reverse=reverse)
        
        for result in sorted_results:
            results_list.append(dict(result))
    
    return results_list


def list_all_elements(index):
    results_list = []

    with index.searcher() as searcher:
        results = searcher.documents()  
    
        for result in results:
            results_list.append(dict(result))
    
    return results_list