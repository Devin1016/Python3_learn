class Person:
    sum_num = 0

    def __init__(self, new_name, new_num):
        self.name = new_name
        # self.sum_num = 10
        # Person.sum_num += 1

    @classmethod
    def add_sum_num(cls):
        cls.sum_num += 1
        print(cls.sum_num)

    @staticmethod
    def static_test():
        print('静态方法')
        Person.sum_num += 1
        print(Person.sum_num)


# p1 = Person('zhangsan')
# p1.sum_num = 2
# print(p1.sum_num, Person.sum_num)
# p2 = Person('lisi')
# print(p1.sum_num, p2.sum_num, Person.sum_num)

# p1 = Person('zhangsan', 10)
# print(p1.sum_num, Person.sum_num)

Person.add_sum_num()
p1 = Person('zhangsan', 20)
p1.add_sum_num()

Person.static_test()
p1.static_test()
