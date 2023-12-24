import os

from sqlalchemy import text

user_name = os.environ.get('DATABASE_USERNAME').replace("\r", "")
password = os.environ.get('DATABASE_PASSWORD').replace("\r", "")
host = os.environ.get('DATABASE_HOST').replace("\r", "")
database_name = os.environ.get('DATABASE_NAME').replace("\r", "")


# user_name = 'root'

def get_database_url() -> str:
    return f"mysql+pymysql://{user_name}:{password}@{host}:3306/{database_name}?charset=utf8"


def test_connection():
    from sqlalchemy import create_engine
    print('Testing database connection...')
    print(get_database_url())
    engine = create_engine(get_database_url())
    with engine.connect() as connection:
        result = connection.execute(text('select 1'))
        print(result)
        assert result.fetchone()[0] == 1
        print('Database connection successful')


# test_connection()
