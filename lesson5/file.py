import os
import shutil

f = open('test.txt', 'a', encoding='utf-8')
w_str1 = 'asdfjkljasdlf'
f.write(w_str1)
f.close()

f = open('test.txt', 'r', encoding='utf-8')
r_str = f.read()
print(r_str)
f.close()

f = open('test.txt', 'a', encoding='utf-8')
w_str2 = '132132123'
f.write(w_str2)
f.close()

f = open('test.txt', 'r', encoding='utf-8')
r_str = f.read()
f.close()
print(r_str)

f = open('test.txt', 'r', encoding='utf-8')
lines = f.readlines()
print(lines)
for line in lines:
    print(line)
f.close()

f = open('test.txt', 'r', encoding='utf-8')
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(line1, line2, line3)
f.close()

f = open('test.txt', 'a', encoding='utf-8')
f.writelines(['zs', 'ls', 'ww'])
f.close()

# os.rename('test.txt', 'file.txt')

with open('test.txt', 'a', encoding='utf-8') as f:
    f.writelines(['zs', 'ls', 'ww'])

print(os.getcwd())

os.mkdir('sks')

print(os.listdir('e://'))
print(os.listdir())

os.rmdir('sks')

shutil.rmtree('123')

print(os.getcwd())
os.chdir('d://')
print(os.getcwd())
