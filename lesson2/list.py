name_list = ['zs', 'ls', 'ww']
print(name_list[0])
name_list[0] = 'xb'
print(name_list[0])
name_list.append('lw')
name_list.insert(1, 'hhh')

for name in name_list:
    print(name)

i = 0

while i < len(name_list):
    print(name_list[i])
    i += 1

info_list = [[1, 3, 5], [2, 4, 6]]

for i in info_list:
    for j in i:
        print(j)

new_list = name_list + info_list
print(new_list)

name_list.extend(info_list)
print(name_list)

del name_list[0]
print(name_list)

name_list.remove('ls')
print(name_list)

name_list.pop()
print(name_list)
name_list.reverse()
print(name_list)

if 'ww' in name_list:
    print('11111')

num_list = [3, 5, 1, 0]
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)
