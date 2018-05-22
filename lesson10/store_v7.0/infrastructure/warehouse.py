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
