# encoding: UTF-8
# 引入函数
from mysql_template import SqlHelper
# 创建对象
per=SqlHelper("localhost",3306,"db_two","root","root")
# 获取一条信息
# data=per.fetchone("select * from emp")
# print(data)
#
# # 获取所有的对象
# data1=per.fetchall("select *from emp")
# print(data1)

# 增加用户
# one="insert into emp VALUE (null,%s,%s,%s,%s,%s)"
# one1=["难兄",33,"男","9999","2"]
# count=per.update1(one,one1)
# print(count)
# 删除用户
# two="delete from emp where deptid=%s"
# two1=(3)
# count=per.update1(two,two1)
# print(count)
# 查询总数量
# sql = "select count(*) from emp "
# data = per.fetchall(sql)
# print(data)

# 将数据库的记录输出
class User(object):
    def __init__(self,id,name,age,sex,tel,deptid):
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.tel = tel
        self.deptid = deptid

    def __str__(self):
        return "用户名称%s,用户电话%s,用户性别%s,用户年龄%s" %(self.name,self.tel,
                                               self.sex,self.age)

data2=per.fetchall("select *from emp")
print(data2)

list=[]
for x in data2:
    u=User(x[0],x[1],x[2],x[3],x[4],x[5])
    list.append(u)
for i in list:
    print(i)
