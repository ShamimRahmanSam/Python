x = "Awesome"                           #eta global variable
                                       #Variables that are created outside of a function (as in all of the examples above) are known as global variables.Global variables can be used by everyone, both inside of functions and outside.
def myfunc():                           #CREATED OWN FUNCTIOON   and function er output 1at e show ghoy tai awesome er ta pore print hocche
  x = "jhakasss"                        #inside e thakay eta global variable nah
  print("Python is " + x)
myfunc()

print("Python is " +x)                 #function uprer mto create krle last er print er jnne space/ indentation use korle nicher output ta ashbena. bhul hbe space dile\



               #Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
                            #To create a global variable inside a function, you can use the global keyword.

def Sam():                              #newfunctionfor Global Keyword
  global x                              #upre variable na deyay inside e deya hoise r setake global way te use kortei global keyword used.
  x = "fantastic"                       # ei variable global way te used chaile uprer global diye variable dite hbe evabe.. aage eta diye pore uprer global x dile hbe na
Sam()

print("Python is " + x)



                            #Also, use the global keyword if you want to change a global variable inside a function.
             #To change the value of a global variable inside a function, refer to the variable by using the global keyword:

global s
s ='jshbjash'           # etai output e ashbe cz erta global tai funtion er vitrer s er ans ashbena print korle
z = "awesome"            #ei variable ta kaje lagbena cz function er vitre z er value changed tai.and seta global kora houay etar value ow ekhon lkorrah e show korbe global hoye jaway

def myfunc():
  global z
  z = "korrah"
  s = "shuvo"
  print("jhdj " + s)          #eta function er vitre houay  s=shuvo ashbe but function er bairer s ta print korle global s ta ashbe ouput
myfunc()

print("Python is " + z)
print("jhgj " +s)