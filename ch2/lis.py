import math
import operator as op
from collections import ChainMap as Environment

Symbol = str
List = list
Number = (int, float)


class Procedure(object):
    "A user-defined Scheme procedure."

    def __init__(self, params, body, env):
        self.params, self.body, self.env = params, body, env

    def __call__(self, args):
        env = Environment(dict(zip(self.params, args)), self.env)
        return eval(self.body, dict(env))
