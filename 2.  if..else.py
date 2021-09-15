'''Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.



Conditionals Cheat Sheet
Conditionals Cheat Sheet
In earlier videos, we took a look at some of the built-in Python operators that allow us to compare values, and some logical operators we can use to combine values. We also learned how to use operators in if-else-elif blocks.

It’s a lot to learn but, with practice, it gets easier to remember it all. In the meantime, this handy cheat sheet gives you all the information you need at a glance.

Comparison operators
a == b: a is equal to b
a != b: a is different than b
a < b: a is smaller than b
a <= b: a is smaller or equal to b
a > b: a is bigger than b
a >= b: a is bigger or equal to b
Logical operators
a and b: True if both a and b are True. False otherwise.
a or b: True if either a or b or both are True. False if both are False.
not a: True if a is False, False if a is True.

An "if statement" is written by using the if keyword.'''


a = 200                                                   # chaile if(a>b): evabe or nahoy if a>b : evabeo bracket ta charai statement deya jay if else
b = 33
if (a > b):   print("a is greater than b")                # Short Hand If ..If you have only one statement to execute, you can put it on the same line as the if statement.0




a = 100
b = 500
if (a > b) :                                            # evabei if else use korte hoy.. if else for while esob loop condition er por  : eta use korte hoy
    print ('a is greater than  b')                      # space or indentation print er aage na dile error dekhabe output.Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
else :                                                  # In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b" .. You can also have an else without the elif:
    print('b is greater than a')




a = 33
b = 33
if (b > a):
  print("b is greater than a")
elif a == b:                                            # The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition"....  also the elif condition is not true, so we go to the else condition
  print("a and b are equal")                            # In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".
                                                        # more Complex Branching with elif Statements : Building off of the if and else blocks, which allow us to branch our code depending on the evaluation of one statement, the elif statement allows us even more comparisons to perform more complex branching. Very similar to the if statements, an elif statement starts with the elif keyword, followed by a comparison to be evaluated. This is followed by a colon, and then the code block on the next line, indented to the right. An elif statement must follow an if statement, and will only be evaluated if the if statement was evaluated as false. You can include multiple elif statements to build complex branching in your code to do all kinds of powerful things!



a = 2
b = 330
print("A") if a > b else print("B")                     # Short Hand If ..Else ...ei rule e korle  :  lagena after if else.. If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:



a = 330
b = 330
print("A") if a > b else print("equal") if a == b else print("B")           # can also have multiple else statements on the same line:





a = 200
b = 33
c = 500

if a > b and c > a:
  print("Both conditions are True")                       # egulo sob operators er program tay korechilam

if a > b or a > c:
  print("At least one of the conditions is True")         # evabe and or egulo use kora hoy





x = 41
if x > 10:
  print("Above ten,")
  if x > 20:                                              # nested if e emn space diye korte hoy
    print("and also above 20!")                           # can have if statements inside if statements, this is called nested if statements.
  else:
    print("but not above 20.")




a = 33
b = 200
if b > a:                                                 # if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
  pass                                                    # having an empty if statement like this, would raise an error without the pass statement




'''Decision-making is the anticipation of conditions occurring during the execution of a program and specified actions taken according to the conditions.

Decision structures evaluate multiple expressions, which produce TRUE or FALSE as the outcome. You need to determine which action to take and which statements to execute if the outcome is TRUE or FALSE otherwise.

Following is the general form of a typical decision making structure found in most of the programming languages −

Decision making
Python programming language assumes any non-zero and non-null values as TRUE, and any zero or null values as FALSE value.

Python programming language provides the following types of decision-making statements.

Sr.No.	Statement & Description
1	if statements
An if statement consists of a boolean expression followed by one or more statements.

2	if...else statements
An if statement can be followed by an optional else statement, which executes when the boolean expression is FALSE.

3	nested if statements
You can use one if or else if statement inside another if or else if statement(s).

Let us go through each decision-making statement quickly.

Single Statement Suites
If the suite of an if clause consists only of a single line, it may go on the same line as the header statement.


link-   https://www.tutorialspoint.com/python3/python_decision_making.htm    '''