user_info_list = ['悟空', 100, 'male', '取经']
user_info_dict = {'name': '悟空', 'age': 100, 'gender': 'male', 'job': '取经'}
print(user_info_dict)
user_info_dict['job'] = '取经|偷桃'
print(user_info_dict)
print('{}的年龄是{}性别是{}工作是{}'.format(user_info_dict['name'], user_info_dict['age'], user_info_dict['gender'], user_info_dict['job']))

user_info_dict['tel'] = 12312412432
print(len(user_info_dict))

for key in user_info_dict.keys():
    print(key, user_info_dict[key])

for value in user_info_dict.values():
    print(value)

for line, key in enumerate(user_info_dict):
    print(line, key, user_info_dict[key])

for item in user_info_dict.items():
    print(type(item), item)
    for info in item:
        print(info)

print(user_info_dict.get('tel'))
print(user_info_dict.get('123'))
print(user_info_dict.get('adr', 'earth'))

print(user_info_dict)

print(type(user_info_dict.items()))

for key, value in user_info_dict.items():
    print(key, value)
