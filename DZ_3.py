class Dog:
    def __init__(self, name, age, breed):
        self.name = name  # Кличка
        self.age = age  # Вік
        self.breed = breed  # Порода
        self.weight = 4  # Вага (1,5kg - 140kg)
        self.energy = 60  # Рівень енергії (0-100)
        self.hunger = 50  # Рівень голоду (0-100)
        self.happiness = 50  # Рівень щастя (0-100)

    def eat(self, food):
        if self.hunger < 100:
            self.hunger -= 20
            self.energy += 10
            print(f"{self.name} зїла {food}, і тепер меньш голодна")
        else:
            print(f"{self.name} не голодна")

    def play(self):
        if self.energy > 20:
            self.energy -= 20
            self.happiness += 20
            print(f"{self.name} поргалася, і зараз щасливіша!")
        else:
            print(f"{self.name} не можу грати, хоче відпочити")

    def sleep(self):
        self.energy = 100
        self.happiness += 20
        print(f"{self.name} поспала!")

    def voice(self):
        print(f"{self.name} гав-гав")

    def status(self):
        print(f"\nІм'я: {self.name}\nВік: {self.age}\nПорода: {self.breed}\nВага: {self.weight}\n")
        print(f"Енергія: {self.energy}\nГолод: {self.hunger}\nЩастя: {self.happiness}\n")

class Owner:
    def __init__(self, name, age):
        self.name = name  # Ім'я власника
        self.age = age  # Вік власника
        self.dogs = []  # Список собак

    def adopt_dog(self, dog):
        self.dogs.append(dog)
        print(f"{self.name} всиновила собаку на ім'я {dog.name}!")

    def feed_dog(self, dog, food):
        if dog in self.dogs:
            dog.eat(food)
        else:
            print(f"{dog.name} не є собакою {self.name}!")

    def play_with_dog(self, dog):
        if dog in self.dogs:
            dog.play()
        else:
            print(f"{dog.name} не є собакою {self.name}!")

    def status(self):
        print(f"\nІм'я власника: {self.name}\nВік: {self.age}")
        print("Собаки власника:")
        for dog in self.dogs:
            print(f"- {dog.name} ({dog.breed})")


milashka = Dog(name="Мілашка", age=3, breed="Мальтезе")
zoriana = Owner(name="Зоряна", age=11)

zoriana.adopt_dog(milashka)
zoriana.status()
milashka.status()

zoriana.feed_dog(milashka, "Вкусняшку")
zoriana.play_with_dog(milashka)
milashka.status()

milashka.sleep()
milashka.voice()
zoriana.status()
