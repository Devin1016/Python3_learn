card_id = input('请输入卡号:')
pwd = int(input('请输入密码:'))

print('卡号：{}\n密码：{}'.format(card_id, pwd))
print('卡号：%s\n密码：%d' % (card_id, pwd))
print('卡号：%s\\n密码：%d' % (card_id, pwd))

height = 180.35

print('%.2f' % height)
print('{:.4f}'.format(height))

p = 99.99

print('%.2f%%' % p)

print('hello', end='')
print('python')
