import camelcase                                              #pip theke package ta download koira ja korar sob koira kapaya felsi by cmd prompt

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))      #This method capitalizes the first letter of each word.











'''Python Try Except
The    try            block lets you test a block of code for errors.

The    except         block lets you handle the error.

The    finally        block lets you execute code, regardless of the result of the try- and except blocks.

Exception Handling--
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
These exceptions can be handled using the try statement:'''


#The try block will generate an error, because x is not defined:
try:
  print(z)
except:
  print("An exception occurred")




'''Many Exceptions
You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

Example
Print one message if the try block raises a NameError and another for other errors:'''
#The try block will generate a NameError, because x is not defined:

try:
  print(y)
except NameError:
  print("Variable y is not defined")
except:
  print("Something else went wrong")






#The try block does not raise any errors, so the    else    block is executed:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")






#The finally block gets executed no matter if the try block raises any errors or not:

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")







'''Raise an exception
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.

Example
Raise an error and stop the program if x is lower than 0:'''

x = -2

if x < 0:
  raise Exception("Sorry, no numbers below zero")







'''The raise keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.

Example
Raise a TypeError if x is not an integer:'''

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")                      # ager program tar jnne ei program ta run hbena. but aladavabe korle program tar output pawa jabe ei last line ta error hisebe





#The try block will raise an error when trying to write to a read-only file:
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()             # The program can continue, without leaving the file object open
                        # upre NameError use koray etar output er sthe  NameError: name 'f' is not defined etaw show krbe ager 2 ta program er agei krle.
                        # r first e krle Nameerror ta r dekhabena. but last e koray kono output e asheni









  '''What is Exception?
An exception is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. In general, when a Python script encounters a situation that it cannot cope with, it raises an exception. An exception is a Python object that represents an error.

When a Python script raises an exception, it must either handle the exception immediately otherwise it terminates and quits.

Handling an exception
If you have some suspicious code that may raise an exception, you can defend your program by placing the suspicious code in a try: block. After the try: block, include an except: statement, followed by a block of code which handles the problem as elegantly as possible.

Syntax
Here is simple syntax of try....except...else blocks −'''