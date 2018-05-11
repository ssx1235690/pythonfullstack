#!/usr/bin/python
# -*- coding: gbk -*-
# __Author__ = songxy
# date : 2017/12/10
import sys
print(sys.getdefaultencoding())
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
current_menu = zone
parent_menu = []
while True:
    for key1 in current_menu:
        print(key1)
    choice = input('give me your province choice，\\b 返回上层 \q 退出').strip()
    if len(choice) == 0: continue
    if choice in current_menu:
        parent_menu.append(current_menu)
        current_menu = current_menu[choice]
    elif choice == 'q':
        if parent_menu == []:
            break
        continue
    elif choice == 'b':
        current_menu = parent_menu.pop()
    else:
        if not parent_menu == []:
            print('invalid input!!!!!')