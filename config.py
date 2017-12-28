import os


basedir = os.path.abspath(os.path.dirname(__file__))
db_file_name = os.environ['FLASK_DB_FILENAME']
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, db_file_name)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SESSION_TYPE = 'memcached'
SECRET_KEY = 'super secret key'
DEBUG=1
site_ip_address = '0.0.0.0'
site_port = 8080
admin_name = os.environ["FLASK_ADMIN"]
admin_password = os.environ["FLASK_PASSWORD"]
