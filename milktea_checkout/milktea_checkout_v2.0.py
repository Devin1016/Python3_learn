'''
    项目名称：小象奶茶馆价格结算系统
    日期：2018/5/12
    版本：V2.0
'''


def main():
    vistor = 0
    vip_list = []
    sold_list = []

    while vistor < 5:
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

            print('你是今天第{}位幸运顾客！'.format(vistor + 1))

            qty = int(input('请输入你需要的数量：'))
            money = price * qty
            sold_list_once = []

            vip = input('请输入会员号：(新顾客直接设置会员号，下次消费才可享受会员价。)')
            if vip in vip_list:
                money *= 0.9
                vistor += 1
                print('今天第{}位顾客，你购买的{}，一共{}杯，您的会员价位{}元。'.format(vistor, mt_type, qty, money))
                sold_list_once.append(vip)
                sold_list_once.append(mt_type)
                sold_list_once.append(qty)
                sold_list_once.append(money)
                sold_list.append(sold_list_once)
            else:
                vip_list.append(vip)
                vistor += 1
                print('今天第{}位顾客，你购买的{}，一共{}杯，合计{}元。'.format(vistor, mt_type, qty, money))
                sold_list_once.append(vip)
                sold_list_once.append(mt_type)
                sold_list_once.append(qty)
                sold_list_once.append(money)
                sold_list.append(sold_list_once)
        else:
            print('Woops!我们只售卖以上五种奶茶哦！新口味敬请期待！')

    print('今日已闭店，欢迎明天光临！')
    print('VIP信息：{}'.format(vip_list))
    print('今日销售记录：{}'.format(sold_list))


if __name__ == '__main__':
    main()
