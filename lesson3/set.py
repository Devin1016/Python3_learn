student_set = {'zs', 'lx', 'ww'}
print(student_set)

student_list = ['id1', 'id2', 'id3', 'id1', 'id2']
student_set = set(student_list)
print(student_set)

string_set = set('hello')
print(string_set)

none_set = set()

user_id = 'id1'
user_id5 = 'id5'

if user_id in student_set:
    print(user_id)

if user_id5 not in student_set:
    print(user_id5)

student_set.add('lw')
print(student_set)

s1 = {'zs', 'lx', 'ww'}
s1.update(student_list)
print(s1)

s1.remove('zs')
print(s1)

s1.discard('ssss')

a = s1.pop()
print(a)

s2 = {1, 2, 3, 5, 7, 9}
s3 = {1, 2, 4, 6, 8, 0}

inter_set1 = s2 & s3
inter_set2 = s2.intersection(s3)

print(inter_set1)
print(inter_set2)

union_set1 = s2 | s3
union_set2 = s2.union(s3)

print(union_set1)
print(union_set2)

diff_set1 = s2 - s3
diff_set2 = s2.difference(s3)

print(diff_set1)
print(diff_set2)

sym_set1 = s2 ^ s3
sym_set2 = s2.symmetric_difference(s3)

print(sym_set1)
print(sym_set2)
