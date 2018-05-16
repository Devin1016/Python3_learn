class Animal:
    def __init__(self):
        print('构造animal')

    def __private_method(self):
        print('私有方法')

    def eat(self):
        print('吃')

    def drink(self):
        print('喝')

    def run(self):
        print('跑')


class Dog(Animal):
    def __init__(self):
        print('构造dog')

    def hand(self):
        print('握手')

    def run(self):
        print('摇着尾巴跑')


class GoldenDog(Dog):
    def guid(self):
        print('导航！')


wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.hand()

golden_dog = GoldenDog()
golden_dog.eat()
golden_dog.guid()
