import logging
import sqlite3

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='pet_simulation.log',
    filemode='w'
)

# Підключення до бази даних
conn = sqlite3.connect("pet_simulation.db")
cursor = conn.cursor()

# Створення таблиць
cursor.execute('''CREATE TABLE IF NOT EXISTS owners (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    weight REAL,
    type TEXT,
    owner_id INTEGER,
    FOREIGN KEY(owner_id) REFERENCES owners(id)
)''')

conn.commit()

class Pet:
    def __init__(self, name, age, weight):
        self.name = name  # Кличка
        self.age = age  # Вік
        self.weight = weight  # Вага
        self.energy = 60  # Рівень енергії (0-100)
        self.hunger = 50  # Рівень голоду (0-100)
        self.happiness = 50  # Рівень щастя (0-100)

    def eat(self, food):
        if self.hunger < 100:
            self.hunger -= 20
            self.energy += 10
            logging.info(f"{self.name} з'їла {food} і тепер менш голодна")
            print(f"{self.name} з'їла {food}, і тепер менш голодна")
        else:
            logging.warning(f"{self.name} не голодна")
            print(f"{self.name} не голодна")

    def play(self):
        if self.energy > 20:
            self.energy -= 20
            self.happiness += 20
            logging.info(f"{self.name} погралася, і зараз щасливіша!")
            print(f"{self.name} погралася, і зараз щасливіша!")
        else:
            logging.warning(f"{self.name} не може грати, хоче відпочити")
            print(f"{self.name} не може грати, хоче відпочити")

    def sleep(self):
        self.energy = 100
        self.happiness += 20
        logging.info(f"{self.name} поспала і тепер повна сил!")
        print(f"{self.name} поспала!")

    def status(self):
        logging.info(f"Статус {self.name}: Енергія={self.energy}, Голод={self.hunger}, Щастя={self.happiness}")
        print(f"\nІм'я: {self.name}\nВік: {self.age}\nВага: {self.weight}")
        print(f"Енергія: {self.energy}\nГолод: {self.hunger}\nЩастя: {self.happiness}\n")

class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.pets = []
        cursor.execute("INSERT INTO owners (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        self.id = cursor.lastrowid

    def adopt_pet(self, pet, pet_type):
        self.pets.append(pet)
        cursor.execute("INSERT INTO pets (name, age, weight, type, owner_id) VALUES (?, ?, ?, ?, ?)",
                       (pet.name, pet.age, pet.weight, pet_type, self.id))
        conn.commit()
        logging.info(f"{self.name} всиновив(-ла) {pet_type} на ім'я {pet.name}")
        print(f"{self.name} всиновив(-ла) {pet_type} на ім'я {pet.name}!")

    def status(self):
        logging.info(f"Статус власника {self.name}: {len(self.pets)} тварин")
        print(f"\nІм'я власника: {self.name}\nВік: {self.age}")
        print("Домашні тварини власника:")
        for pet in self.pets:
            print(f"- {pet.name} ({type(pet).__name__})")

# Перевірка
try:
    owner_name = input("Введіть ім'я власника: ")
    owner_age = int(input("Введіть вік власника: "))
    owner = Owner(name=owner_name, age=owner_age)

    while True:
        pet_name = input("Введіть ім'я тварини (або 'вихід' для завершення): ")
        if pet_name.lower() == 'вихід':
            break
        pet_age = int(input("Введіть вік тварини: "))
        pet_weight = float(input("Введіть вагу тварини: "))
        pet_type = input("Введіть тип тварини (Dog/Cat): ")
        pet = Pet(name=pet_name, age=pet_age, weight=pet_weight)
        owner.adopt_pet(pet, pet_type)

    owner.status()
except Exception as e:
    logging.critical(f"Несподівана помилка: {e}")
    print(f"Несподівана помилка: {e}")
