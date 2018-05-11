#!/usr/bin/python
# _*_ coding:utf-8 _*_
# __Author__ = songxy
# date : 2018/1/28
#############要生成下列配置文件##########
'''
[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg

[topsecret.server.com]
Port = 50022
ForwardX11 = no
'''

import configparser
config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
    config.write(configfile)


##############config文件的增删改查##################
# config.remove_section('bitbucket.org')
config.read('example.ini')
print(config.sections())
print(config.defaults())
# ['bitbucket.org', 'topsecret.server.com']
# OrderedDict([('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes')])
print('bytebong.com' in config)# False

print(config['bitbucket.org']['User']) # hg

print(config['DEFAULT']['Compression']) #yes

print(config['topsecret.server.com']['ForwardX11'])  #no


for key in config['bitbucket.org']:
    print(key)


# user
# serveraliveinterval   默认块在打印别的块的时候也会跟着打印
# compression
# compressionlevel
# forwardx11


#---------------------------------------------删,改,增(config.write(open('i.cfg', "w")))


config.add_section('yuan')

config.remove_section('topsecret.server.com')
config.remove_option('bitbucket.org','user')

config.set('bitbucket.org','k1','11111')

config.write(open('i.cfg', "w"))