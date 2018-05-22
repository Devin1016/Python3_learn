class RackManageSys:
    def check_add_rack(self, rack, item_type, item_counts, warehouse_manage):
        if len(rack) == 0:
            print('正在更新货架，请稍等！')
            item_list = warehouse_manage.get_items_list(item_type)
            while len(rack) < item_counts:
                rack_index = len(rack) % len(item_list)
                rack.append(item_list[rack_index])
            print('商品已上架')
