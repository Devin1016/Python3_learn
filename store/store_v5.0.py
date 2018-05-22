import datetime
import csv


class WareHouseManageSys:
    def __init__(self):
        self.item_detail = {
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

    def get_items_list(self, item_type):
        pm_list = ['酸菜', '牛肉', '酸辣粉', '拉面']
        zc_list = ['老干妈', '乌江']
        xc_list = ['王中王', '蒜肠', '淀粉肠']
        if item_type == 'pm':
            items_list = pm_list
        elif item_type == 'zc':
            items_list = zc_list
        elif item_type == 'xc':
            items_list = xc_list
        return items_list

    def add_updata_item_info(self, **kwargs):
        for item, price in kwargs.items():
            self.item_detail[item] = price


class RackManageSys:
    def check_add_rack(self, rack, item_type, item_counts, warehouse_manage):
        if len(rack) == 0:
            print('正在更新货架，请稍等！')
            item_list = warehouse_manage.get_items_list(item_type)
            while len(rack) < item_counts:
                rack_index = len(rack) % len(item_list)
                rack.append(item_list[rack_index])
            print('商品已上架')


class LogManagerSys:
    def __init__(self):
        self.user_buy_log_list = []
        self.buy_log_list = []

    def get_log_time(self, format='%Y%m%d'):
        log_time = datetime.datetime.now().strftime(format)
        return log_time

    def write_log_append_csv(self, header, data, file_path='log/'):
        log_time = self.get_log_time()
        file_name = file_path + 'buy_log_' + log_time + '.csv'
        with open(file_name, 'a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, header)
            writer.writerows(data)

    def user_buy_log_manager_sys(self, user_id, money, *buy_car):
        items_str = ''
        for item in buy_car:
            if items_str == '':
                items_str = item
            else:
                items_str += '|' + item

        header = ['user_id', 'money', 'items']
        buy_log_dict = {'user_id': user_id, 'money': money, 'items': items_str}
        log_dict = {'user_id': user_id, 'money': money, 'items': buy_car}
        self.user_buy_log_list.append(buy_log_dict)
        self.buy_log_list.append(log_dict)
        self.write_log_append_csv(header, self.user_buy_log_list)


class UserManageSys:
    def __init__(self):
        self.user_id_set = set()

    def add_new_user(self, user_id):
        if user_id not in self.user_id_set:
            self.user_id_set.add(user_id)

    def check_vip(self, user_id):
        if user_id in self.user_id_set:
            if_vip = True
        else:
            if_vip = False
        return if_vip


class BuyCar:
    def __init__(self, user_id, user_manage, warehouse_manage):
        self.buy_car = []
        self.user_id = user_id
        self.if_vip = user_manage.check_vip(user_id)
        self.item_detail = warehouse_manage.item_detail

    def add_item_2_car(self, pm_rack, zc_rack, xc_rack, item_id):
        if int(item_id) == 1:
            self.buy_car.append(pm_rack[len(pm_rack) - 1])
            pm_rack.pop()
        elif int(item_id) == 2:
            self.buy_car.append(zc_rack[len(zc_rack) - 1])
            zc_rack.pop()
        elif int(item_id) == 3:
            self.buy_car.append(xc_rack[len(xc_rack) - 1])
            xc_rack.pop()
        else:
            print('没有你想要购买的商品，请输入在售商品')

    def account(self):
        total_money = 0
        for item in self.buy_car:
            total_money += self.item_detail.get(item, 0)
        if self.if_vip:
            total_money *= 0.9
        return total_money


class RecommendSys:
    def recommend(self):
        print('推荐商品')


class BaseItemRecommendSys(RecommendSys):
    def recommend(self, user_id, log_manage):
        user_item_set = set()
        other_user_item_dict = {}
        recommend_list = []
        for log in log_manage.buy_log_list:
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


class UnstaffedStore:
    def __init__(self):
        self.warehouse_manage = WareHouseManageSys()
        self.rack_manage = RackManageSys()
        self.log_manage = LogManagerSys()
        self.user_manage = UserManageSys()
        self.recommend = BaseItemRecommendSys()

    def shopping_hall(self):
        pm_rack = []
        zc_rack = []
        xc_rack = []
        pm_rack_counts = 3
        zc_rack_counts = 3
        xc_rack_counts = 3

        while True:
            print('欢迎光临！')

            while True:
                user_id = input('请输入手机号作为会员号使用：')
                if user_id != '':
                    self.user_manage.add_new_user(user_id)
                    break
                else:
                    print('手机号不能为空！')

            buy_car = BuyCar(user_id, self.user_manage, self.warehouse_manage)

            while True:
                self.rack_manage.check_add_rack(pm_rack, 'pm', pm_rack_counts, self.warehouse_manage)
                self.rack_manage.check_add_rack(zc_rack, 'zc', zc_rack_counts, self.warehouse_manage)
                self.rack_manage.check_add_rack(xc_rack, 'xc', xc_rack_counts, self.warehouse_manage)

                item_id = input('---本店售卖商品：1）泡面，2）榨菜，3）香肠。---\n请输入想要购买的商品编号：')
                if item_id in ['1', '2', '3']:
                    buy_car.add_item_2_car(pm_rack, zc_rack, xc_rack, item_id)
                else:
                    print('你所选择的商品不存在。')
                if_buy = input('是否继续购物？（y/n）')
                if if_buy == 'n':
                    if len(buy_car.buy_car) > 0:
                        total_money = buy_car.account()
                        print('你购物商品如下：', buy_car.buy_car)
                        print('你本次消费金额：{}元'.format(total_money))
                        self.log_manage.user_buy_log_manager_sys(user_id, total_money, *buy_car.buy_car)
                        recommend_items_list = self.recommend.recommend(user_id, self.log_manage)
                        if recommend_items_list is not None:
                            print('买了该商品的其他用户，还买了:{}'.format(recommend_items_list))
                        buy_car = []
                        print('欢迎下次光临！')
                    else:
                        print('你未购买任何商品。')
                    break
                print('欢迎下次光临！')


def main():
    usstaffed_store = UnstaffedStore()
    usstaffed_store.shopping_hall()


if __name__ == '__main__':
    main()
