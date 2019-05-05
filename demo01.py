# encoding:UTF-8
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import shelve

# filename = r"G:\main\broker.ph"
# db = shelve.open(filename)
# print db['brokerDict']
# brokerDict = db['brokerDict']
# db.close()
#
# for k, v in brokerDict.items():
#     # print
#     # print u"********期货公司 Front Address********"
#     # print u"BrokerID:",k
#     # print u"Name:",v['name']
#     # print k
#     # print('______________')
#     # print(v)
#     servers = v['Servers']
#     sum = 0
#     for i, j in servers.items():
#         #     print
#         print i
#         print('__________')
#         print(j)
#
#         sum += len(j['trading']) + len(j['marketData'])
#     if sum == 0:
#         print u"BrokerID:", k

filename = r"G:\main\accounts.ph"
db = shelve.open(filename)
print db['mainAccountList']





