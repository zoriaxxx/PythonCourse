import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self):
        self.exchange_rate = self.get_usd_exchange_rate()

    def get_usd_exchange_rate(self):
        # Отримуємо курс долара США за допомогою парсингу HTML-сторінки НБУ.
        url = "https://bank.gov.ua/ua/markets/exchangerates"
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Знаходимо таблицю з курсами валют (шукаємо елемент <table> з класом "table")
            table = soup.find('table', class_='table')
            if not table:
                print("Таблицю з курсами валют не знайдено.")
                return None

            rows = table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                # Якщо рядок містить дані та містить валюту "USD"
                if columns and any(col.text.strip() == 'USD' for col in columns):
                    # Припускаємо, що курс знаходиться у 5-му стовпці (індекс 4)
                    if len(columns) >= 5:
                        rate_text = columns[4].text.strip().replace(',', '.')
                        try:
                            rate = float(rate_text)
                            return rate
                        except ValueError:
                            print("Неможливо перетворити курс в число.")
                            return None
                    else:
                        print("Неправильна структура рядка з даними.")
                        return None
            print("Курс долара не знайдено в таблиці.")
            return None

        except requests.exceptions.RequestException as e:
            print(f"Помилка при отриманні даних: {e}")
            return None
        except Exception as e:
            print(f"Несподівана помилка: {e}")
            return None

    def convert_to_usd(self, amount):
        #Конвертує суму в гривнях у долари США.

        if self.exchange_rate is None:
            print("Неможливо виконати конвертацію через відсутність курсу.")
            return None
        try:
            amount = float(amount)
        except ValueError:
            print("Будь ласка, введіть числове значення.")
            return None
        return round(amount / self.exchange_rate, 2)

# Перевірка
converter = CurrencyConverter()

if converter.exchange_rate:
    print(f"Поточний курс долара США: {converter.exchange_rate} грн")
    user_input = input("Введіть суму в гривнях: ")
    usd_amount = converter.convert_to_usd(user_input)
    if usd_amount is not None:
        print(f"Еквівалент у доларах США: {usd_amount} USD")
else:
    print("Не вдалося отримати курс долара США.")
