class Dog:
    def eat(self):
        print('啃骨头')

    def drink(self):
        print('喝水')


wangcai = Dog()
print(id(wangcai))
wangcai.eat()
wangcai.drink()

afu = Dog()
print(id(afu))
afu.eat()
afu.drink()
