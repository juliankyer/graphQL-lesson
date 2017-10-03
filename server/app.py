#!/usr/bin/env python

from flask import Flask
from flask_cors import CORS 
from flask_graphql import GraphQLView

from database import db_session
from database_ops import init_db
from relay_schema import schema as relay_schema

app = Flask(__name__)
app.debug = True

app.add_url_rule('/graphql-relay', view_func=GraphQLView.as_view('graphql-relay',
															     schema=relay_schema,
															     graphiql=True,
															     context={'session': db_session}
																))

CORS(app, resources={'/graphql-relay': {'origins': '*'}})

@app.teardown_appcontext
def shutdown_session(exception=None):
	db_session.remove()

if __name__ == '__main__':
	init_db()
	app.run()
