import graphene
from graphene import relay
from graphene_sqlalchemy import (SQLAlchemyObjectType, SQLAlchemyConnectionField)
from models import (Comrade as ComradeModel, Question as QuestionModel, Round as RoundModel)
from database_ops import create_question, create_comrade

class Comrade(SQLAlchemyObjectType):
	class Meta:
		model = ComradeModel
		interfaces = (relay.Node, )

class Question(SQLAlchemyObjectType):
	class Meta:
		model = QuestionModel
		interfaces = (relay.Node, )

class Round(SQLAlchemyObjectType):
	class Meta:
		model = RoundModel
		interfaces = (relay.Node, )

class Query(graphene.ObjectType):
	node = relay.Node.Field()
	comrades = SQLAlchemyConnectionField(Comrade)
	questions = SQLAlchemyConnectionField(Question)
	rounds = SQLAlchemyConnectionField(Round)

class AddQuestion(graphene.Mutation):
	class Input:
		text = graphene.String(required=True)

	ok = graphene.Boolean()
	question = graphene.Field(lambda: Question)
	
	def mutate(self, args, context, info):
		question = create_question(args['text'])
		return AddQuestion(question=question, ok=True)

class AddComrade(graphene.Mutation):
	class Input:
		name = graphene.String(required=True)
		email = graphene.String(required=True)

	ok = graphene.Boolean()
	comrade = graphene.Field(lambda: Comrade)

	def mutate(self, args, context, info):
		comrade = create_comrade(**args)
		return AddComrade(comrade=comrade, ok=True)

class Mutation(graphene.ObjectType):
	add_question = AddQuestion.Field()
	add_comrade = AddComrade.Field()

schema = graphene.Schema(query=Query, mutation=Mutation, types=(Comrade, Question, Round))
