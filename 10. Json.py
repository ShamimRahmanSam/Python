'''JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.

JSON in Python--
Python has a built-in package called json, which can be used to work with JSON data.'''



#Parse JSON - Convert from JSON to Python--

import json

x =  '{ "name":"John", "age":30, "city":"New York"}'              # some JSON: and dui pashe ' ' eta dite hbe r vitre " " eta use korte hbe json er khtere

y = json.loads(x)                                                 # parse x: and  If you have a JSON string, you can parse it by using the json.loads() method.

print (y)
print(y["age"])                                                   # the result is a Python dictionary: and single resulty evabe pawa jay json theke python korle







'''Convert from Python to JSON--
If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.'''

import json

x = {"name": "John", "age": 30, "city": "New York"}               # a Python object (dict):

y = json.dumps(x)                                                 # convert into JSON:

print(y)                                                          # the result is a JSON string:
#print(y["age"])                                                   # evabe single kichu ber kora jayna. error dekhay python to json er khetre




'''You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None

example below down '''

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))






#Convert a Python object (into JSON strings:) containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))





'''You can also define the separators, default value is (", ", ": "),
which means using a comma and a space to separate each object, and a colon and a space to separate keys from values:

and #Format the Result--
The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
The json.dumps() method has parameters to make it easier to read the result:'''

import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4, separators=(". ", " = ")))         # use . and a space to separate objects, and a space, a = and a space to separate keys from their values:





'''Order the Result-- The json.dumps() method has parameters to order the keys in the result:

Example-- Use the sort_keys parameter to specify if the result should be sorted or not:'''


import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))             # and     json.dumps(x, indent=4))    use four indents to make it easier to read the result:
