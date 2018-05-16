'''
    项目名称：小象奶茶馆价格结算系统
    日期：2018/5/12
    版本：V3.0
'''


def chose_milktea(shopping_car):
    milktea_type = input(
        '请选择口味：\n1）原味冰奶茶 3元\n2）香蕉冰奶茶 5元\n3）草莓冰奶茶 5元\n4）蒟蒻冰奶茶 7元\n5）珍珠冰奶茶 7元\n请选择你需要的口味：'
    )
    while milktea_type.lower() != 'q':
        if int(milktea_type) <= 5 and int(milktea_type) > 0:
            if milktea_type == '1':
                mt_type = '原味冰奶茶'
            elif milktea_type == '2':
                mt_type = '香蕉冰奶茶'
            elif milktea_type == '3':
                mt_type = '草莓冰奶茶'
            elif milktea_type == '4':
                mt_type = '蒟蒻冰奶茶'
            elif milktea_type == '5':
                mt_type = '珍珠冰奶茶'
            qty = int(input('请输入你需要的数量：'))
            shopping_car[mt_type] = qty
            milktea_type = input(
                '请选择口味：\n1）原味冰奶茶 3元\n2）香蕉冰奶茶 5元\n3）草莓冰奶茶 5元\n4）蒟蒻冰奶茶 7元\n5）珍珠冰奶茶 7元\n请选择你需要的口味：(结算请输入Q)'
            )
        else:
            print('Woops!我们只售卖以上五种奶茶哦！新口味敬请期待！')
            milktea_type = input(
                '请选择口味：\n1）原味冰奶茶 3元\n2）香蕉冰奶茶 5元\n3）草莓冰奶茶 5元\n4）蒟蒻冰奶茶 7元\n5）珍珠冰奶茶 7元\n请选择你需要的口味：(结算请输入Q)'
            )


def vip_check(vip_dict):
    vip_no = input('请输入会员号：')
    if vip_no in vip_dict.keys():
        vip = True
    else:
        vip_tel = input('请输入你的手机号，注册为会员：')
        vip_dict[vip_no] = vip_tel
        vip = False
    return vip_no, vip


def shopping_car_account(shopping_car):
    money = 0
    milktea_info_dict = {
        '原味冰奶茶': 3,
        '香蕉冰奶茶': 5,
        '草莓冰奶茶': 5,
        '蒟蒻冰奶茶': 7,
        '珍珠冰奶茶': 7
    }
    for milktea_type, milktea_counts in shopping_car.items():
        money += milktea_info_dict[milktea_type] * milktea_counts
    return money


def print_buy_info(shopping_car, vip):
    print('你的购买清单如下：')
    for milktea_type, milktea_counts in shopping_car.items():
        print('{}:{}杯'.format(milktea_type, milktea_counts))

    money = shopping_car_account(shopping_car)

    if vip:
        money *= 0.9
        print('你的奶茶会员结算价为：{}元'.format(money))
    else:
        print('你的奶茶结算价为：{}元'.format(money))


def shopping_log(shopping_car, sold_log_list, vip_no):
    for milktea_type, milktea_counts in shopping_car.items():
        sold_log = {}
        sold_log['vip_no'] = vip_no
        sold_log['milktea_type'] = milktea_type
        sold_log['milktea_counts'] = milktea_counts
        sold_log_list.append(sold_log)


def main():
    vistor = 0
    vip_info_dict = {}
    sold_log_list = []
    shopping_car = {}

    while vistor < 1:
        print('今天的第{}位顾客，欢迎光临小象奶茶馆！\n小象奶茶馆售卖宇宙无敌奶茶，奶茶虽好，可不要贪杯哦！'.format(
            vistor + 1))

        chose_milktea(shopping_car)
        vip_no, vip = vip_check(vip_info_dict)
        print_buy_info(shopping_car, vip)
        shopping_log(shopping_car, sold_log_list, vip_no)
        vistor += 1

    print('今日已闭店，欢迎明天光临！')
    print('VIP信息：{}'.format(vip_info_dict))
    print('今日销售记录：{}'.format(sold_log_list))


if __name__ == '__main__':
    main()
