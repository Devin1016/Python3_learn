from log import LogManagerSys
import datetime
import re


class DataAnalysisSys:
    def __init__(self):
        self.log_manage = LogManagerSys()

    def get_data(self, days=0, format_type='%Y%m%d'):
        today = datetime.datetime.today()
        timedelta = datetime.timedelta(days=days)
        target_date = today - timedelta
        return target_date.strftime(format_type)

    def user_report(self):
        ym = self.get_data(days=30, format_type='%Y%m')

        datas = self.log_manage.read_log_csv('user_info.csv')
        new_user_dict = {}
        for data in datas:
            dt = data[1]
            if re.match('{}'.format(ym), dt):
                user_num = new_user_dict.get(dt, 0) + 1
                new_user_dict[dt] = user_num

        m_new_user_count = 0

        for key, value in new_user_dict.items():
            m_new_user_count += value

        print('{}月每日新增用户数：\n{}'.format(ym, new_user_dict))
        print('{}月新增用户数：{}'.format(ym, m_new_user_count))

    def sale_report(self):
        ym = self.get_data(days=30, format_type='%Y%m')
        files = self.log_manage.list_dir_file('log/')
        sale_money_dict = {}
        sale_count_dict = {}
        for file_name in files:
            if re.match('buy_log_{}'.format(ym), file_name):
                file_path = 'log/' + file_name
                datas = self.log_manage.read_log_csv(file_path)
                money = 0
                count = 0
                for data in datas:
                    money += float(data[1])
                    items_list = data[2].split('|')
                    count += len(items_list)
                sale_count_dict[file_name[-12:-4]] = count
                sale_money_dict[file_name[-12:-4]] = money
        print('{}月每日销售额：{}'.format(ym, sale_money_dict))
        print('{}月每日销量：{}'.format(ym, sale_count_dict))


das = DataAnalysisSys()
das.user_report()
das.sale_report()
