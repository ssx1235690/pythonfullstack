#!/usr/bin/python
# -*- coding : utf-8 -*-
# __Author__ = songxy
# date : 2017/12/5
import time
zone = {
     'sd' : {
         'qd' : ['四方','黄岛','崂山','李沧','城阳'],
         'jn' : ['历城','槐荫','高新','长青','章丘'],
         'yt' : ['龙口','莱山','牟平','蓬莱','招远']
     },
     'js' : {
         'sz' : ['沧浪','相城','平江','吴中','昆山'],
         'nj' : ['白下','秦淮','浦口','栖霞','江宁'],
         'wx' : ['崇安','南长','北塘','锡山','江阴']
     },
     'zj' : {
         'hz' : ['西湖','江干','下城','上城','滨江'],
         'nb' : ['海曙','江东','江北','镇海','余姚'],
         'wz' : ['鹿城','龙湾','乐清','瑞安','永嘉']
     },
     'ah' : {
         'hf' : ['蜀山','庐阳','包河','经开','新站'],
         'wh' : ['镜湖','鸠江','无为','三山','南陵'],
         'bb' : ['蚌山','龙子湖','淮上','怀远','固镇']
     },
     'gz' : {
         'sz' : ['罗湖','福田','南山','宝安','布吉'],
         'gz' : ['天河','珠海','越秀','白云','黄埔'],
         'dg' : ['莞城','长安','虎门','万江','大朗']
     }
 }
print(zone['js']['sz'][1])
while True:
    for key1 in zone:
        print(key1)
    choice1 = input('give me your province choice，\q 退出').strip()
    if choice1 == 'q':
        break
    if choice1 in zone:
        while True:
            for key2 in zone[choice1]:
                print(key2)
            choice2 = input('give me your city choice ,\q 返回上层菜单').strip()
            if choice2 == 'q':
                break
            if choice2 in zone[choice1]:
                while True:
                    for key3 in zone[choice1][choice2]:
                        print(key3)
                    choice3 = input('give me your town number,\q 返回上层菜单').strip()
                    if choice3 == 'q':
                        break
                    if choice3.isdigit():
                        choice3 = int(choice3) - 1
                        if choice3 > -1 and choice3 < 4:
                            print(zone[choice1][choice2][choice3])
                    else:
                        print('invalid input please bu careful!!!')
                        time.sleep(1)
            else:
                print('invalid input please bu careful!!!')
                time.sleep(1)
    else:
        print('invalid input please bu careful!!!')
        time.sleep(1)



'''
定义标志位是一种高大上的方法
q_flag = False
while not q_flag:

这样可以实现当你的输入错误的时候 走一个判断使 q_flag = True
直接返回上层


 '''