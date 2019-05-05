# ecoding:UTF-8
import MyCtpApi, sys, os, time, json
from mxh_work import wechat_main

reload(sys)
sys.setdefaultencoding('utf8')
from mysql_template import SqlHelper
from phObject import *


class mxhMysql():
    def __init__(self):

        self.trader = SqlHelper('localhost', 3306, 'traders', 'root', '123456')
        # self.trader = SqlHelper('106.75.103.134',3306,'Zqbxzxh1','root','lottery')
        self.mainAccountList1=[]
    def insert(self,*args):
        print('inset data into mysql')
        # sql = 'insert into accounts(userID,password,brokerID,company,operator,tdaddress) value(%s,%s,%s,%s,%s,%s)'
        sql = 'insert into accounts(userID,password,brokerID,company,operator,tdaddress,mdAddress,mainFlag,strike,accountID,subscribes,mysqlChilds,mysqlFather) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        sql_res = args
        print(sql_res)
        count = self.trader.update(sql, sql_res)
        print(count)
        return True
    def select(self):
        sql = 'select * from accounts where userID="118336"'
        res = self.trader.fetchall(sql)
        return res
    def saveAccount(self):
        pass
    def deleteAccount(self,userid):
        sql = 'DELETE FROM accounts WHERE userID = %s'
        userid =[userid]
        res = self.trader.update(sql,userid)
        return res
    #跟新登陆日志：
    def updateLog(self,userAccount,ip,time):
        sql='select userID,count(*) from AccountLog where userID = %s group by userID'
        args = [userAccount]
        res = self.trader.fetchall(sql,args)
        print(type(res),res)
        if res:
            if int(res[0][1]) > 10:
                print('达到最大限制')
                sql = 'select userID,loginTime from AccountLog where userID = %s order by loginTime asc '
                res = self.trader.fetchone(sql, args)
                print(res)
                res1 = self.trader.update('delete from AccountLog where loginTime = %s',[res[1]])
                print('是否删除 ',res1)
            print('没有达到最大日志限制')
            count = self.trader.update("insert into AccountLog(userID,IP,loginTime) value(%s,%s,%s)",[userAccount,ip,time])
        else:
            print('第一次添加数据')
            count = self.trader.update("insert into AccountLog(userID,IP,loginTime) value(%s,%s,%s)",[userAccount,ip,time])
        return count
    #记录交易订单
    def transactionRecord(self,data):
        per_data = []
        for i in data:
            per_data.append(data[i])
        # per_data = ['\x00','9999caf', '118336', '10:51:5'
        #                                         '2','0','9999',3539.0,'9999118316',1, '      125561','9999','jd1905', 'DCE', 1,'1', '20190412','9999', '1', '       32948','       65293', '20190412', '',50046,'1',151091,'118336', 'jd1905','0','\x00','\x00']
        #数字类型可以保存在字符串类型的数据库中
        # per_data = [str(i) for i in per_data]
        sum_s ='%s,'*29
        sql = 'insert into TransactionRecord value '+'('+sum_s+'%s)'
        print('sql is ',sql)
        count = self.trader.update(sql,per_data)
        return count
    def getSubscribes(self):
        sql = 'select * from subscribes'
        res = self.trader.fetchall(sql)
        return res
    def subscribesApi(self,subuserID,mainuserID):

        for i in self.mainAccountList1:
            print(i.userID,i.subscribes)
            if i.userID ==mainuserID:
                print('start subscribe',i.userID)
                if subuserID not in i.subscribes:
                    sql = 'select subscribes from accounts where userID = %s'
                    userid = [i.userID]
                    res = self.trader.fetchall(sql,userid)
                    res = res[0][0].split(' ')
                    print('res is ',res)
                    s_list =[]
                    if res:
                        for each in res:
                            s_list.append(each)
                    s_list.append(subuserID)
                    print('s_list is ',s_list)
                    s_listToStr = ' '.join(s_list)
                    sql1 = 'update accounts set subscribes=%s where userID = %s'
                    userid1 = [s_listToStr,i.userID]
                    res1 = self.trader.update(sql1,userid1)


                    return res1

                else:
                    print('have subscript %s'% i.userID)

    def unsubscribesApi(self, subuserID, mainuserID):

        for i in self.mainAccountList1:
            print(i.userID, i.subscribes)
            if i.userID == mainuserID:
                print('start unsubscribe', i.userID)
                if subuserID  in i.subscribes:
                    sql = 'select subscribes from accounts where userID = %s'
                    userid = [i.userID]
                    res = self.trader.fetchall(sql, userid)
                    print('res is ',res)
                    res = res[0][0].split(' ')
                    print('res ',res)
                    s_list = []
                    if res:
                        for each in res:
                            if each ==subuserID:
                                continue
                            s_list.append(each)
                    print('s_list is ', s_list)
                    s_listToStr = ' '.join(s_list)
                    sql1 = 'update accounts set subscribes=%s where userID = %s'
                    userid1 = [s_listToStr, i.userID]
                    res1 = self.trader.update(sql1, userid1)

                    return res1

                else:
                    print('have unsubscript %s' % i.userID)

    def getAccount(self):
        sql ='select * from accounts'
        res = self.trader.fetchall(sql)

        for i in res:
            account_one =phAccount()
            #数据库中保存的是字符串
            if i[0]:
                account_one.subscribes=i[0].split(' ')
            if i[1]:
                account_one.mysqlFather=i[1].split(' ')
            if i[2]:
                account_one.mysqlChilds=i[2].split(' ')

            if i[4]:
                account_one.strike =i[4]
            else:
                account_one.strike=3
            #永远使用的是主账户
            if i[5]:
                account_one.mainFlag = True
            else:
                account_one.mainFlag = True
            if i[6]:
                account_one.mdAddress=i[6]
            if i[7]:
                account_one.tdAddress=i[7]
            if i[8]:
                account_one.operator=i[8]
            if i[9]:
                account_one.company=i[9]
            if i[10]:
                account_one.brokerID = i[10]
            if i[11]:
                account_one.password = i[11]
            if i[12]:
                account_one.userID = i[12]

            # if i[3]:
            #     account_one.accountID =i[3]
            # else:
            #     account_one.accountID=".".join((i[12],i[10]))
            self.mainAccountList1.append(account_one)
        return self.mainAccountList1







