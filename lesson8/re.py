import re

# rs = re.match("chinahadoop", "chinahadoop.cn")

# print(rs)
# print(rs.group())

# rs = re.match('.', 'a')
# print(rs.group())

# rs = re.match('...', 'aadfasf')
# print(rs.group())

# rs = re.match('.', '1')
# print(rs.group())

# rs = re.match('.', '\n')
# print(rs)

# rs = re.match('\s', '\t')
# print(rs)

# rs = re.match('\s', '\n')
# print(rs)

# rs = re.match('\s', ' ')
# print(rs)

# rs = re.match('\S', '\t')
# print(rs)

# rs = re.match('\S', 'abc')
# print(rs)

# rs = re.match('\w', 'A')
# print(rs)

# rs = re.match('\w', 'a')
# print(rs)

# rs = re.match('\w', '1')
# print(rs)

# rs = re.match('\w', '_')
# print(rs)

# rs = re.match('\w', '我')
# print(rs)

# rs = re.match('\w', '*')
# print(rs)

# rs = re.match('[hH]', 'hello')
# print(rs)

# rs = re.match('[hH]', 'Hello')
# print(rs)

# rs = re.match('[0123456789]', '3')
# print(rs)
# rs = re.match('[0-9]', '3')
# print(rs)

# rs = re.match('1\d*', '1234')
# print(rs)

# rs = re.match('1\d*', '112312323asdfasdf4')
# print(rs)

# rs = re.match('\d+', 'adfasfa')
# print(rs)

# rs = re.match('\d+', '123adfasfa')
# print(rs)

# rs = re.match('\d?', 'adfasfa')
# print(rs)

# rs = re.match('\d?', '123adfasfa')
# print(rs)


# rs = re.match('\d{3}', '123adfasfa')
# print(rs)

# rs = re.match('\d{3}', '121233adfasfa')
# print(rs)

# rs = re.match('\d{1,}', '121233adfasfa')
# print(rs)

# rs = re.match('\d{0,1}', '121233adfasfa')
# print(rs)

# rs = re.match('1[3578]\d{9}', '13312345678')
# if rs:
#     print(rs)
# else:
#     print('不合法')

# str1 = r'hello\\world'
# str2 = r'hello\\world'
# str3 = r'hello\\\\world'
# rs = re.match('\w{5}\\\\\\\\\w{5}', str1)
# print(rs)
# rs = re.match(r'\w{5}\\\\\w{5}', str1)
# print(rs)
# rs = re.match(str2, str1)
# print(rs)
# rs = re.match(str3, str1)
# print(rs)

# rs = re.match('1[3578]\d{9}$', '13312345678')
# if rs:
#     print(rs)
# else:
#     print('不合法')

# rs = re.match('\w{3,10}@163.com$', 'hello123@163.com')
# print(rs)

# rs = re.match('\w{3,10}@163\.com$', '2113@163.com')
# print(rs)

# rs = re.match(r'.*\bpython\b', 'hi python hello')
# print(rs)

# rs = re.match(r'.*\Byt\B', 'hi python hello')
# print(rs)

# rs = re.match(r'100|[1-9][0-9]|[0-9]', '95')
# print(rs)

# rs = re.match(r'100$|[1-9]?\d?$', '100')
# print(rs)

# rs = re.match(r'\w{3,10}@(163|qq|outlook)\.(com|cn)$', '100@qq.com')
# print(rs)

# html_str = '<head><title>python</title></head>'
# rs = re.match(r'<.+><.+>.+</.+></.+>', html_str)
# print(rs)
# rs = re.match(r'<(.+)><(.+)>.+</\2></\1>', html_str)
# print(rs)

# html_str = '<head><title>python</head></title>'
# rs = re.match(r'<.+><.+>.+</.+></.+>', html_str)
# print(rs)
# rs = re.match(r'<(.+)><(.+)>.+</\2></\1>', html_str)
# print(rs)

# rs = re.match(r'<(?P<g1>.+)><(?P<g2>.+)>.+</(?P=g2)></(?P=g1)>', html_str)
# print(rs)

# re_str = 'haha car carbal abcar carbal'
# rs = re.search('car', re_str)
# print(rs)

# rs = re.findall('car', re_str)
# print(rs)

# mail_str = 'zhangsan:hello@163.com,li:123123@qq.cn'
# res_list = re.findall(r'(\w{3,20}@(163|qq|outlook)\.(com|cn))', mail_str)
# print(res_list)

# itor = re.finditer(r'\w{3,20}@(163|qq|outlook)\.(com|cn)', mail_str)
# for it in itor:
#     print(it.group())

# re_str = 'haha car carbal abcar carbal'
# rs = re.sub(r'car', r'python', re_str)
# print(rs)


def update_price(result):
    price = result.group()
    print(price)
    return str(int(price) + 1)


re_str = 'apple=5,banana=3,orange=2'
rs = re.sub(r'\d+', lambda result: str(int(result.group())+1), re_str)
print(rs)

re_list = rs.split(',')
print(re_list)
