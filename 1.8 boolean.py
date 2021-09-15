print (10>9)                                    # Booleans represent one of two values: True or False.  & int er jnne print er bracket e ' ' / "  "  lagena
print (10<5)                                    # You can evaluate any expression in Python, and get one of two answers, True or False.
print (9==9)                                    # When you compare two values, the expression is evaluated and Python returns the Boolean answer:



print(bool('jesjefhfuhfihfiedsfierehrie'))      # Any string is True, except empty strings. r hae chaile ei string er habijabi lekha ta r nicher numbers variable e rekhe then print(bool(y)) diyeo variable cl kore output ber kora jeto. but evabe shortcut way te kora jay
print(bool(82829489324934935))                  # Any number is True, except 0. r hae  emn number r uprer mto words er string ja e deina keno true bolbe boolean wise
print (bool(['apple', 'banana', 'cherry']))     # Any list, tuple, set, and dictionary are True, except empty ones. this one is list data type.



print(bool(False))                              #In fact, there are not many values that evaluates to False,
print(bool(None))                               # except empty values, such as (), [], {}, "", the number 0, and the value None.
print(bool(0))                                  # And of course the value False evaluates to False.
print(bool(""))                                 # specifically etay jodi " " er moddhe kichu likhi or emn ekta khali space ow dei tahole eta false na dekhiye true dekhabe.
print(bool(()))                                 # vitrer () eta na dileo hoto cz agei ekta deya ase. eta bujhate deya hoise
print(bool([]))                                 # [], {}, "", the number 0, and the value None egulor agei evabei bool( ) eta use korte hobe jodi boolean er kaj kori then
print(bool({}))



x = 200
print(isinstance(x, int))                       # Python also has many built-in functions that returns a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:



class myclass():                                # This class is for creating a class
  def __len__(self):                            # this def is for creating a function
    return 0                                    # just like c language
myobj = myclass()                               # One more value, or object in this case, evaluates to False,
print(bool(myobj))                              # and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:



def myFunction() :                              # Functions can Return a Boolean & we can create functions that returns a Boolean Value:
  return True
print(myFunction())



def myFunction() :                              # we can execute code based on the Boolean answer of a function:
  return True
if myFunction():
  print("YES!")                                 # as like this one -- Print "YES!" if the function returns True, otherwise print "NO!":
else:
  print("NO!")



a,b = 9,50                                      # When you run a condition in an if statement, Python returns True or False like this way:
if a > b :
    print ("a is greater than b")
else :
    print ('b is greater than a')