import os
from bs4 import BeautifulSoup
import requests
import random
from selenium import webdriver
import time
import re
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from .whoosh_util import add_to_index, create_index

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.67 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.1 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/90.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
]

def fetch_data():
    print("Fetching data from IMDb website...")
    url = "https://www.imdb.com/chart/top/"
    data = []
    version = random.choice(user_agents)
    headers = { 'headers': {'User-Agent': version} }
    response = requests.get(url, **headers)

    if response.status_code != 200:
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
        return data  
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    contenedor = soup.find('ul', class_='ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 iyTDQy compact-list-view ipc-metadata-list--base')
    
    movies_list = contenedor.find_all('li', class_='ipc-metadata-list-summary-item sc-4929eaf6-0 DLYcv cli-parent')
    
    if not movies_list:
        print("No movies found. Check the HTML structure or class names.")
        return data
    
    print(f"Found {len(movies_list)} movies.")    
    
    index = create_index()
    writer = index.writer()
    
    for movie in movies_list:
        title = remove_leading_number(movie.find('h3', class_='ipc-title__text').text)
        info_text = movie.find('div', class_='sc-300a8231-6 dBUjvq cli-title-metadata').text
        year_text, duration_text, recommended_age_text = separate_info_text(info_text)
        year = int(year_text)
        duration = parse_hours(duration_text)
        recommended_age = parse_recommendation_age(recommended_age_text)
        rate = float(movie.find('span', class_='ipc-rating-star--rating').text)
        number_of_votes = parse_number_of_votes(movie.find('span', class_='ipc-rating-star--voteCount').text)
        data.append({
            'title': title,
            'year': year,
            'duration': duration,
            'rate': rate,
            'votes': number_of_votes,
            'recommended_age': recommended_age
        })  
        writer.add_document(
            title=title,
            year=year,
            duration=duration,
            rate=rate,
            votes=number_of_votes,
            recommended_age=recommended_age
        )
    writer.commit()
    return data

def parse_hours(duration_str):
    match = re.search(r'(?:(\d+)h)?\s*(?:(\d+)m)?', duration_str.strip())

    if not match:
        raise ValueError("Formato inválido. Use 'Xh Ym', 'Xh', o 'Ym'.")
    
    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    
    total_minutes = hours * 60 + minutes
    return total_minutes

def parse_number_of_votes(text):
    match = re.search(r'\((\d+(\.\d+)?)([MK])\)', text.strip())

    if not match:
        raise ValueError("Formato inválido. Use texto en el formato '(X.XM)' o '(X.XK)'.")

    # Extraer partes del número
    number = float(match.group(1))  
    suffix = match.group(3)         

    # Convertir según el sufijo
    if suffix == 'M':  
        return int(number * 1_000_000)
    elif suffix == 'K':  
        return int(number * 1_000)
    else:
        raise ValueError("Sufijo no reconocido. Use 'M' para millones o 'K' para miles.")

def separate_info_text(text):
    match = re.match(r'(\d{4})(.*)(\d{2}|A)$', text.strip(), re.IGNORECASE)
    
    if not match:
        raise ValueError(f"El texto '{text}' no coincide con el formato esperado.")
    
    first_part = match.group(1)  # Primeros 4 dígitos
    middle_part = match.group(2)  # Parte del medio hasta 'min'
    last_part = match.group(3)  # Último valor (2 dígitos o 'A')
    
    return first_part, middle_part, last_part

def remove_leading_number(text):
    result = re.sub(r'^\d+\.\s*', '', text)
    return result

def parse_recommendation_age(text):
    if text == 'A':
        return "Todos los públicos"    
    else:
        return text