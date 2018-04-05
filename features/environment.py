from test_app import FlaskTest
from app import app


def before_scenario(context, scenario):
    context.client = FlaskTest(app)


def after_scenario(context, scenario):
    del context.client
