from uuid import uuid4
from sqlalchemy import (Column, DateTime, ForeignKey, func, String, CHAR, Table)
from sqlalchemy.orm import (backref, relationship)

from database import Base

comrade_to_round = Table('association', Base.metadata,
	Column('comrade_uuid', CHAR(36), ForeignKey('comrade.uuid')),
	Column('round_uuid', CHAR(36), ForeignKey('round.uuid'))
	)

class Comrade(Base):
	__tablename__ = 'comrade'
	uuid = Column(CHAR(36), primary_key=True, nullable=False, default=lambda: str(uuid4()))
	name = Column(String)
	email = Column(String)

class Question(Base):
	__tablename__ = 'question'
	uuid = Column(CHAR(36), primary_key=True, nullable=False, default=lambda: str(uuid4()))
	text = Column(String)

class Round(Base):
	__tablename__ = 'round'
	uuid = Column(CHAR(36), primary_key=True, nullable=False, default=lambda: str(uuid4()))
	name = Column(String)
	date = Column(DateTime)
	question_uuid = Column(CHAR(36), ForeignKey('question.uuid'))

	question = relationship(Question, backref=backref('rounds', uselist=True, cascade='delete,all'))
	comrades = relationship(Comrade, secondary=comrade_to_round, backref='rounds')

