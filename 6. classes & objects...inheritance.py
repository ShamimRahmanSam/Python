'''Python Classes/Objects
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.'''


'''Object-Oriented Programming Defined
In object-oriented programming, concepts are modeled as classes and objects. 
An idea is defined using a class, and an instance of this class is called an object. 
Almost everything in Python is an object, including strings, lists, dictionaries, and numbers.
 When we create a list in Python, we’re creating an object which is an instance of the list class, which represents the concept of a list. 
Classes also have attributes and methods associated with them. Attributes are the characteristics of the class, while methods are functions that are part of the class.'''


'''Classes and Objects in Detail
We can use the type() function to figure out what class a variable or value belongs to. 
For example, type(" ") tells us that this is a string class. The only attribute in this case is the string value, 
but there are a bunch of methods associated with the class. We've seen the upper() method, 
which returns the string in all uppercase, as well as isnumeric() which returns a boolean telling us whether or not the string is a number. 
You can use the dir() function to print all the attributes and methods of an object. 
Each string is an instance of the string class, having the same methods of the parent class. 
Since the content of the string is different, the methods will return different values.
 You can also use the help() function on an object, which will return the documentation for the corresponding class.
 This will show all the methods for the class, along with parameters the methods receive, types of return values, and a description of the methods.'''




class sam :                                     # To create a class, use the keyword class:... Create a class named MyClass, with a property named x.. r hae class er name deyar por seshe : eta dite hoy
    x = 10                                      # eta output e na ashleo eta na dile cls create hbena. evabe bhitore kono ekta value key dite hbei
print(sam)                                      # etay indentation deini cz dilei bhul hoto



class sam:
    x=10
y = sam()
print(y.x)                                      # x.y dile hotona cz aage class diye then variable ta dite hbe . diye.... r eta na kore nicher way te easily output pawa jay. tokhon r uporer y variable e cls rakhar need htona.
#print(sam.x)



class sam:
    x=10
print(sam.x)                                    # uporer tay ei way er kotha bola hoise






'''The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:'''

class boy:
    def __init__(self,name,age,id):                     # The __init__() function is called automatically every time the class is being used to create a new object.
        self.name = name
        self.age = age
        self.id = id
s = boy('Sam', 22, 201611044094)
print(s.name)
print(s.age)
print(s.id)





'''Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.
Let us create a method in the Person class:'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  #def myfunc(self):                                # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
#p1.myfunc()                                        # ei hashtag deya lines program tay thakleo ami # diye rakhsi cz eta charai program run krbe, eta just new duction creation system ager function er moddhe





'''The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
Use the words mysillyobject and abc instead of self:'''

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()





'''Modify Object Properties
You can modify properties on objects like this:'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.age = 40                                  # evabe new variable niye change kora jay value cls er .just ei line ta ekdom first init function er program er mddhe korlei hbe berfore print.. ei program wise kothin lagle korar need nai
print(p1.age)






class Person:
  pass                                      # having an empty class definition like this, would raise an error without the pass statement








'''Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
Any class can be a parent class, so the syntax is the same as creating any other class:'''

class Person:

  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):                          # To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
  pass                                          # Use the pass keyword when you do not want to add any other properties or methods to the class.

x = Person("John", "Doe")                       # Use the Person class to create an object, and then execute the printname method:
x.printname()







'''Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.
We want to add the __init__() function to the child class (instead of the pass keyword).
Note: The __init__() function is called automatically every time the class is being used to create a new object.

Example : Add the __init__() function to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
    
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):                         # evabe child class e init function add korle nichei emn parent class er init function call korte hobe nahoy output error dekhabe. ei child cls er 3 ta line  na dileo output same ashto. just bujhate evabe kora hoise.
    Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()



'''Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.
Use the super() Function --- Python also has a super() function that will make the child class inherit all the methods and properties from its parent:'''


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)                                  #uporer ta r eta same program just difference ei super(). function ei..   super(). use korle class name person. deyar dorkar hoyna and (self) taw lagena.. and . lage super() er por or cls name er por.  check out that
    self.graduationyear = 2019                                      # adding this new properties called graduationyear.. evabei add kora lage child cls er moddhe
                                                                    #self.graduationyear = year  evabe dile nicher line e olsen er por 2019 dileo hoto and uprer child function tay lname er por year variable taw add kora lagto..but eta easy way otar cheye tai ota r korini.
x = Student("Mike", "Olsen")
x.printname()
print(x.graduationyear)                                             # eta use kora hoise just for that new properties graduationyear..





'''
        Final program of inheritance..

