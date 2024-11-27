import json
import os
from datetime import datetime
from suntime import Sun, SunTimeException

# Função para salvar os dados no arquivo
def save_sun_times_to_file(latitude, longitude, sunrise, sunset, filename="sun_times.json"):
    data = {
        'latitude': latitude,
        'longitude': longitude,
        'sunrise': sunrise.strftime('%H:%M:%S'),
        'sunset': sunset.strftime('%H:%M:%S'),
        'date': datetime.now().strftime('%Y-%m-%d')
    }
    
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            file_data = json.load(f)
    else:
        file_data = []
    
    # Adiciona os novos dados
    file_data.append(data)
    
    # Salva os dados no arquivo
    with open(filename, 'w') as f:
        json.dump(file_data, f, indent=4)
    print("Dados salvos com sucesso.")

# Função para obter os dados de nascer e pôr do sol de um arquivo
def get_sun_times_from_file(latitude, longitude, filename="sun_times.json"):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            file_data = json.load(f)
        
        # Procurar pelos dados correspondentes à latitude e longitude
        for entry in file_data:
            if entry['latitude'] == latitude and entry['longitude'] == longitude:
                print("Dados encontrados no arquivo.")
                return entry['sunrise'], entry['sunset']
    
    return None, None

# Função para obter os horários de nascer e pôr do sol utilizando a biblioteca suntime
def get_sun_times_from_api(latitude, longitude):
    sun = Sun(latitude, longitude)
    
    try:
        sunrise = sun.get_sunrise_time()  # Nascer do sol
        sunset = sun.get_sunset_time()    # Pôr do sol
        
        # Retorna os horários como objetos datetime
        return sunrise, sunset
    except SunTimeException as e:
        print(f"Erro ao obter dados do sol: {e}")
        return None, None

# Função principal
def main(latitude, longitude, filename="sun_times.json"):
    # Primeiro, tentar obter os dados do arquivo
    sunrise, sunset = get_sun_times_from_file(latitude, longitude, filename)
    
    if sunrise is None or sunset is None:
        print("Dados não encontrados no arquivo. Consultando a API...")
        sunrise, sunset = get_sun_times_from_api(latitude, longitude)
        
        if sunrise and sunset:
            # Salvar os dados no arquivo para uso futuro
            save_sun_times_to_file(latitude, longitude, sunrise, sunset, filename)
        else:
            print("Não foi possível obter os dados do sol.")
            return
    
    # Exibir os horários do nascer e pôr do sol
    if sunrise and sunset:
        print(f"Nascer do sol: {sunrise.strftime('%H:%M:%S')}")
        print(f"Pôr do sol: {sunset.strftime('%H:%M:%S')}")

# Coordenadas geográficas (exemplo: Lisboa)
latitude = 38.7169
longitude = -9.1395

# Chamar a função principal
main(latitude, longitude)
