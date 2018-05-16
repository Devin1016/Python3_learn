for i in range(0, 10, 2):
    print(i)

lst = [1, 3, 5, 7, 9]

for i in lst:
    if i < 6:
        print(i)
    else:
        break

for i in lst:
    if i == 5:
        continue
    else:
        print(i)

s = 'hello'

for i in s:
    print(i)