If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.        
Add a method called welcome to the Student class:  below down'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
x.printname()
x.welcome()









# Delete a class : below down
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1                                       # that's how delete krte hoy ejnne output e error dekhabe
print(p1)






''' Python has been an object-oriented language since the time it existed. Due to this, creating and using classes and objects are downright easy. This chapter helps you become an expert in using Python's object-oriented programming support.

If you do not have any previous experience with object-oriented (OO) programming, you may want to consult an introductory course on it or at least a tutorial of some sort so that you have a grasp of the basic concepts.

However, here is a small introduction of Object-Oriented Programming (OOP) to help you −


Overview of OOP Terminology
Class − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.

Class variable − A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. Class variables are not used as frequently as instance variables are.

Data member − A class variable or instance variable that holds data associated with a class and its objects.

Function overloading − The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved.

Instance variable − A variable that is defined inside a method and belongs only to the current instance of a class.

Inheritance − The transfer of the characteristics of a class to other classes that are derived from it.

Instance − An individual object of a certain class. An object obj that belongs to a class Circle, for example, is an instance of the class Circle.

Instantiation − The creation of an instance of a class.

Method − A special kind of function that is defined in a class definition.

Object − A unique instance of a data structure that is defined by its class. An object comprises both data members (class variables and instance variables) and methods.

Operator overloading − The assignment of more than one function to a particular operator.




Built-In Class Attributes
Every Python class keeps following built-in attributes and they can be accessed using dot operator like any other attribute −

__dict__ − Dictionary containing the class's namespace.

__doc__ − Class documentation string or none, if undefined.

__name__ − Class name.

__module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode.

__bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.




You can use issubclass() or isinstance() functions to check a relationships of two classes and instances.

The issubclass(sub, sup) boolean function returns True, if the given subclass sub is indeed a subclass of the superclass sup.

The isinstance(obj, Class) boolean function returns True, if obj is an instance of class Class or is an instance of a subclass of Class




Base Overloading Methods
The following table lists some generic functionality that you can override in your own classes −

Sr.No.	Method, Description & Sample Call
1	
__init__ ( self [,args...] )

Constructor (with any optional arguments)

Sample Call : obj = className(args)

2	
__del__( self )

Destructor, deletes an object

Sample Call : del obj

3	
__repr__( self )

Evaluatable string representation

Sample Call : repr(obj)

4	
__str__( self )

Printable string representation

Sample Call : str(obj)

5	
__cmp__ ( self, x )

Object comparison

Sample Call : cmp(obj, x)





Creating Classes
The class statement creates a new class definition. The name of the class immediately follows the keyword class followed by a colon as follows −

class ClassName:
   'Optional class documentation string'
   class_suite
The class has a documentation string, which can be accessed via ClassName.__doc__.

The class_suite consists of all the component statements defining class members, data attributes and functions.







[MUSIC] Object orientation is not easy to understand. So congratulations on getting through these Concepts. 
Let's quickly recap the main Concepts we've just covered. 
We've learned that in an object-oriented language like python real-world concepts are represented by classes. 
We know that instances of classes are usually called objects. 
That objects have attributes which are used to store information about them and we can make objects do work by calling their methods.
 We've also learned that we can access attributes and methods using dot notation. We then dove into objects can be organized by inheritance.
  And how they can be contained inside each other using composition. Wow, that really is a lot of new stuff. Congratulations on sticking with it.
   Objects are a great way for programmers to model real world Concepts. They let us have functions that work on specific things like reading a file, setting the subject for an email, calculating the size of a repository of packages and so on. Isn't it cool to see how all of this is coming together? As a sysadmin the objects ideal with the most represent individual users and their accounts. I use them to group lots of different properties that help me turn abstract code into tangible interactions. I also use objects in my code to group functions based on the data they act upon. For example, I recently needed to write a bunch of functions that were all operating on some specific file attributes. 
So I used a class to group all those functions making my code clearer and more reusable. Super helpful, right?'''