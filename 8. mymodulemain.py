import mymodule                                     # Now we can use the module we just created, by using the import statement:

mymodule.greeting('Sam')                            # When using a function from a module, use the syntax: module_name.function_name

a = mymodule.person['age']

print(a)







from mymodule import z                              # can choose to import only parts from a module, by using the from keyword.
print(z)                                            # output ashbe 15 . mymodule.py program tay z=x+y bola hoise r x,y er value deya ase tai






from mymodule import person
print(person["age"])                               # When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"] eta dite hbe, not mymodule.person1["age"] evabe dile output ashbena






#You can name the module file whatever you like, but it must have the file extension .py
# Re-naming a Module-- You can create an alias when you import a module, by using the as keyword:

import mymodule as mx               #re-naming module
a = mx.person["age"]
print(a)







'''Built-in Modules
There are several built-in modules in Python, which you can import whenever you like.
--
Import and use the platform module:'''

import platform
x = platform.system()
print (x)







'''Using the dir() Function--
There is a built-in function to list all the function names (or variable names) in a module. The dir() function:'''

import platform
a = dir(platform)                           # The dir() function can be used on all modules, also the ones you create yourself.
print(a)