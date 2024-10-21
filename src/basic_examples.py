import sqlalchemy as sa
from sqlalchemy import create_engine, text

engine = create_engine(
    'sqlite:///database.db',  # connection string address
    echo=True,  # show the SQL query at the console
)

print(engine)
print(engine.dialect)
print(engine.pool)
print(engine.pool.status())

metadata = sa.MetaData()
comments_table = sa.Table(
    'comments',
    metadata,
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('comment', sa.String(), nullable=False),
    sa.Column('live', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
)

metadata.create_all(engine)

with engine.connect() as connection:
    print(connection.connection.dbapi_connection)
    print(engine.pool.status())

    sql = text('select id, name, comment from comments')
    result = connection.execute(sql)
