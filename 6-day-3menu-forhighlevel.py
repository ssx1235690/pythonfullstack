#!/usr/bin/python
# -*- coding: gbk -*-
# __Author__ = songxy
# date : 2017/12/10
import sys
print(sys.getdefaultencoding())
zone = {
     'sd' : {
         'qd' : ['�ķ�','�Ƶ�','��ɽ','���','����'],
         'jn' : ['����','����','����','����','����'],
         'yt' : ['����','��ɽ','Ĳƽ','����','��Զ']
     },
     'js' : {
         'sz' : ['����','���','ƽ��','����','��ɽ'],
         'nj' : ['����','�ػ�','�ֿ�','��ϼ','����'],
         'wx' : ['�簲','�ϳ�','����','��ɽ','����']
     },
     'zj' : {
         'hz' : ['����','����','�³�','�ϳ�','����'],
         'nb' : ['����','����','����','��','��Ҧ'],
         'wz' : ['¹��','����','����','��','����']
     },
     'ah' : {
         'hf' : ['��ɽ','®��','����','����','��վ'],
         'wh' : ['����','𯽭','��Ϊ','��ɽ','����'],
         'bb' : ['��ɽ','���Ӻ�','����','��Զ','����']
     },
     'gz' : {
         'sz' : ['�޺�','����','��ɽ','����','����'],
         'gz' : ['���','�麣','Խ��','����','����'],
         'dg' : ['ݸ��','����','����','��','����']
     }
 }
current_menu = zone
parent_menu = []
while True:
    for key1 in current_menu:
        print(key1)
    choice = input('give me your province choice��\\b �����ϲ� \q �˳�').strip()
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