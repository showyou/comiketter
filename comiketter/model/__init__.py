from datetime import datetime
from pylons import config
from sqlalchemy import Column, MetaData, Table, types
from sqlalchemy.orm import mapper
from sqlalchemy.orm import scoped_session, sessionmaker

Session = scoped_session(sessionmaker(autoflush=True, transactional=True,
									bind=config['pylons.g'].sa_engine))

metadata = MetaData()

position_table = Table('position', metadata,
	Column('id',types.Integer, primary_key=True),
	Column('name',types.Unicode(40), default='hoge'),
	Column('pos',types.Unicode(), default=''),
	Column("update", types.DateTime, default=datetime.now)
)

class Position(object):
	pass

mapper(Position, position_table)

