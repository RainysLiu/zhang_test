from pymysql.connections import Connection

class MysqlConf:
    host = 'localhost'
    port = 3306
    user = 'root'
    password = '123456'
    database = 'tiantian'

class Handle_pymysql(object):
    def __init__(self, host=None, user=None, password=None, database=None):
        if host and user and password and database:
            self.__host = host
            self.__user = user
            self.__password = password
            self.__database = database
        elif host is None and user is None and password is None and database is None:
            self.__host = MysqlConf.host
            self.__user = MysqlConf.user
            self.__password = MysqlConf.password
            self.__database = MysqlConf.database
        else:
            raise Exception("参数不全")

    def __mysql_connect(self):
        conn = Connection(host=self.__host, user=self.__user, passwd=self.__password,
                          database=self.__database)
        cur = conn.cursor()
        return conn, cur

    def mysql_excute(self, sql):
        conn, cur = self.__mysql_connect()
        try:
            res = cur.execute(sql)
            conn.commit()
            # return res
        except Exception as err:
            print(err)
            return 0
        finally:
            cur.close()
            conn.close()

    @staticmethod
    def __test_result(dic_result):
        """
        """
        return len(dic_result)

    def mysql_query(self, sql):
        conn, cur = self.__mysql_connect()
        try:
            cur.execute(sql)
            result = cur.fetchall()
            return result
        except:
            return ()
        finally:
            cur.close()
            conn.close()


class TestDB:
    def __init__(self):
        self.mysql = Handle_pymysql()

    def test_query(self):
        sql = ""
        self.mysql.mysql_query(sql)

    def test_insert(self):
        sql = ""
        for i in range(1000):
            self.mysql.mysql_query(sql)

    def clean_data(self):
        pass

    def test(self):
        self.test_query()
        self.clean_data()
        self.test_insert()


if __name__ == '__main__':
    mysql_conn = Handle_pymysql()
    sql = "show databases;"
    result = mysql_conn.mysql_query(sql)
    print(result)
    sql = "show tables;"
    result = mysql_conn.mysql_query(sql)
    print(result)
    sql = "desc df_user_userinfo"
    result = mysql_conn.mysql_query(sql)
    print(result)
    sql = "select * from df_user_userinfo where id=1;"
    result = mysql_conn.mysql_query(sql)
    print(result)
    sql = "update df_user_userinfo set uname='liumang' where id=1"
    mysql_conn.mysql_excute(sql)
    print("修改成功")
    sql = "select * from df_user_userinfo where id=1"
    result = mysql_conn.mysql_query(sql)
    print(result)






