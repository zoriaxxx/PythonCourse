def error_handling_decorator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            print(f"Результат: {result}")
            return result
        except ZeroDivisionError:
            print("Помилка: Ділення на нуль не дозволено.")
        except SyntaxError:
            print("Помилка: Невірний синтаксис виразу.")
        except NameError:
            print("Помилка: Вираз містить недопустимі символи або змінні.")
        except Exception as e:
            print(f"Несподівана помилка: {e}")
    return wrapper

@error_handling_decorator
def calculate(expression):
    return eval(expression)

# перевірка
calculate("5 + 5")
calculate("10 / 0")
calculate("5 + ")
calculate("abc + 5")
calculate("10 * 2")