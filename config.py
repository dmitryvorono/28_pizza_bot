import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'pizza.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
DEBUG=1
site_ip_address = '0.0.0.0'
site_port = 8080