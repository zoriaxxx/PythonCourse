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
            print(f"{self.name} I ate, and now I am not hungry anymore!")
        else:
            print(f"{self.name} I don't hungry")

    def play(self):
        if self.energy > 20:
            self.energy -= 20
            self.happiness += 20
            print(f"{self.name} I played, and now I am more happy!")
        else:
            print(f"{self.name} I don't want to play")

    def sleep(self):
        self.energy = 100
        self.happiness += 20
        print(f"{self.name} I slept, and now I don't want to sleep!")

    def voice(self):
        print(f"{self.name} woof woof")

    def status(self):
        print(f"\nІм'я: {self.name}\nВік: {self.age}\nПорода: {self.breed}\nВага: {self.weight}\n")
        print(f"Енергія: {self.energy}\nГолод: {self.hunger}\nЩастя: {self.happiness}\n")


my_dog = Dog(name="Мілашка", age=3, breed="Мальтезе")
my_dog.status()
my_dog.eat(food="вкусняшку")
my_dog.play()
my_dog.status()
my_dog.sleep()
my_dog.voice()
my_dog.status()
