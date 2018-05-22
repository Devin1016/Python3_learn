import datetime
import csv


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
