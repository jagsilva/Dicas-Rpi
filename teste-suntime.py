from suntime import Sun, SunTimeException
from datetime import datetime

# Coordenadas geográficas para a cidade de Lisboa, Portugal
latitude = 38.7169
longitude = -9.1395

# Criar uma instância da classe Sun com as coordenadas
sun = Sun(latitude, longitude)

# Obter o horário do nascer do sol para hoje
try:
    sunrise = sun.get_sunrise_time()  # Nascer do sol
    sunset = sun.get_sunset_time()    # Pôr do sol

    # Exibir os horários em formato legível
    print(f"Nascer do sol: {sunrise.strftime('%H:%M:%S')}")
    print(f"Pôr do sol: {sunset.strftime('%H:%M:%S')}")
    
    # Duração do dia em segundos
    day_length = sun.get_day_length()  # Duração do dia (em segundos)
    print(f"Duração do dia: {day_length / 3600:.2f} horas")

except SunTimeException as e:
    print(f"Erro ao obter dados do sol: {e}")
