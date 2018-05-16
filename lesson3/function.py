def print_user_info():
    print('name:zs')
    print('age:20')
    print('gender:male')


def print_user_info2(name, age, gender):
    print('name:{}'.format(name))
    print('age:{}'.format(age))
    print('gender:{}'.format(gender))


def sum_return(x, y):
    res = x + y
    return res


print_user_info2('zs', 20, 'male')
res = sum_return(1, 3)
print(res)
