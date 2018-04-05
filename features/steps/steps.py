from behave import *


@when(u'I navigate to Home Page')
def step_impl(ctx):
    ctx.resp = ctx.client.get('/')


@when(u'Home Page should be displayed')
def step_impl(ctx):
    assert 'Home Page' in ctx.resp
