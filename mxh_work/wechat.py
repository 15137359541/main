# coding=utf-8
import requests

'''
通用post方式
url：请求的url地址
headers：请求的头信息数据，是以字典形式存在的
cookies：请求的cookies信息数据，以字典形式存在
proxies：代理IP地址，字典
params：get方式中？号后面的一大串数据，url地址截至到？以前
timeout：客户端与服务器的连接时常
data：同form表单，对应与form中的id，键，也是字典形式的
参数默认值设置
'''


def posts(url, data, params=None, proxies=None, timeout=20, cookies=None, headers=None):
    # 建立与服务端的会话
    s = requests.session()
    ret = {}
    # 返回值数据
    ret["issucess"] = 0
    ret["message"] = ""
    try:
        # 如果params有信息，则设置params
        if params is not None:
            s.params = params
        # 如果proxies有效，则设置proxies
        if proxies is not None:
            s.proxies = proxies
        # 默认设置timeout为20秒，可自定义设置
        if timeout != 20:
            s.timeout = timeout
        # 如果cookies有效，则设置cookies
        if cookies is not None:
            s.cookies = cookies
        # 如果headers有效，则设置headers
        if headers is not None:
            s.headers = headers
        # 发送请求包
        r = s.post(url, data=data, verify=False)
        if r:
            ret["issucess"] = 1
            ret["message"] = r.content
    except Exception as ex:
        # 异常处理
        print (ex)
        ret["message"] = ex
    finally:
        # 关闭本次会话
        if s:
            s.close()
    # 返回数据
    return ret


'''
通用的get方法
url：请求的url地址
headers：请求的头信息数据，是以字典形式存在的
cookies：请求的cookies信息数据，以字典形式存在
proxies：代理IP地址，字典
params：get方式中？号后面的一大串数据，url地址截至到？以前
timeout：客户端与服务器的连接时常
参数默认值设置
'''


def gets(url, headers=None, cookies=None, proxies=None, params=None, timeout=20):
    # 与服务器建立会话连接
    s = requests.session()
    ret = {}
    # 设置返回值参数
    ret["issuccess"] = 0  # 是否成功的标志
    ret["message"] = ""  # 返回内容
    try:
        # 如果headers有效，则设置headers
        if headers is not None:
            s.headers = headers
        # 如果cookies有效，则设置cookies
        if cookies is not None:
            s.cookies = cookies
        # 如果proxies有效，则设置proxies
        if proxies is not None:
            s.proxies = proxies
        # 如果params有效，则设置params
        if params is not None:
            s.params = params
        # 自定义timeout的值
        if timeout != 20:
            s.timeout = timeout
        # 发送请求
        r = s.get(url, verify=False)
        # 设置返回标志
        if s:
            ret["issuccess"] = 1
            # 设置返回值
            ret["message"] = r.content
            ret["cookie"] = s.cookies
    except Exception as ex:
        print(ex)
        ret["message"] = ex
    finally:
        # 结束会话
        if s:
            s.close()
    return ret