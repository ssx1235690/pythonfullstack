# -*- coding: utf-8 -*-
# @Time    :  2019/4/19 14:24
# @Author  : songxy
# @Email   : ......998@qq.com
# @File    : 1.ssh_test.py


import paramiko


hostname='192.168.163.131'
hostname='192.168.157.133'
passwd='1'
passwd='123456'
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname=hostname, port=22, username='root', password=passwd)

# 执行命令
stdin, stdout, stderr = ssh.exec_command('echo song lele && ls song lele')
# 获取命令结果
result = stdout.read()
print(result.decode())

# 关闭连接
ssh.close()





transport = paramiko.Transport((hostname, 22))
transport.connect(username='root', password=passwd)

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')

transport.close()
