# Практическое занятие №16, блок 2, вариант 15.
# Класс «Животное»; наследники «Собака» и «Кошка» с породой.


class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age

    def describe(self):
        return f'Вид: {self.species}, возраст: {self.age} лет'


class Dog(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

    def describe(self):
        return f'{super().describe()}, порода: {self.breed}'

    def speak(self):
        return 'Гав!'


class Cat(Animal):
    def __init__(self, species, age, breed):
        super().__init__(species, age)
        self.breed = breed

    def describe(self):
        return f'{super().describe()}, порода: {self.breed}'

    def speak(self):
        return 'Мяу!'


if __name__ == '__main__':
    dog = Dog('Собака', 3, 'Лабрадор')
    cat = Cat('Кошка', 2, 'Сиамская')

    for pet in (dog, cat):
        print(pet.describe())
        print(pet.speak())

    generic = Animal('Хомяк', 1)
    print(generic.describe())
