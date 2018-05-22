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
