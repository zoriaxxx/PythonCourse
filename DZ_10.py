import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime


class WeatherScraper:
    def __init__(self):
        self.db_name = "weather.db"
        self.create_database()
        self.weather_url = "https://www.weather.com/weather/today/l/50.2547,28.6587?par=google"

    def create_database(self):
        """Створює БД з таблицею для збереження температури."""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                datetime TEXT,
                temperature REAL
            )
        """)
        conn.commit()
        conn.close()

    def fahrenheit_to_celsius(self, fahrenheit):
        """Конвертує температуру з Фаренгейтів у Цельсії."""
        return round((fahrenheit - 32) * 5.0 / 9.0, 2)

    def get_temperature(self):
        """Здійснює парсинг сайту погоди та повертає температуру у Житомирі в Цельсіях."""
        try:
            response = requests.get(self.weather_url, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Перевіряємо, чи вдалося отримати контент
            if soup is None:
                print("Помилка: отриманий HTML-код порожній або недоступний.")
                return None

            # Знаходимо елемент з температурою
            temp_element = soup.find('span', {'data-testid': 'TemperatureValue'})

            if temp_element:
                try:
                    temperature_fahrenheit = float(temp_element.text.strip().replace('°', ''))
                    temperature_celsius = self.fahrenheit_to_celsius(temperature_fahrenheit)
                    return temperature_celsius
                except ValueError:
                    print("Помилка: не вдалося перетворити значення температури.")
                    return None
            else:
                print("Не вдалося знайти температуру на сайті.")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Помилка при отриманні даних: {e}")
            return None
        except Exception as e:
            print(f"Несподівана помилка: {e}")
            return None

    def save_to_database(self, temperature):
        """Зберігає температуру в базу даних."""
        if temperature is not None:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute("INSERT INTO weather (datetime, temperature) VALUES (?, ?)", (current_datetime, temperature))
            conn.commit()
            conn.close()
            print(f"Дані збережено: {current_datetime}, Температура: {temperature}°C")
        else:
            print("Дані не були збережені через помилку.")

# Перевірка
scraper = WeatherScraper()
temp = scraper.get_temperature()
scraper.save_to_database(temp)
