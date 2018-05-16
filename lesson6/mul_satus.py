class Animal:
    def eat(self):
        print('animal吃饭')


class Dog(Animal):
    def eat(self):
        print('dog吃饭')


class Cat(Animal):
    def eat(self):
        print('cat吃饭')


def show_eat(obj):
    obj.eat()


wangcai = Dog()
show_eat(wangcai)
tom = Cat()
show_eat(tom)
