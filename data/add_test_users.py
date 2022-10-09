# coding=gbk
import pymysql
from faker import Faker
from config.db_sql import  sql_create, sql_insert



class AddUsers():
    def __init__(self, host, user, password, database, port=3306):
        # self.data = ConfigYaml().get_db_config_yml("db_1")
        # self.mysql = MysqlUtile(host=self.data['db_host'],user=self.data['db_user'], password=self.data['db_password'], database=self.data['db_name'],port=self.data['db_port'])
        try:
            self.conn = pymysql.connect(host=host, user=user, password=password, database=database,
                                    port=int(port), cursorclass=pymysql.cursors.DictCursor)
        except Exception as e:
            print("数据库连接失败",e)
        self.cur = self.conn.cursor()
        self.fake = Faker('zh_CN')

    def create_table(self):
        try:
            self.cur.execute(sql_create)
        except Exception as e:
            print(e)

    def add_users(self):
        try:
            for j in range(100):
                dept_id = self.fake.random_int(min=10, max=20)
                name = self.fake.name()
                identity = self.fake.ssn()
                address = self.fake.address()
                job = self.fake.job()
                company = self.fake.company()
                user_type = self.fake.random_int(min=1, max=2)
                email = self.fake.email()
                phonenumber = self.fake.phone_number()
                self.cur.execute(sql_insert, (dept_id,name,identity,address,job,company,user_type,email,phonenumber))
                print('{}条数据插入成功'.format(j))
            self.conn.commit()
        except Exception as e:
            print(e)

    def __del__(self):
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    res = AddUsers(host="127.0.0.1", user="root", password="", database="mysql", port=3306)
    res.create_table()
    res.add_users()
