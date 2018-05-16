# 三个空货架
pm_rack = []
zc_rack = []
xc_rack = []

# 摆货，泡面
pm_list = ['酸菜', '牛肉', '酸辣粉', '拉面']
pm_rack_num = 3

while len(pm_rack) < pm_rack_num:
    pm_index = len(pm_rack) % len(pm_list)
    pm_rack.append(pm_list[pm_index])

# 摆货，榨菜
zc_list = ['老干妈', '乌江']
zc_rack_num = 3

while len(zc_rack) < zc_rack_num:
    zc_index = len(zc_rack) % len(zc_list)
    zc_rack.append(zc_list[zc_index])

# 摆货，香肠
xc_list = ['王中王', '蒜肠', '淀粉肠']
xc_rack_num = 3

while len(xc_rack) < xc_rack_num:
    xc_index = len(xc_rack) % len(xc_list)
    xc_rack.append(xc_list[xc_index])

buy_car = []

while True:
    if len(pm_rack) == 0 and len(pm_rack) == 0 and len(pm_rack) == 0:
        print('所有商品已售罄！')
        break
    else:
        goods_num = input('---本店售卖商品：1）泡面，2）榨菜，3）香肠。---\n请输入想要购买的商品编号：')
        if int(goods_num) == 1:
            if len(pm_rack) > 0:
                buy_car.append(pm_rack[len(pm_rack) - 1])
                pm_rack.pop()
            else:
                print('非常抱歉！泡面已售完.')
        elif int(goods_num) == 2:
            if len(zc_rack) > 0:
                buy_car.append(zc_rack[len(zc_rack) - 1])
                zc_rack.pop()
            else:
                print('非常抱歉！榨菜已售完.')
        elif int(goods_num) == 3:
            if len(xc_rack) > 0:
                buy_car.append(xc_rack[len(xc_rack) - 1])
                xc_rack.pop()
            else:
                print('非常抱歉！香肠已售完.')
        else:
            print('没有你想要购买的商品，请输入在售商品')
            continue

    if len(buy_car) > 0:
        print('你购物商品如下：', buy_car)
        if_buy = input('是否继续购物？（y/n）')
        if if_buy == 'n':
            break

print('欢迎下次光临！')
