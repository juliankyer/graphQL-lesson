## Installation

Requires Python 2.7

```
pip install virtualenv
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Usage

```
. venv/bin/activate
./app.py
```
Navigate to http://localhost:5000/graphql-relay


TODO:

* Round/iteration on question
* Has question been fully answered?
* Has Round been did?
* Slack names

PLAN (not the same as TODO):
* Create rounds mutation (and link rounds to question)
* Link round and comrade mutation
* Heroku deploy
* Determine filters (ex query unfulfilled questions or rounds)
* Optional things -- slack integration, email notifications


