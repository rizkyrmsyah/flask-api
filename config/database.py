import os

mysql = {
    'host': os.environ.get("DB_HOST"),
    'user': os.environ.get("DB_USERNAME"),
    'passwd': os.environ.get("DB_PASSWORD"),
    'port': os.environ.get("DB_PORT"), 
    'db': os.environ.get("DB_DATABASE")
}

MysqlConfig = "mysql+pymysql://{}:{}@{}:{}/{}".format(mysql['user'], mysql['passwd'], mysql['host'], mysql['port'], mysql['db'])