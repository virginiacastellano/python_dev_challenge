import requests

class GeoAPI:
    # API Key, latitud y longitud de Pehuajó
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT = "-35.836948753554054"
    LON = "-61.870523905384076"
    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}"

    @classmethod
    def is_hot_in_pehuajo(cls):
        """
        Consulta la información del clima y devuelve True si la temperatura actual
        en Pehuajó supera los 28 grados Celsius, o False en caso contrario.
        Devuelve False ante cualquier excepción HTTP.
        """
        try:
            response = requests.get(cls.URL)  # Realiza una solicitud GET a la API del clima
            response.raise_for_status()  # Lanza una excepción si la respuesta no es exitosa (código de estado HTTP distinto de 200)
            weather_data = response.json()  # Obtiene los datos del clima en formato JSON
            temperature = weather_data["main"]["temp"]  # Obtiene la temperatura de los datos del clima
            temperature_celsius = temperature - 273.15  # Convierte la temperatura de Kelvin a Celsius
            return temperature_celsius > 28  # Retorna True si la temperatura supera los 28 grados Celsius, False en caso contrario
        except requests.exceptions.RequestException:
            return False  # Retorna False en caso de que ocurra una excepción durante la solicitud HTTP
