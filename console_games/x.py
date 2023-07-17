import pickle

class X:

    def __init__(self):

        self.a = "hallo"
        self.b = "world"

    def addition(self, a, b):
        return a+b

x=X()
print(x)

y=pickle.dumps(x)
print(y)
z = pickle.loads(y)

print(z)
from collections import OrderedDict
d = {"aa": 123, "bb": [1,2,3]}

import json

ds=json.dumps(d, indent=4)
print(ds)

with open("fun.json", "w") as xx:
    json.dump(d, xx, indent=4,s)

with open("fun.json", "r") as xx:
    xxx=json.load(xx)
    print(xxx)