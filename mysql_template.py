# encoding: UTF-8
import pymysql
class SqlHelper():
    def __init__(self,host,port,db,user,password):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.password=password
        self.charset="utf8"

    # 创建连接和得到游标
    def __connect(self):
        self.conn=pymysql.connect(host=self.host,port=self.port,db=self.db,user=self.user,password=self.password,charset=self.charset)
        self.cursor=self.conn.cursor()
        # 游标设置为字典类型,输出的内容为字典格式，上面的为列表形式
        # cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

        # 查询一条记录
    def fetchone(self,sql,*params):
        try:
            self.__connect()
            #可以执行的语句数
            self.cursor.execute(sql,*params)
            # 获取返回的结果（查询有返回结果，增删改没有返回结果）
            data=self.cursor.fetchone()
            return data
        except Exception as e:
            print("错误信息是====》",e)
        finally:
            self.close()

    # 查询所有信息

    def fetchall(self,sql,*params):
        try:
            self.__connect()
            self.cursor.execute(sql,*params)
            data =self.cursor.fetchall()
            return data
        except Exception as e:
            print("错误信息是===》",e)
        finally:
            self.close()

    # 增删改的操作
    def update(self,sql,*params):
        try:
            self.__connect()
            count=self.cursor.execute(sql,*params)

            self.conn.commit()
            return count


        except Exception as e:
            print("错误信息为===》",e)
            # rollback回滚的意思。  就是数据库里做修改后 （ update, insert, delete）未commit
            # 之前使用rollback可以恢复数据到修改之前。
            self.conn.rollback()
        finally:self.close()


    # 关闭资源方法
    def close(self):
        self.__connect()
        if self.cursor !=None:
            self.cursor.close()
        if self.conn !=None:
            self.conn.close()