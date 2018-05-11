#!/usr/bin/python
# _*_ coding:utf-8 _*_
# __Author__ = songxy
# date : 2018/2/28

import xml.etree.cElementTree as ET

tree = ET.parse('12-dayxml')
root = tree.getroot()
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.attrib)
        print(i.tag,i.text)
