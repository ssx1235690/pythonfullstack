# -*- coding: utf-8 -*-
# @Time    :  2019/9/30
# @Author  :  user01
# @Email   : ......998@qq.com
# @File    : 3.argparse


import argparse



# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=min,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))

# parser = argparse.ArgumentParser()




####################   prog   ==   Program  name   默认使用 sys.args[0]

# parser = argparse.ArgumentParser(prog='myprogram')
# parser.add_argument('--foo', help='foo help')


# usage: myprogram [-h]
# usage: 3.argparse.py [-h] [--foo FOO]


####################  usage

# parser = argparse.ArgumentParser(prog='learn  argparser', usage='%(prog)s [options]')



'''
usage: learn  argparser [options]

optional arguments:
  -h, --help  show this help message and exit
  '''

################# description   epilog
# parser = argparse.ArgumentParser(description='A foo that bars', epilog="And that's how you'd foo a bar")


# parser.print_help()
'''
usage: 3.argparse.py [-h]

A foo that bars

optional arguments:
  -h, --help  show this help message and exit

And that's how you'd foo a bar
'''


##########################  prefix_chars

# parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
# parser.add_argument('+f')
# parser.add_argument('++bar')
# ll = parser.parse_args('+f X ++bar Y'.split())
# print(ll.f,ll.bar)


##############################  method to add args

# name or flags    位置参数不可省略    选项参数可以省略

# parser1 = argparse.ArgumentParser()
# # parser.add_argument('-f', '--foo')
# parser1.add_argument('-f','--foo')
# parser1.add_argument('bar')
# ll = parser1.parse_args([ 'barxxxx'])
#
# print(ll.bar)
'''
positional arguments:
  bar

optional arguments:
  -h, --help         show this help message and exit
  -f FOO, --foo FOO
'''


# ############## action   行为操作

# 储存为常量   store_cons

# parser = argparse.ArgumentParser()
#
# parser.add_argument('--foo', action='store_const', const=42)
#
# print(parser.parse_args(['--foo']))
# Namespace(foo=42)


# store_true   store_false

#
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', action='store_true')
# parser.add_argument('--bar', action='store_false')
# parser.add_argument('--baz', action='store_false')
# print(parser.parse_args('--foo --bar'.split()))
#
# Namespace(bar=False, baz=True, foo=True)


# count
# parser = argparse.ArgumentParser()
# parser.add_argument('--verbose', '-v', action='count')
# print(parser.parse_args(['-vvv']))
# Namespace(verbose=3)

# narg  引用参数个数
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', nargs=2)
# parser.add_argument('bar', nargs=1)
# parser.parse_args('c --foo a b'.split())
#
# Namespace(bar=['c'], foo=['a', 'b'])


# choices
# parser = argparse.ArgumentParser(prog='game.py')
# parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
# parser.parse_args(['rock'])
# # Namespace(move='rock')
# print(parser.parse_args(['fire']))
# usage: game.py [-h] {rock,paper,scissors}
# game.py: error: argument move: invalid choice: 'fire' (choose from 'rock',
# 'paper', 'scissors'


#  dest 自己给传入参数取名字

# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', dest='bar')
# parser.parse_args('--foo XXX'.split())
# Namespace(bar='XXX')




### 使用

parser = argparse.ArgumentParser()

parser.add_argument('-f','--foo')

args = parser.parse_args()
print(args.foo)

