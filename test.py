# encoding:UTF-8
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import shelve
filename=r"F:\vnpyStudy\main\broker.ph"
db=shelve.open(filename)
brokerDict=db['brokerDict']
db.close()

for k,v in brokerDict.items():
    # print 
    # print u"********期货公司 Front Address********"
    # print u"BrokerID:",k
    # print u"Name:",v['name']
    servers=v['Servers']
    sum=0
    for i,j in servers.items():
    #     print
    #     print i
    #     print "======"
    #     print "trading"
    #     print "-------------"
    #     for t in j['trading']:
    #         print t
    #     print 
    #     print "MarkerData"
    #     print "-------------"
    #     for m in j['marketData']:
    #         print m
    # print "*************************************"
        sum+=len(j['trading'])+len(j['marketData'])
    if sum==0:
        print u"BrokerID:",k



    

