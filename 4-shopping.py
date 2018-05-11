#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2017/12/3
menu ='''
salary = 5000
1. iphone6s 5500
2. mac book 9000
3. coffee 32
4. python book 80
5. bicycle 800
'''
salary = 5000
print(type(salary))
goods = ['','iphone6s','mac book','coffee','python book','bicycle']
price = ['','5500','9000','32','80','800']
print(menu)
flag = '0'
shopcar = []
while flag != 'quit':
    flag = input('give me your choice! ')
    if flag.isdigit():
        flag = int(flag)
        if flag > len(goods) - 1:
            print('没有这个商品----请您认真选择！！！！')
            continue
        if (salary - int(price[flag])) > 0:
            print('已加入%s,余额为%d'%(goods[flag],salary - int(price[flag])))
            salary = salary - int(price[flag])
            shopcar.append(flag)
        else:
            print('余额不足%d'%(salary - int(price[flag])))
    elif flag != 'quit':
        print('invalid input！！！')
else:
    print('您已购买一下产品')
    
    for i in shopcar:
        print('%s   %s'%(goods[i],price[i]))
    print('你的余额为%d\n 欢迎下次光临'%(salary))







