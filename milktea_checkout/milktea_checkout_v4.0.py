'''
    项目名称：小象奶茶馆价格结算系统
    日期：2018/5/12
    版本：V4.0
'''


def chose_milktea(shopping_car, vip_milktea_list):
    milktea_info_dict = {
        '1': '原味冰奶茶',
        '2': '香蕉冰奶茶',
        '3': '草莓冰奶茶',
        '4': '蒟蒻冰奶茶',
        '5': '珍珠冰奶茶'
    }
    user_buy_milktea_set = set()
    chose_str = '请选择口味：\n1）原味冰奶茶 3元\n2）香蕉冰奶茶 5元\n3）草莓冰奶茶 5元\n4）蒟蒻冰奶茶 7元\n5）珍珠冰奶茶 7元\n请选择你需要的口味(结算请输入Q,查看推荐奶茶输入T)：'
    if_hot = input('今日推荐奶茶为：蒟蒻冰奶茶，要不要尝试一下（y/n）：')
    if if_hot.lower() == 'y':
        milktea_type = '4'
    else:
        milktea_type = input(chose_str)
    while True:
        if milktea_type.lower() == 'q':
            vip_milktea_list.append(user_buy_milktea_set)
            break
        elif milktea_type.lower() == 't':
            recom_milktea = other_recommend(vip_milktea_list, user_buy_milktea_set)
            if recom_milktea is not None:
                print('为你推荐：{}'.format(recom_milktea))
                if_buy = input('是否尝试（y/n）？')
                if if_buy.lower() == 'y':
                    for key, value in milktea_info_dict.items():
                        if value == recom_milktea:
                            milktea_type = key
            else:
                print('暂时没有为你推荐的奶茶')
                milktea_type = input(chose_str)
            continue
        else:
            if milktea_type in milktea_info_dict.keys():
                qty = int(input('请输入你需要的数量：'))
                user_buy_milktea_set.add(milktea_info_dict[milktea_type])
                if milktea_info_dict[milktea_type] in shopping_car.keys():
                    shopping_car[milktea_info_dict[milktea_type]] += qty
                else:
                    shopping_car[milktea_info_dict[milktea_type]] = qty
            else:
                print('Woops!我们只售卖以上五种奶茶哦！新口味敬请期待！')
            milktea_type = input(chose_str)


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


def other_recommend(vip_milktea_list, user_buy_milktea_set):
    inner_list = []
    diff_list = []

    for other_milktype_set in vip_milktea_list:
        inner_set = user_buy_milktea_set & other_milktype_set
        if len(inner_set) > 0 and len(inner_set) < len(
                other_milktype_set):
            diff_set = other_milktype_set - inner_set
            inner_list.append(inner_set)
            diff_list.append(diff_set)

    if len(inner_list) > 0:
        len_list = []
        for length in range(len(inner_list)):
            len_list.append(length)

        index_list = []
        for i in range(len(len_list)):
            if len_list[i] == max(len_list):
                index_list.append(i)

        recom_set = set()
        for index in index_list:
            for diff_milktea in diff_list[index]:
                recom_set.add(diff_milktea)
        recom_milktea = recom_set.pop()
    else:
        if '蒟蒻冰奶茶' not in user_buy_milktea_set:
            recom_milktea = '蒟蒻冰奶茶'
        else:
            recom_milktea = None
    return recom_milktea


def main():
    vistor = 0
    vip_info_dict = {}
    sold_log_list = []
    shopping_car = {}
    vip_milktea_list = []

    while vistor < 5:
        print('今天的第{}位顾客，欢迎光临小象奶茶馆！\n小象奶茶馆售卖宇宙无敌奶茶，奶茶虽好，可不要贪杯哦！'.format(
            vistor + 1))

        chose_milktea(shopping_car, vip_milktea_list)
        vip_no, vip = vip_check(vip_info_dict)
        print_buy_info(shopping_car, vip)
        shopping_log(shopping_car, sold_log_list, vip_no)
        vistor += 1

    print('今日已闭店，欢迎明天光临！')
    print('VIP信息：{}'.format(vip_info_dict))
    print('今日销售记录：{}'.format(sold_log_list))


if __name__ == '__main__':
    main()
