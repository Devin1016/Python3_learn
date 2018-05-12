num1 = input('请输入第一个数字：')
operator1 = input('请输入运算符：')
num2 = input('请输入第二个数字：')

num_1 = int(num1)
num_2 = int(num2)

if operator1 == '+':
    result = num_1 + num_2
elif operator1 == '-':
    result = num_1 - num_2
elif operator1 == '*':
    result = num_1 * num_2
elif operator1 == '/':
    result = num_1 + num_2
elif operator1 == '%':
    result = num_1 + num_2
elif operator1 == '**':
    result = num_1 + num_2
elif operator1 == '//':
    result = num_1 + num_2
else:
    result = 'wrong'

if result != 'wrong':
    print('结算结果为：{}'.format(result))
else:
    print('输入有错误')
