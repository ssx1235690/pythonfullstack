# -*- coding: utf-8 -*-
# @Time    : 2019/3/30 22:09
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : genetors.py


class Eg2(object):
    """
    可迭代对象：从python内部获取迭代器
    """

    def __init__(self, text):
        # type：list
        self.sub_text = text.split(" ")

    def __iter__(self):
        return Eg2Iterator(self.sub_text)


class Eg2Iterator:
    """
    迭代器：对已经划分完毕的字符串进行迭代
    """

    def __init__(self, sub_text):
        self.sub_text = sub_text
        self.index = 0

    def __next__(self):
        try:
            subtext = self.sub_text[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return subtext

    def __iter__(self):
        return self


if "__main__" == __name__:

    o2 = Eg2("hello, the wonderful new world!")
    for i in o2:
        print(i, end=" | ")



b = (i for i in range(10))
a = [i for i in range(10)]
c = {i for i in range(10)}
print(a,b,c)
