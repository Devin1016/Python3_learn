def warehouse(item_type):
    pm_list = ['酸菜', '牛肉', '酸辣粉', '拉面']
    zc_list = ['老干妈', '乌江']
    xc_list = ['王中王', '蒜肠', '淀粉肠']
    if item_type == 'pm':
        res = pm_list
    elif item_type == 'zc':
        res = zc_list
    elif item_type == 'xc':
        res = xc_list
    return res


def check_add_rack(rack, item_type, item_counts):
    if len(rack) == 0:
        print('正在更新货架，请稍等！')
        item_list = warehouse(item_type)
        while len(rack) < item_counts:
            rack_index = len(rack) % len(item_list)
            rack.append(item_list[rack_index])
        print('商品已上架')


def buy_car_account(buy_car):
    item_detail = {'酸菜': 5, '牛肉': 4, '酸辣粉': 6, '拉面': 7, '老干妈': 10, '乌江': 2, '王中王': 2, '蒜肠': 12, '淀粉肠': 1}
    total_money = 0
    for item in buy_car:
        total_money += item_detail.get(item, 0)
    return total_money


def shopping_hall():
    pm_rack = []
    zc_rack = []
    xc_rack = []
    pm_rack_counts = 3
    zc_rack_counts = 3
    xc_rack_counts = 3
    buy_car = []
    if_new_user = True

    while True:
        check_add_rack(pm_rack, 'pm', pm_rack_counts)
        check_add_rack(zc_rack, 'zc', zc_rack_counts)
        check_add_rack(xc_rack, 'xc', xc_rack_counts)
        if if_new_user:
            print('欢迎光临！')

        item_id = input('---本店售卖商品：1）泡面，2）榨菜，3）香肠。---\n请输入想要购买的商品编号：')
        if int(item_id) == 1:
            buy_car.append(pm_rack[len(pm_rack) - 1])
            pm_rack.pop()
        elif int(item_id) == 2:
            buy_car.append(zc_rack[len(zc_rack) - 1])
            zc_rack.pop()
        elif int(item_id) == 3:
            buy_car.append(xc_rack[len(xc_rack) - 1])
            xc_rack.pop()
        else:
            print('没有你想要购买的商品，请输入在售商品')
            continue

        if_buy = input('是否继续购物？（y/n）')
        if if_buy == 'n':
            if len(buy_car) > 0:
                total_money = buy_car_account(buy_car)
                print('你购物商品如下：', buy_car)
                print('你本次消费金额：{}元'.format(total_money))
                buy_car = []
                print('欢迎下次光临！')
                break
            else:
                print('你未购买任何商品。')
        else:
            if_new_user = False


shopping_hall()
