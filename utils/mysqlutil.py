import pymysql

from utils.logutil import Logger


# from utils.logutil import logs


class MysqlUtile:
    """
    """

    def __init__(self, host, user, password, database, port=3306):
        try:
            self.conn = pymysql.connect(host=host, user=user, password=password, database=database,
                                        port=int(port), cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            print("数据库连接失败")
            raise e
        self.cur = self.conn.cursor()
        self.logs = Logger.logs()

    def get_fetchone(self, sql):
        """
        查询一条
        :return:
        """
        self.cur.execute(sql)
        res = self.cur.fetchone()
        return res

    def get_fetchall(self, sql):
        """
        查询多条
        :return:
        """
        self.cur.execute(sql)
        res = self.cur.fetchall()
        return res

    def commit(self, sql):
        """
        修改、提交sql
        :param sql:
        :return:
        """
        try:
            if self.conn and self.cur:
                self.cur.execute(sql)
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.logs.error("提交不成功：%s" % e)
            return False
        return True

    def __del__(self):
        """
        关闭对象
        :return:
        """
        if self.conn is not None:
            self.conn.close()
        if self.cur is not None:
            self.cur.close()

# if __name__ == '__main__':
#     mysql = MysqlUtile(host="127.0.0.1", user="root", password="", database="mysql", port=3306)
#     # res = mysql.get_fetchone("select * from tb_users")
#     res = mysql.commit("create table stu2(id int ,name varchar(20),class varchar(30),age varchar(10))")
#     print(res)
