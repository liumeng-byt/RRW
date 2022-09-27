from config.conf import ConfigYaml
from utils.mysqlutil import MysqlUtile


def init_db(db_alias):
    # 初始化数据化信息，获取数据
    db_info = ConfigYaml().get_db_config_yml(db_alias)
    hsot = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    db_name = db_info["db_name"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"])
    # 初始化mysql对象
    conn = MysqlUtile(host=hsot, user=user, password=password, database=db_name, port=port)
    return conn
    # 其他文件中调用该mysql对象即可，通过该对象调用mysql封装的方法,如下：
    # data = conn.get_fetchone("select * from tb_users")
    # print(data)

