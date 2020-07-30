import itertools

aa = itertools.combinations([1,2,3,4,5],4)
list1 = list(aa)
print(aa)
print(list1)
print(len(list1))

bb = list(itertools.product('0123456789',repeat=3))
print(bb)
print(len(bb))

for i in itertools.chain([1,2,3],[4,5,6]):
    print(i)
for j in list(zip(['a','b','c'],[1,2,3])):
    print(j)

# 装饰器
# def funA(fn):
#     # 定义一个嵌套函数
#     def say(arc):
#         print("Python教程:",arc)
#     return say
#
# @funA
# def funB(arc):
#     print(funB())
# # 传参调用
# funB("http://c.biancheng.net/python")


# 1 windows/linux下执行系统命令/调用应用程序
# import os
# import subprocess
# os.chdir(os.path.dirname(os.getcwd()))
# print(os.getcwd())
# print(os.path.dirname(os.getcwd()))

# path = '/Download'
# # 查看当前工作目录
# retval = os.getcwd()
# print("当前工作目录为 %s" % retval)
# # 切换工作目录
# os.chdir(path)
# # print(os.chdir(path))
# # 查看切换后的工作目录
# retval = os.getcwd()
# print("目录修改成功 %s" % retval)

# p = os.popen("ping baidu.com")
# p2 = os.popen("D:\\tools\ipmtool.exe -h 190.67.87.445 -u cmmcc -p huawei123 changepowerstate 0")
# print(p.read())
# subprocess 模块可以命令操作系统打开另外一个子进程，这类功能类似于os模块下的os.system()函数
# pp = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE)
# print(pp.stdout.read().decode('gbk'))


# 2.requests进行web服务接口调用
import json
import requests

"""
response = requests.post("http://www.baidu.com/login", data={'user': 'admin'})
response.json()
token = response.cookies['token']
response = requests.get("http://www.baidu.com/get", headers={"token": token})
if response.status_code == '200':
    print(response.json())
else:
    print('get failed')
response = requests.post("http://www.baidu.com/set", data={'operation_key': 'on'},
                         headers={"token": token})
if response.status_code == '200':
    print('successfully')
"""

# 3.ssh远程连接

"""
import paramiko
ssh_clinet = paramiko.SSHClient()
# 如果之前没有；连接过的ip, 会自动选择yes
ssh_clinet.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh_clinet.connect(hostname='192.168.43.234', port=22, username='zhang', password='123456')
# 执行命令
_, stdout, _ = ssh_clinet.exec_command('users')
# 查看执行结果（得到远程主机的输出）
print(stdout.read())
_, stdout, _ = ssh_clinet.exec_command('python3 test.py')
print(stdout.read())
# 关闭连接
ssh_clinet.close()
# 建立与远程主机的通道
trans = paramiko.Transport(("192.168.43.234", 22))
# 验证用户名和密码是否正确
trans.connect(username='zhang', password='123456')
# 创建sftp客户端
sftp=paramiko.SFTPClient.from_transport(trans)
# 从远程主机下载
# sftp.get('/home/zhang/git_test.py', 'git_test.py')
# 从本地上传
sftp.put('zhang.txt', '/home/zhang/zhang.txt')
print(sftp.listdir(path='/home/zhang/'))
"""


# 4.操作数据库
# import pymysql
# conn = pymysql.connect(host='localhost', user='root', password='123456',
#                        cursorclass=pymysql.cursors.DictCursor
#                        )
# cur = conn.cursor()
# cur.execute('show databases;')
# databases = cur.fetchall()
# # print(databases)
# all_databases = {}
# for data in databases:
#     database = data['Database']
#     # print(database)
#     # database = res[0][0]
#     print("库%s的数据:" % database)
#     cur.execute('use %s;' % database)
#     cur.execute('show tables;')
#     tables = cur.fetchall()
#     # print(res)
#     database_tables = {}
#     for table in tables:
#         table_name = table["Tables_in_%s" % database]
#         print("表%s的数据:" % table_name)
#         # table_name = table[0]
#         try:
#             cur.execute('select * from %s;' % table_name)
#             result = cur.fetchall()
#         except:
#             result = []
#         for row in result:
#             for key, value in row.items():
#                 if (type(value) is not str) and (type(value) is not int):
#                     row[key] = str(value)
#         if not result:
#             result = []
#         try:
#             print(result)
#             database_tables.update({table_name: result})
#         except:
#             database_tables.update({table_name:"数据读取异常"})
#     all_databases.update({database: database_tables})
# with open("localhost_mysql.json", 'w', encoding='utf8') as f:
#     f.write(json.dumps(all_databases))


