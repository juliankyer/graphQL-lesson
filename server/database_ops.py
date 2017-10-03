from datetime import date, timedelta

from models import Comrade, Question, Round, comrade_to_round
from database import db_session, Base, engine


one_week = timedelta(days=7)

def create_question(text):
	new_question = Question(text=text)
	db_session.add(new_question)
	db_session.commit()
	return new_question

def create_comrade(name, email):
	new_comrade = Comrade(name=name, email=email)
	db_session.add(new_comrade)
	db_session.commit()
	return new_comrade

def init_db():
	Base.metadata.drop_all(bind=engine)
	Base.metadata.create_all(bind=engine)

	wall_question = Question(text='What was on your wall as a kid?')
	db_session.add(wall_question)
	pet_question = Question(text='What was your favorite pet?')
	db_session.add(pet_question)

	matt = Comrade(name='Matt', email='matthew.wood@cognizant.com')
	db_session.add(matt)
	julian = Comrade(name='Julian', email='julian.kyer@cognizant.com')
	db_session.add(julian)

	wall_1 = Round(name='wall_round_one', date=date.today(), question=wall_question)
	wall_2 = Round(name='wall_round_two', date=date.today() + one_week, question=wall_question)

	pet_1 = Round(name='pet_round_one', date=date.today() + 2 * one_week, question=pet_question)
	pet_2 = Round(name='pet_round_two', date=date.today() + 3 * one_week, question=pet_question)

	db_session.add_all([wall_1, wall_2, pet_1, pet_2])

	db_session.commit()

	db_session.execute(comrade_to_round.insert().values([(matt.uuid, wall_1.uuid),
														 (julian.uuid, wall_2.uuid),
														 (julian.uuid, pet_1.uuid),
														 (matt.uuid, pet_2.uuid)
														]))
	db_session.commit()

