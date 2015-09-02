# coding: utf-8

import os

MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_PORT = int(os.getenv('MYSQL_PORT', '3306'))
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'argonath')

ETCD_HOST = os.getenv('ETCD_HOST', 'localhost')
ETCD_PORT = int(os.getenv('ETCD_PORT', '4001'))
ETCD_HOST_BACKUP = os.getenv('ETCD_HOST_BACKUP', '')
ETCD_PORT_BACKUP = int(os.getenv('ETCD_PORT_BACKUP', '0'))

SQLALCHEMY_POOL_SIZE = 100
SQLALCHEMY_POOL_TIMEOUT = 10
SQLALCHEMY_POOL_RECYCLE = 2000

OPENID2_YADIS = 'http://openids.intra.hunantv.com/server/yadis/'
OPENID2_LOGOUT = 'http://openids.intra.hunantv.com/auth/logout/'

SUBDOMAINS = os.getenv('SUBDOMAINS', 'intra')

ARGONATH_ADMIN = os.getenv('ARGONATH_ADMIN', '')

try:
    from .local_config import *
except ImportError:
    pass

SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(
    MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE,
)
