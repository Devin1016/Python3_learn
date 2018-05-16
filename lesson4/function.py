def set_name():
    name = 'zhangsan'
    return name


def get_name(name):
    print(name)


nm = set_name()
get_name(nm)

g_name = "wangwu"


def get_name1():
    print(g_name)


get_name1()

age = 20


def change_age():
    age = 25
    print(age)


def change_age1():
    global age
    age = 25
    print(age)


change_age()
print(age)
change_age1()
print(age)

g_num1 = 100


def print_global_num():
    print(g_num1)
    print(g_num2)
    # print(g_num3)


g_num2 = 200

print_global_num()

# g_num3 = 300

g_num_list = [1, 2, 3]
g_info_dict = {'name': 'zhangsan', 'age': 20}


def update_info():
    g_num_list.append(4)
    g_info_dict['gender'] = 'male'


update_info()
print(g_num_list, g_info_dict)


def x_y_sum(x, y=20):
    print(x)
    print(y)
    return x + y


res = x_y_sum(1)
print(res)
res = x_y_sum(1, 2)
print(res)


def x_y_sum(x=10, y=20):
    return x + y


res = x_y_sum(y=30, x=15)
print(res)


# *args封装为元组，**kvargs封装为字典
def any_num_sum(x, y=10, *args):
    print(args)
    rs = x + y
    if len(args) > 0:
        for arg in args:
            rs += arg
    return rs


res = any_num_sum(20)
print(res)
res = any_num_sum(20, 30)
print(res)
res = any_num_sum(20, 30, 40, 50, 60)
print(res)


def any_num_sum1(x, *args, y=10):
    print(args)
    rs = x + y
    if len(args) > 0:
        for arg in args:
            rs += arg
    return rs


res = any_num_sum1(20)
print(res)
res = any_num_sum1(20, 30)
print(res)
res = any_num_sum1(20, 30, 40, 50, 60, y=50)
print(res)


def social_insurance_comp(basic_money, **proportion):
    print(proportion)
    e_money = basic_money * proportion['e']
    m_money = basic_money * proportion['m']
    a_money = basic_money * proportion['a']
    total_money = e_money + m_money + a_money
    return total_money, e_money, m_money, a_money


t, e, m, a = social_insurance_comp(8000, e=0.2, m=0.1, a=0.12)
print(t, e, m, a)


def salary_comp(basic_money, *other_money, **proportion):
    print(basic_money)
    print(other_money)
    print(proportion)
    res = basic_money
    money_tuple = social_insurance_comp(basic_money, **proportion)
    for money in other_money:
        res += money
    res = res - money_tuple[0]
    return res


other_money = (500, 200, 100, 1000)
proportion_dict = {'e': 0.2, 'm': 0.1, 'a': 0.12}
money = salary_comp(8000, *other_money, **proportion_dict)
print(money)


# 递归函数
def recursive_for(num):
    if num > 1:
        res = num * recursive_for(num - 1)
    else:
        res = num
    return res


res = recursive_for(5)
print(res)

# res_sum = lambda x, y: x + y
# print(res_sum(1, 3))


def x_y_comp(x, y, func):
    res = func(x, y)
    return res


res = x_y_comp(2, 3, lambda x, y: x - y)
print(res)

user_info_dict = [{
    'name': 'zhangsan',
    'age': 20
}, {
    'name': 'lisi',
    'age': 30
}, {
    'name': 'wangwu',
    'age': 17
}]

print(user_info_dict)
user_info_dict.sort(key=lambda info: info['age'], reverse=True)
print(user_info_dict)
