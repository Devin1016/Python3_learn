import datetime
import csv

g_user_id_set = set()
g_user_buy_log_list = []


class LogManager:
    def get_log_time(self, format='%Y%m%d'):
        log_time = datetime.datetime.now().strftime(format)
        return log_time

    def write_log_append_csv(self, header, data, file_path='log/'):
        log_time = self.get_log_time()
        file_name = file_path + 'buy_log_' + log_time + '.csv'
        with open(file_name, 'a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, header)
            writer.writerows(data)


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


def buy_car_account(buy_car, user_id):
    item_detail = {
        '酸菜': 5,
        '牛肉': 4,
        '酸辣粉': 6,
        '拉面': 7,
        '老干妈': 10,
        '乌江': 2,
        '王中王': 2,
        '蒜肠': 12,
        '淀粉肠': 1
    }
    total_money = 0
    for item in buy_car:
        total_money += item_detail.get(item, 0)
    if user_manager_sys(user_id):
        total_money *= 0.9
    return total_money


def user_manager_sys(user_id):
    if_vip = False
    if user_id in g_user_id_set:
        if_vip = True
    else:
        g_user_id_set.add(user_id)
    return if_vip


def user_buy_log_manager_sys(user_id, *buy_car):
    items_str = ''
    for item in buy_car:
        if items_str == '':
            items_str = item
        else:
            items_str += '|' + item

    header = ['user_id', 'money', 'items']
    buy_log_dict = {'user_id': user_id, 'money': buy_car_account(buy_car, user_id), 'items': items_str}
    g_user_buy_log_list.append(buy_log_dict)
    log = LogManager()
    log.write_log_append_csv(header, g_user_buy_log_list)


def recommend_sys(user_id):
    if user_id in g_user_id_set:
        user_item_set = set()
        other_user_item_dict = {}
        recommend_list = []
        for log in g_user_buy_log_list:
            user_id_key = log['user_id']
            items_value = log['items']
            if user_id_key == user_id:
                user_item_set.update(items_value)
            else:
                items_set = other_user_item_dict.get(user_id_key)
                if items_set is None:
                    other_user_item_dict[user_id_key] = set(items_value)
                else:
                    items_set.update(items_value)
                    other_user_item_dict[user_id_key] = items_set
            for value_set in other_user_item_dict.values():
                inner_set = value_set & user_item_set
                length = len(inner_set)
                if length > 0 and length < len(value_set):
                    diff_set = value_set - user_item_set
                    recommend_list.append({
                        'common_num': length,
                        'diff_items': diff_set
                    })
            if len(recommend_list) > 0:
                recommend_list.sort(
                    key=lambda items: items['common_num'], reverse=True)
                recommend_set = recommend_list[0]['diff_items']
                return list(recommend_set)


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
                while True:
                    user_id = input('请输入手机号作为会员号使用：')
                    if user_id != '':
                        break
                    else:
                        print('手机号不能为空！')

                total_money = buy_car_account(buy_car, user_id)

                print('你购物商品如下：', buy_car)
                print('你本次消费金额：{}元'.format(total_money))
                user_buy_log_manager_sys(user_id, *buy_car)
                recommend_items_list = recommend_sys(user_id)
                if recommend_items_list is not None:
                    print('买了该商品的其他用户，还买了:{}'.format(recommend_items_list))
                buy_car = []
                print('欢迎下次光临！')
            else:
                print('你未购买任何商品。')
        else:
            if_new_user = False
        print('欢迎下次光临！')


shopping_hall()
