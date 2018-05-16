db_info = ('192.168.10.1', 3306, 'root', 'rood123')
ip = db_info[0]
port = db_info[1]
print('ip={},port={}'.format(ip, port))

one_tuple = ('zzzz',)
print(type(one_tuple))
none_tuple = ()

for info in db_info:
    print(info)
