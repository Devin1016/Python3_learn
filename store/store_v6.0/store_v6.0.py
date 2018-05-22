from infrastructure.warehouse import WareHouseManageSys
from infrastructure.rack import RackManageSys
from infrastructure.log import LogManagerSys
from infrastructure.user import UserManageSys, BuyCar
from infrastructure.recommend import BaseItemRecommendSys


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
                if self.user_manage.check_id(user_id):
                    self.user_manage.add_new_user(user_id)
                    break
                else:
                    print('手机号不正确！')

            buy_car = BuyCar(user_id, self.user_manage, self.warehouse_manage)

            while True:
                self.rack_manage.check_add_rack(pm_rack, 'pm', pm_rack_counts, self.warehouse_manage)
                self.rack_manage.check_add_rack(zc_rack, 'zc', zc_rack_counts, self.warehouse_manage)
                self.rack_manage.check_add_rack(xc_rack, 'xc', xc_rack_counts, self.warehouse_manage)

                item_id = input('---本店售卖商品：1）泡面，2）榨菜，3）香肠。---\n请输入想要购买的商品编号：')
                if buy_car.item_id_check(item_id):
                    buy_car.add_item_2_car(pm_rack, zc_rack, xc_rack, item_id)
                else:
                    print('你所选择的商品不存在。')
                    continue
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
