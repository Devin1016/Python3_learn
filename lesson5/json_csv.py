import json
import csv

json_dict = {
        'name': 'zhangsan',
        'age': 20,
        'language': ['python', 'jave'],
        'study': {'AI': 'python', 'bigdata': 'hadoop'},
        'vip': True
    }

json_str = json.dumps(json_dict)
print(json_str)
print(type(json_str))

python_dict = json.loads(json_str)
print(python_dict)
print(type(python_dict))

with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(json_dict, f)

with open('test.json', 'r', encoding='utf-8') as f:
    js_dict = json.load(f)
    print(js_dict)

csv_list = [['name', 'age'], ['zhangsan', 20], ['lisi', 30]]

with open('test.csv', 'w', encoding='utf-8', newline='') as f:
    wroter = csv.writer(f)
    # for row in csv_list:
    #     wroter.writerow(row)
    wroter.writerows(csv_list)

with open('test.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)
    header = next(read)
    print(header)
    for row in read:
        print(row)

header = ['name', 'age', 'language', 'study', 'vip']
csv_dict = [{
        'name': 'zhangsan',
        'age': 20,
        'language': ['python', 'jave'],
        'study': {'AI': 'python', 'bigdata': 'hadoop'},
        'vip': True
    }, {
        'name': 'lisi',
        'age': 30,
        'language': ['python', 'jave'],
        'study': {'AI': 'python', 'bigdata': 'hadoop'},
        'vip': True
    }]

with open('test1.csv', 'w', encoding='utf-8', newline='') as f:
    write = csv.DictWriter(f, header)
    write.writeheader()
    write.writerows(csv_dict)

with open('test1.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row, row['name'])