if __name__=="__main__":
    sqlObj = mxhMysql()
    mainAccountList = sqlObj.getAccount()
    # #传入的序号必须是字符串，不能是数字
    one = sqlObj.subscribesApi('1','118336')
    print(one)

    # res = sqlObj.transactionRecord()
    # print(res)

    # res = sqlObj.updateLog('1','aaaaaa','dddddd')
    # print(res)
    # res = sqlObj.deleteAccount('1356')
    # print(res)


    # con = sqlObj.insert(1,2,'3','sdf','df','dkfs','dkfksd',True,3,'sssss','[1,2,3]',"[2,3,4]","[4,5,6]")
    # con = sqlObj.insert(u'sdf', u'sdfsdf', u'8016', u'\u5317\u4eac\u9996\u521b', u'\u7535\u4fe1', u'tcp://101.230.15.17:41205', '', True, 3, '.', '', '', '')
    #
    # print(con)
    # # res =sqlObj.select()
    # # print(res)

    # res = sqlObj.getAccount()
    # for i in res:
    #     print(i.userID,i.password,i.brokerID,i.company,i.operator,i.tdAddress,i.mdAddress,i.mainFlag,i.accountID,i.subscribes,i.mysqlChilds,i.mysqlFather)

    # res = sqlObj.getSubscribes()
    # mainAccountList = sqlObj.getAccount()
    # logintime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    # print(res)
    # for i in mainAccountList:
    #     for j in res:
    #         if j[0] in i.subscribes:
    #             i.subscribes.append(j)
    # for i in mainAccountList:
    #     if i.subscribes:
    #         print(i.subscribes)
    #         for i in i.subscribes:
    #             if type(i) == tuple or type(i) == list:
    #                 url = 'https://wechat.17aitec.xyz/api/trade/temmsg'
    #
    #                 headers = {
    #                     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    #                 }
    #
    #                 post_data = {
    #                      'token': i[1],
    #                     'channel_id': i[0],
    #                     'keyword1': '棕榈油1709(P1709)',
    #                     'keyword2': '5203',
    #                     'keyword3': '卖出/开仓',
    #                     'keyword4': '1',
    #                     'keyword5': logintime,
    #                 }
    #                 con = wechat_main.wechatInterface(url, post_data).run()
    #                 print(con)
    #             else:
    #                 print('meimei',i)
