import sqlalchemy as sa
from sqlalchemy import create_engine, MetaData, URL

url_obj = URL.create(
    drivername='mysql+mysqldb',
    username='root',
    password='pwd',
    host='localhost',
    database='db_name',
)
print(url_obj)
engine = create_engine(
    url_obj,
    echo=False,  # show the SQL query at the console
)
metadata = MetaData()

inspect = sa.inspect(engine)

for table_name in inspect.get_table_names():
    print(table_name)
    table = sa.Table(table_name, metadata, autoload_with=engine)
    print(table)
    constraints = inspect.get_unique_constraints(table_name)
    print(constraints)
    print()
