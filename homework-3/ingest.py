import requests
from bs4 import BeautifulSoup
import re
import os

def download_green_taxi_data(year=2022, folder_name='datasets'):
    # URL da página com os dados
    url = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"
    try:
        # Verifica se o diretório existe. Se não, cria o diretório
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Regex para identificar os links dos arquivos de táxi verde de 2022
        regex_pattern = f'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year}-[01][0-9].parquet'
        
        # Encontra todos os links na página
        links = soup.find_all('a', href=True)
        
        # Filtra os links com base no padrão regex definido
        green_taxi_links = [link['href'] for link in links if re.match(regex_pattern, link['href'])]
        
        # Download dos arquivos
        for file_url in green_taxi_links:
            file_name = file_url.split('/')[-1]
            print(f"Baixando {file_name} para o diretório {folder_name}...")
            file_response = requests.get(file_url)
            file_response.raise_for_status()  # Verifica se o download foi bem-sucedido
            
            # Salva o arquivo no diretório especificado
            with open(os.path.join(folder_name, file_name), 'wb') as file:
                file.write(file_response.content)
            print(f"{file_name} baixado com sucesso no diretório {folder_name}.")
            
    except requests.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")

# Chama a função para baixar os dados de táxi verde de 2022 para o diretório 'datasets'
download_green_taxi_data(2022, 'datasets')
