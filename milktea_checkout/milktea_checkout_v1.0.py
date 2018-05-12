'''
    项目名称：小象奶茶馆价格结算系统
    日期：2018/5/12
    版本：V1.0
'''


def main():
    milktea_type = input(
        '欢迎光临小象奶茶馆！\n小象奶茶馆售卖宇宙无敌奶茶，奶茶虽好，可不要贪杯哦！每次限尝鲜一种口味：\n1）原味冰奶茶 3元\n2）香蕉冰奶茶 5元\n3）草莓冰奶茶 5元\n4）蒟蒻冰奶茶 7元\n5）珍珠冰奶茶 7元\n请选择你需要的口味：'
    )

    if int(milktea_type) <= 5 and int(milktea_type) > 0:
        if milktea_type == '1':
            price = 3
            mt_type = '原味冰奶茶'
        elif milktea_type == '2':
            price = 5
            mt_type = '香蕉冰奶茶'
        elif milktea_type == '3':
            price = 5
            mt_type = '草莓冰奶茶'
        elif milktea_type == '4':
            price = 7
            mt_type = '蒟蒻冰奶茶'
        elif milktea_type == '5':
            price = 7
            mt_type = '珍珠冰奶茶'

        qty = int(input('请输入你需要的数量：'))
        money = price * qty

        vip = input('是否是会员：（y/n）')
        if vip == 'y':
            vip_money = money * 0.9
            print('你购买的{}，一共{}杯，您的会员价位{}元。'.format(mt_type, qty, vip_money))
        else:
            print('你购买的{}，一共{}杯，合计{}元。'.format(mt_type, qty, money))
    else:
        print('Woops!我们只售卖以上五种奶茶哦！新口味敬请期待！')


if __name__ == '__main__':
    main()
