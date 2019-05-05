# coding=utf-8
from wechat import posts,gets
import time
import re


class wechatInterface():
    def __init__(self,url,post_data,headers = None):
        self.url =url
        self.post_data = post_data
        self.headers = headers

    def run(self):
        res = posts(url = self.url,data = self.post_data)
        return res
class FutureSetUp():
    def __init__(self):
        self.url = 'http://hq.sinajs.cn/list='
    def run(self,code):
        #将合约名的小写转换成大写
        word = re.findall('[^\d]+', code)[0].upper()
        print('非数字部分：',word)
        #查看数字部分的长度，如果3位，补全成四位，即开头加1或者2
        digite = re.findall('\d+',code)
        print("数字部分",digite)
        #注意合约中有些没有数字
        if digite:
            pure_digite = digite[0]
            len_num =len(pure_digite)
            if len_num == 3:
                #19年合约到期的情况
                pure_digite1 = '1'+pure_digite
                #20年合约到期的情况
                pure_digite2 = '2'+pure_digite

                fin_code1 = word +pure_digite1
                fin_code2 = word +pure_digite2
                print('start get 3',fin_code1)
                res = gets(url = self.url+fin_code1)
                #将结果进行一系列的格式转换,如果没有访问到，返回结果为空
                con = re.findall('"(.*?)"', res['message'])[0]
                con = con.split(',')
                print(con[0])
                if con[0]:
                    return con[0]
                #当19年合约没有查询到，使用20年查询
                else:
                    res = gets(url=self.url + fin_code1)
                    # 将结果进行一系列的格式转换,如果没有访问到，返回结果为空
                    con2 = re.findall('"(.*?)"', res['message'])[0]
                    con2 = con2.split(',')
                    print(con2[0])
                    if con2[0]:
                        return con2
                    return None
            fin_code3=word + pure_digite
            print('start get 4',fin_code3)
            # 将结果进行一系列的格式转换
            res = gets(url=self.url + fin_code3)
            print(res)
            con =  re.findall('"(.*?)"',res['message'])[0]
            con = con.split(',')
            print(con[0])
            if con[0]:
                return con[0]
            else:
                return None




        else:
            print('合约中没有数字')
            res = gets(url=self.url + code)
            con = re.findall('"(.*?)"', res['message'])[0]
            con = con.split(',')
            print(con[0])
            if con[0]:
                return con[0]
            else:
                return None




if __name__ =='__main__':
    # future = FutureSetUp()
    # cn= future.run('b1905')
    # print(cn)


    logintime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    url = 'https://wechat.17aitec.xyz/api/trade/temmsg'
    #
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    #
    post_data = {
        'token': '1e74812f38fa0a8707567dfbc9b6cfda',
        # 'openid': 'o7K_g04fAv1dExrgfGFqnz33E7mA',
        'channel_id': '2',
        'keyword1': '棕榈油1709(P1709)',
        'keyword2': '5203',
        'keyword3': '卖出/开仓',
        'keyword4': '1',
        'keyword5': logintime,
    }
    con = wechatInterface(url,post_data).run()
    print(con)

    # url ='https://wechat.17aitec.xyz/api/trade/trader_useful_channel'
    #
    # post_data = {'token': '1e74812f38fa0a8707567dfbc9b6cfda',}
    # con = operaters(url,post_data,headers).run()
    # print(con)


    # url = 'https://wechat.17aitec.xyz/api/trade/channnel_subscribe'
    # post_data={
    #     'token': '1e74812f38fa0a8707567dfbc9b6cfda',
    #     'channel_id': '2',
    # }
    # con = wechatInterface(url,post_data,headers = headers).run()
    # print(con)

