class Dog:
    def __init__(self, gender, variety, name, age):
        self.gender = gender
        self.variety = variety
        self.name = name
        self.__age = age
        print('构造方法,创建对象时自动调用')

    def get_pro(self):
        print(self.gender, self.variety, self.name, self.__age)

    def eat(self):
        print('啃骨头')

    def drink(self):
        print('喝水')

    def set_pro(self, **kvargs):
        if 'gender' in kvargs.keys():
            self.gender = kvargs['gender']
        if 'age' in kvargs.keys():
            if kvargs['age'] < 0 or kvargs['age'] > 20:
                print('非法年龄')
            else:
                self.__age = kvargs['age']


wangcai = Dog('male', 'golden', 'wangcai', 4)
wangcai.get_pro()
wangcai.eat()
wangcai.drink()
wangcai.get_pro()
wangcai.set_pro(gender='female', age=10)
wangcai.get_pro()


class Comrade:
    def __send_message(self):
        print('消息已经向上级汇报')

    def answer_secret(self, secret):
        if secret == '芝麻开门':
            print('接头成功')
            self.__send_message()
        else:
            print('接头失败')


comrade = Comrade()
comrade.answer_secret('芝麻开门')
