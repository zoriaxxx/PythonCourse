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
            print(f"{self.name} з'їла {food}, і тепер менш голодна")
        else:
            print(f"{self.name} не голодна")

    def play(self):
        if self.energy > 20:
            self.energy -= 20
            self.happiness += 20
            print(f"{self.name} погралася, і зараз щасливіша!")
        else:
            print(f"{self.name} не може грати, хоче відпочити")

    def sleep(self):
        self.energy = 100
        self.happiness += 20
        print(f"{self.name} поспала!")

    def status(self):
        print(f"\nІм'я: {self.name}\nВік: {self.age}\nВага: {self.weight}")
        print(f"Енергія: {self.energy}\nГолод: {self.hunger}\nЩастя: {self.happiness}\n")


class Dog(Pet):
    def __init__(self, name, age, breed, weight):
        super().__init__(name, age, weight)
        self.breed = breed  # Порода

    def voice(self):
        print(f"{self.name} гав-гав")

    def status(self):
        super().status()
        print(f"Порода: {self.breed}\n")


class Cat(Pet):
    def __init__(self, name, age, color, weight):
        super().__init__(name, age, weight)
        self.color = color  # Колір шерсті

    def voice(self):
        print(f"{self.name} няв-няв")

    def status(self):
        super().status()
        print(f"Колір шерсті: {self.color}\n")


class Owner:
    def __init__(self, name, age):
        self.name = name  # Ім'я власника
        self.age = age  # Вік власника
        self.pets = []  # Список домашніх тварин

    def adopt_pet(self, pet):
        self.pets.append(pet)
        print(f"{self.name} всиновив(-ла) {type(pet).__name__.lower()} на ім'я {pet.name}!")

    def feed_pet(self, pet, food):
        if pet in self.pets:
            pet.eat(food)
        else:
            print(f"{pet.name} не є твариною {self.name}!")

    def play_with_pet(self, pet):
        if pet in self.pets:
            pet.play()
        else:
            print(f"{pet.name} не є твариною {self.name}!")

    def status(self):
        print(f"\nІм'я власника: {self.name}\nВік: {self.age}")
        print("Домашні тварини власника:")
        for pet in self.pets:
            print(f"- {pet.name} ({type(pet).__name__})")


my_dog = Dog(name="Мілашка", age=3, breed="Мальтезе", weight=4)
my_cat = Cat(name="Пушинка", age=2, color="Білий", weight=3)
owner = Owner(name="Зоряна", age=11)

owner.adopt_pet(my_dog)
owner.adopt_pet(my_cat)

owner.status()
my_dog.status()
my_cat.status()

owner.feed_pet(my_dog, "Вкусняшку")
owner.feed_pet(my_cat, "Рибку")

owner.play_with_pet(my_dog)
owner.play_with_pet(my_cat)

my_dog.sleep()
my_cat.sleep()

my_dog.voice()
my_cat.voice()

owner.status()