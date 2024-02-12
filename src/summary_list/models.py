from sqlalchemy import Table, Column, Integer, String, ARRAY, MetaData

metadata = MetaData()


summary = Table(
    'summary',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('phone', String),
    Column('email', String),
    Column('work_exp', Integer),
    Column('age', Integer),
    Column('enployment', String),
    Column('schedule', String),
    Column('education', String),
    Column('languages', ARRAY(String))
)
