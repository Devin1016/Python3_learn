str1 = 'hello world hello python'
str2 = 'world'

res = str1.find(str2)
res1 = str1.find(str2, 9)
print(res)
print(res1)

res = str1.count('hello')
print(res)

str2 = str1.replace('python', 'java')
print(str2)

res = str1.split(' ', 1)
print(res)

print(str1.startswith('h'))

print(str1.endswith('h'))

print(str1.upper())

print(str1.lower())
