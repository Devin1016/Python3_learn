'''
冒泡排序
1、排序的总轮数 = 列表元素个数 - 1
2、每轮元素比较次数 = 列表元素个数 - 已排序号元素个数 - 1
'''

sort_list = [28, 32, 14, 12, 53, 42, 1, 99, 239, 123]


def bubble_sort(data_list):
    num = len(data_list)
    for i in range(num - 1):
        print('第{}轮:'.format(i + 1))
        for j in range(num - i - 1):
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
            print(data_list)


# bubble_sort(sort_list)
# print('________________________________')
# print(sort_list)


# 选择排序
def select_sort(data_list):
    num = len(data_list)
    for i in range(num - 1):
        print('第{}轮:'.format(i + 1))
        x = i
        for j in range(i + 1, num):
            if data_list[x] > data_list[j]:
                x = j
        if x != i:
            data_list[x], data_list[i] = data_list[i], data_list[x]
        print(data_list)


# select_sort(sort_list)
# print('________________________________')
# print(sort_list)


# 快速排序
def quick_sort(data_list, start, end):
    if start >= end:
        return
    low_index = start
    high_index = end
    basic_data = data_list[low_index]
    while low_index < high_index:
        # 模拟从右向左逐个元素与基准值比较，比基准值大，高位游标一直向左移动
        while low_index < high_index and data_list[high_index] >= basic_data:
            high_index -= 1
        if low_index != high_index:
            # 当高位游标指向的元素小于基准值，将高位游标指向的元素移动到低位游标指向位置
            data_list[low_index] = data_list[high_index]
            low_index += 1
        # 模拟从左向右逐个元素与基准值比较，比基准值小，低位游标一直向右移动
        while low_index < high_index and data_list[low_index] < basic_data:
            low_index += 1
        if low_index != high_index:
            # 当低位游标指向的元素大于基准值，将低位游标指向的元素移动到高位游标指向位置
            data_list[high_index] = data_list[low_index]
            high_index -= 1
    data_list[low_index] = basic_data
    quick_sort(data_list, start, low_index - 1)
    quick_sort(data_list, low_index + 1, end)


quick_sort(sort_list, 0, len(sort_list) - 1)
print('________________________________')
print(sort_list)


# 归并排序
def merge_sort(data_list):
    if len(data_list) > 1:
        mid_index = len(data_list) // 2
        left_list = merge_sort(data_list[:mid_index])
        right_list = merge_sort(data_list[mid_index:])

        l_index = 0
        r_index = 0
        merge_list = []

        while l_index < len(left_list) and r_index < len(right_list):
            if left_list[l_index] < right_list[r_index]:
                merge_list.append(left_list[l_index])
                l_index += 1
            else:
                merge_list.append(right_list[r_index])
                r_index += 1
        merge_list += left_list[l_index:]
        merge_list += right_list[r_index:]
    else:
        merge_list = data_list
    return merge_list


# sort_list = [28, 32, 14, 12, 53, 42]
# new_list = merge_sort(sort_list)
# print('________________________________')
# print(new_list)
