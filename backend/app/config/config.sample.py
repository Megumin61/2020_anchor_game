class BaseConfig:
    begin = '2020-11-4 0:00:00'  # 开始时间
    end = '2020-11-20 0:00:00'  # 结束时间
    frontend_baseurl = ''  # 前端小游戏地址


DatabaseConfig = dict(
    username='',
    password='',
    host='localhost',
    port=3306
)

dbname = {
    'development': '',
    'production': '',
    'testing': ''
}


def get_database_url(env: str) -> str:
    return 'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4&collation=utf8mb4_unicode_ci'.format(
        **DatabaseConfig, database=dbname[env])


class AppConfig:
    SECRET_KEY = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_RECORD_QUERIES = True
    DEBUG = False


class AppConfigDev(AppConfig):
    SQLALCHEMY_DATABASE_URI = get_database_url('development')
    DEBUG = True
    SQLALCHEMY_ECHO = True


class AppConfigProd(AppConfig):
    SQLALCHEMY_DATABASE_URI = get_database_url('production')
    SQLALCHEMY_RECORD_QUERIES = False


class AppConfigTest(AppConfig):
    SQLALCHEMY_DATABASE_URI = get_database_url('testing')
    TESTING = True
    SQLALCHEMY_ECHO = True


app_config = {
    'development': AppConfigDev,
    'production': AppConfigProd,
    'testing': AppConfigTest
}
