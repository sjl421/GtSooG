from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.objects.Base import Base
from utils import Log

__engine = None

DIALECT_SQLITE = 'sqlite'
DIALECT_MYSQL = 'mysql'
DIALECT_POSTGRES = 'postgresql'


# TODO: make configurable
def __get_engine(db_dialect=DIALECT_POSTGRES, db_name='gtsoog', user='postgres', password='root', host='localhost', port=5432):
    global __engine
    auth_string = ""
    if user:
        auth_string += user
        if password:
            auth_string += ':' + password
        auth_string += '@'
    port_string = ""
    if port:
        port_string += ':' + str(port)

    if __engine is None:
        if db_dialect == DIALECT_SQLITE:
            __engine = create_engine('sqlite:///{0}.db'.format(db_name))
        elif db_dialect == DIALECT_MYSQL:
            url = r'mysql+pymysql://{auth_string}{host}{port_string}/{db_name}?charset=utf8mb4'.format(
                auth_string=auth_string,
                host=host,
                port_string=port_string,
                db_name=db_name
            )
            __engine = create_engine(url, pool_recycle=3600)
        elif db_dialect == DIALECT_POSTGRES:
            url = r'postgresql+pg8000://{auth_string}{host}{port_string}/{db_name}'.format(
                auth_string=auth_string,
                host=host,
                port_string=port_string,
                db_name=db_name
            )
            __engine = create_engine(url, client_encoding='utf8')
        else:
            Log.error("SQL Dialect " + db_dialect + " is not supported.")
            return None
    return __engine


# noinspection PyUnresolvedReferences
def create_db():
    # Import all ORM objects to register them in SQLAlchemy Base
    from model.objects.IssueTracking import IssueTracking
    from model.objects.Repository import Repository
    from model.objects.Commit import Commit
    from model.objects.File import File
    from model.objects.Issue import Issue
    from model.objects.Version import Version

    engine = __get_engine()
    if engine is None:
        Log.error("DB Engine could not be created! DB init failed!")
    else:
        Base().base.metadata.create_all(engine)


def create_session():
    engine = __get_engine()
    if engine is None:
        Log.error("DB Engine could not be created! Session creation failed!")
        return None
    session = sessionmaker()
    session.configure(bind=engine)

    return session()
