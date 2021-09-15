
print(dir(" "))





print (help(" "))




class Apple:
    pass




class Apple:
    color=""
    flavor=""
    j=Apple()
    j.color="red"
    j.flavor="sweet"

    print(j.flavor)
    print(j.color)







    '''
Print (j.color). Print j.flavor).
 The syntax used to access the attributes is called dot notation because of the dot used in the expression.
  Dot notation lets you access any of the abilities that the object might have,
   called methods or information that it might store called attributes, like flavor. 
   The attributes and methods of some objects can be other objects and can have attributes and methods of their own. 
or example, we could use the upper method to turn the string of the color attribute to uppercase. So print (j.color.upper()).'''




'''Classes and Objects in Detail
We can use the type() function to figure out what class a variable or value belongs to. 
For example, type(" ") tells us that this is a string class. The only attribute in this case is the string value, 
but there are a bunch of methods associated with the class. We've seen the upper() method, 
which returns the string in all uppercase, as well as isnumeric() which returns a boolean telling us whether or not the string is a number. 
You can use the dir() function to print all the attributes and methods of an object. 
Each string is an instance of the string class, having the same methods of the parent class. 
Since the content of the string is different, the methods will return different values.
 You can also use the help() function on an object, which will return the documentation for the corresponding class.
 This will show all the methods for the class, along with parameters the methods receive, types of return values, and a description of the methods.
 
 
 
 
 
 
 
 When you call the name of a class, the constructor of that class is called. This constructor method is always named __init__.
  You might remember that special methods start and end with two underscore characters. In our example above, the constructor method takes the self variable, which represents the instance, 
 as well as color and flavor parameters. These parameters are then used by the constructor method to set the values for the current instance. 
 
 
 
 In addition to the __init__ constructor special method, there is also the __str__ special method.
  This method allows us to define how an instance of an object will be printed when it’s passed to the print() function. 
  If an object doesn’t have this special method defined, it will wind up using the default representation, which will print the position of the object in memory.
  Not super useful. Here is our Apple class, with the __str__ method added:
 
 
 What Is a Method?
Calling methods on objects executes functions that operate on attributes of a specific instance of the class. 
This means that calling a method on a list, for example, only modifies that instance of a list, and not all lists globally.
 We can define methods within a class by creating functions inside the class definition.
  These instance methods can take a parameter called self which represents the instance the method is being executed on. 
  This will allow you to access attributes of the instance using dot notation, like self.name, which will access the name attribute of that specific instance of the class object.
 When you have variables that contain different values for different instances, these are called instance variables.
 
 
 
 
 
 Classes and Instances
Classes define the behavior of all instances of a specific class.
Each variable of a specific class is an instance or object.
Objects can have attributes, which store information about the object.
You can make objects do work by calling their methods.
The first parameter of the methods (self) represents the current instance.
Methods are just like functions, but they can only be used through a class.
Special methods
Special methods start and end with __.
Special methods have specific names, like __init__ for the constructor or __str__ for the conversion to string.
Documenting classes, methods and functions
You can add documentation to classes, methods, and functions by using docstrings right after the definition.'''