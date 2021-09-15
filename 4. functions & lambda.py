'''Python Functions
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
In Python a function is defined using the def keyword:
To call a function, use the function name followed by parenthesis:'''

def x():
  print("Hello from a function")
x()







'''Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
The following example has a function with one argument (fname). 
When the function is called, we pass along a first name, which is used inside the function to print the full name: 
Arguments are often shortened to args in Python documentations.

Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.
From a function's perspective:
    A parameter is the variable listed inside the parentheses in the function definition.
    An argument is the value that are sent to the function when it is called.'''

def my_function(fname):
 print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")                               # function er aage indentation lagena after print
my_function("Linus")



def myfunction(fname, lname):
  print(fname + " " + lname)                        # If you try to call the function with 1 or 3 arguments, you will get an error:.. ekhane just fname or lname cl krle error show krbe  output e
myfunction("Emil", "Refsnes")






'''Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:  see below down

Arbitrary Arguments are often shortened to *args in Python documentations'''

def myfunction (*kids):
  print ("The youngest child is " + kids[2])
myfunction ("Emil", "Tobias", "Linus")







'''Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.'''

def my_function(child3, child2, child1):                    # The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
    print("The youngest child is " + child1)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")






'''Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:
Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.'''

def function(**kid):
  print("His last name is " + kid["fname"])
function(fname = "Tobias", lname = "Refsnes")





'''Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:'''

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")





'''Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:'''

def my_function(food):
  for x in food:
    print(x)                            # fruits er niche print dile return error hbe
fruits = ["apple", "banana", "cherry"]
my_function(fruits)






'''Return Values
To let a function return a value, use the return statement:'''

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))








'''The pass Statement
function definitions cannot be empty,
but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.'''

def myfunction():
  pass                          # having an empty function definition like this, would raise an error without the pass statement








'''Recursion
Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. It means that a function calls itself. 
This has the benefit of meaning that you can loop through data to reach a result.
The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates,
or one that uses excess amounts of memory or processor power. 
However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.'''


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 2)                          # k-2 dile output e 10 ta ashto nmbrs. r 3 dile 6/7 ta ashto..  -2 deyay 20/2=10 ta ashche output taw abr 2 kore prottek number por bere bere
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(20)







'''Python Lambda
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, 
but can only have one expression.

Syntax:
    lambda arguments : expression'''

x = lambda a: a + 10
print(x(5))

'''Lambda functions can take any number of arguments:
A lambda function that multiplies argument a with argument b and print the result:'''

x = lambda a, b: a * b
print(x(5, 6))


#A lambda function that sums argument a, b, and c and print the result:
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))



'''Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:'''

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(3)
print(mydoubler(13))







                #use the same function definition to make both functions, in the same program:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(7)

print(mydoubler(9))
print(mytripler(15))                    # Use lambda functions when an anonymous function is required for a short period of time.