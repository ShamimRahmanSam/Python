'''Python Iterators--
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol,
which consist of the methods __iter__() and __next__().

Iterator vs Iterable--
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:'''


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))




#We can also use a for loop to iterate through an iterable object:  #The for loop actually creates an iterator object and executes the next() method for each loop.
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)






#Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))



#We can also use a for loop to iterate through an iterable object:..Iterate the characters of a string:
mystr = "banana"
for x in mystr:
  print(x)







'''Create an Iterator---
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
As you have learned in the Python Classes/Objects chapter, 
all classes have a function called __init__(), which allows you do some initializing when the object is being created.
The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence.

Example--
Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):'''


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))







'''StopIteration--
The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
To prevent the iteration to go on forever, we can use the StopIteration statement.
In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:

Example--
Stop after 20 iterations:'''

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)











'''Python Scope--
A variable is only available from inside the region it is created. This is called scope.

Local Scope--
A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

Example--
A variable created inside a function is available inside that function:'''

def myfunc():
    x = 300                   #this variable is scope... A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
    print(x)
myfunc()


x=400
print(x)                       #without function easily e ber kora jay chailei if we don't needed that funtion






'''Function Inside Function---
As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function:
The local variable can be accessed from a function within the function:'''

def myfunc():
  x = 500
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()






'''Global Scope--
A variable created in the main body of the Python code is a global variable and belongs to the global scope.
Global variables are available from within any scope, global and local.
A variable created outside of a function is global and can be used by anyone:'''

x = 900
def myfunc():
  print(x)
myfunc()
print(x)





'''Naming Variables--
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, 
one available in the global scope (outside the function) and one available in the local scope (inside the function):
The function will print the local x, and then the code will print the global x:'''

x = 1000
def myfunc():
  x = 500
  print(x)
myfunc()
print(x)





'''Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
The global keyword makes the variable global.
If you use the global keyword, the variable belongs to the global scope:'''

x = 1462                # etake global kora jay na. but nicher mto function er vitor hole global kora jeto
def myfunc():
  global x              #global x na dile output ashto 1195 ek bar.r arekbar ashto 1462. but eta global x deyay now uprer tar output taw 1462 na eshe 1195 ashbe
  x = 1195
  print(x)
myfunc()
print(x)




