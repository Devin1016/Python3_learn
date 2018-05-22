import itchat
import matplotlib.pyplot as plt


class Analysis:
    def wechat_user_gender_report(self):
        itchat.login()
        friends = itchat.get_friends()
        male_count = 0
        female_count = 0
        other_count = 0
        for friend in friends[1:]:
            gender = friend['Sex']
            if gender == 1:
                male_count += 1
            elif gender == 2:
                female_count += 1
            else:
                other_count += 1
        total = len(friends) - 1
        print('好友总数：{}'.format(total))
        print('男性好友数：{},占比：{:.2f}'.format(male_count, float(male_count / total)))
        print('女性好友数：{},占比：{:.2f}'.format(female_count, float(female_count / total)))
        print('未知性别数：{},占比：{:.2f}'.format(other_count, float(other_count / total)))

        datas = [male_count, female_count, other_count]
        labels = ['Male', 'Female', 'Other']
        self.get_pie(datas, labels)

    def wechat_user_location_report(self):
        itchat.login()
        friends = itchat.get_friends()
        province_dict = {}
        for friend in friends[1:]:
            province = friend['Province']
            if province == '':
                province = '未知'
            else:
                province_dict[province] = province_dict.get(province, 0) + 1
        print(province_dict)

        data_list = []
        for item in province_dict.items():
            data_list.append(item)
        data_list.sort(key=lambda item: item[1], reverse=True)
        top10_datas = data_list[:11]
        print(top10_datas)
        datas_list = []
        labels_list = []
        for data in top10_datas:
            datas_list.append(data[1])
            labels_list.append(data[0])

        self.get_bar(datas_list, labels_list)

    def get_pie(self, datas, labels):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.figure(figsize=(8, 6), dpi=80)
        plt.axes(aspect=1)
        plt.pie(datas, labels=labels, autopct='%.f2%%', shadow=False)
        plt.title('微信好友性别分析图')
        plt.show()

    def get_bar(self, datas, labels):
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.xlabel('Province')
        plt.ylabel('Counts')
        plt.xticks(range(len(datas)), labels)
        plt.bar(range(len(datas)), datas, color='rgb')
        plt.title('微信好友地域分布图')
        plt.show()


analysis = Analysis()
analysis.wechat_user_gender_report()
analysis.wechat_user_location_report()
