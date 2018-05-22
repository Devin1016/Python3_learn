import re


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

    def check_id(self, user_id):
        res = False
        rs = re.match(r'1[3578]\d{9}$', user_id)
        if rs:
            res = True
        return res


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

    def item_id_check(self, item_id):
        res = False
        if item_id in ['1', '2', '3']:
            res = True
        return res
