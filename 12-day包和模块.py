#!/usr/bin/python
# -*- coding: utf-8 -*-
# __Author__ = songxy
# date : 2018/2/5

#模块的引入方式有以下几种
# 1 import  语句
# 2 from  module  import 方法   语句
# 3 from  module  import *  语句
# 无论1还是2，首先通过sys.path找到test.py,然后执行test脚本（全部执行），区别是1会将test这个变量名加载到名字空间，而2只会将add这个变量名加载进来。　
# # import sys
# # print(sys.path)
# from sys import path
# print(path)

#######################包的概念#######################################
# 包(package)
# 如果不同的人编写的模块名相同怎么办？为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。
# 举个例子，一个abc.py的文件就是一个名字叫abc的模块，一个xyz.py的文件就是一个名字叫xyz的模块。
# 现在，假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名：
# 引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，view.py模块的名字就变成了hello_django.app01.views，类似的，manage.py的模块名则是hello_django.manage。
# 请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录(文件夹)，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是对应包的名字。
# 调用包就是执行包下的__init__.py文件

# from song.insong import song
# song()

#['C:\\Users\\ronglian\\pythonfullstack', 'C:\\Users\\ronglian\\pythonfullstack',
#  'C:\\Users\\ronglian\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip',
# 'C:\\Users\\ronglian\\AppData\\Local\\Programs\\Python\\Python36\\DLLs',
# 'C:\\Users\\ronglian\\AppData\\Local\\Programs\\Python\\Python36\\lib', '
# C:\\Users\\ronglian\\AppData\\Local\\Programs\\Python\\Python36',
# 'C:\\Users\\ronglian\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages', '
# C:\\Program Files\\JetBrains\\PyCharm 2017.3\\helpers\\pycharm_matplotlib_backend']
# pycharm 这类的集成工具，会帮你自动添加很多很多路径 就类似我们在linux运维工作中的 $PATH
# 在nod1里import  hello是找不到的，有同学说可以找到呀，那是因为你的pycharm为你把myapp这一层路径加入到了sys.path里面，
# 所以可以找到，然而程序一旦在命令行运行，则报错。有同学问那怎么办？简单啊，自己把这个路径加进去不就OK啦：
import sys
print(sys.path)
print(__file__)
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
######利用 __file__ ,os.path.dirname 和 sys.path.append 来添加自己的模块路径#####################################
print(__name__)
# 如果我们是直接执行某个.py文件的时候，该文件中那么”__name__ == '__main__'“是True,
# 但是我们如果从另外一个.py文件通过import导入该文件的时候，这时__name__的值就是我们这个py文件的名字而不是__main__。
#
# 这个功能还有一个用处：调试代码的时候，在”if __name__ == '__main__'
# “中加入一些我们的调试代码，我们可以让外部模块调用的时候不执行我们的调试代码，但是如果我们想排查问题的时候，
# 直接执行该模块文件，调试代码能够正常运行！s

