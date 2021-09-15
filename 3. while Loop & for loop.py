'''Python Loops
Python has two primitive loop commands:
    while loops
    for loops

    Anatomy of a While Loop
A while loop will continuously execute code depending on the value of a condition.
It begins with the keyword while, followed by a comparison to be evaluated,
then a colon. On the next line is the code block to be executed, indented to the right. Similar to an if statement,
the code in the body will only be executed if the comparison is evaluated to be true.
What sets a while loop apart, however, is that this code block will keep executing as long as the evaluation statement is true.
Once the statement is no longer true, the loop exits and the next line of code will be executed.



The power of for loops comes from the fact that it can iterate over a sequence of any kind of data, not just a range of numbers.
You can use for loops to iterate over a list of strings, such as usernames or lines in a file


***most important thing is :
 Use for loops when there's a sequence of elements that you want to iterate.
 Use while loops when you want to repeat an action until a condition changes.

 Not sure whether to use a for loop or a while loop?
 Remember that a while loop is great for performing an action over and over until a condition has changed.
 A for loop works well when you want to iterate over a sequence of elements.





for loops are best when you want to iterate over a known sequence of elements
but when you want to operate while a certain condition is true, while loops are the best choice




A recursive function must include a recursive case and base case.
The recursive case calls the function again, with a different value. The base case returns a value without calling the same function.




            To quickly recap the range() function when passing one, two, or three parameters:

One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, but this time increasing each step by the third parameter."""
'''

'''While Loops
A while loop executes the body of the loop while the condition remains True.

while condition:
    body
Things to watch out for!

Failure to initialize variables. Make sure all the variables used in the loop’s condition  are initialized before the loop.
Unintended infinite loops. Make sure that the body of the loop modifies the variables used in the condition, so that the loop will eventually end for all possible values of the variables.
Typical use:

While loops are mostly used when there’s an unknown number of operations to be performed, and a condition needs to be checked at each iteration.

For Loops
A for loop iterates over a sequence of elements, executing the body of the loop for each element in the sequence.

for variable in sequence
    body
The range() function:

range() generates a sequence of integer numbers. It can take one, two, or three parameters:

range(n): 0, 1, 2, ... n-1
range(x,y): x, x+1, x+2, ... y-1
range(p,q,r): p, p+r, p+2r, p+3r, ... q-1 (if it's a valid increment)


Forgetting that the upper limit of a range() isn’t included.
Iterating over non-sequences. Integer numbers aren’t iterable. Strings are iterable letter by letter, but that might not be what you want.
For loops are mostly used when there's a pre-defined sequence or range of numbers to iterate.



Break & Continue
You can interrupt both while and for loops using the break keyword. We normally do this to interrupt a cycle due to a separate condition.

You can use the continue keyword to skip the current iteration and continue with the next one. This is typically used to jump ahead when some of the elements of the sequence aren’t relevant.

If you want to learn more, check out this wiki page on for loops.'''





''' Python gives us three different ways to perform repetitive tasks while loops, for loops, and recursion. 
We use while loops when we want to do an operation while a certain condition is true or alternatively until it becomes false.
 We use for loops when we want to iterate over the elements of the sequence or a range of numbers. 
And we use recursion when the problem is best solved in smaller steps and then combining those steps towards a larger solution.'''




                ### while loop

'''The while loop requires relevant variables to be ready, in this example we need to define an indexing variable '''

i = 1
while (i<11) :                  # The while Loop -- With the while loop we can execute a set of statements as long as a condition is true.
    print (i)                   # remember to increment i, or else the loop will continue forever.
    i += 1                      # this += operator means a+new number. and eta jodi print er agei dei tahole i er value 1 show na kore 2 theke show krbe tai niche deya hoy while loop er khetre




i = 1
while i < 6:
  print(i)
  i += 1
else:                                       # With the else statement we can run a block of code once when the condition no longer is true:
  print("i is no longer less than 6")





i = 1
while i < 6 :
    print(i)
    if i == 3 :
        break                       # With the break statement we can stop the loop even if the while condition is true:
    i += 1                          # eta jodi print er agei dei tahole i er value 1 show na kore 2 theke show krbe tai niche deya hoy while loop er khetre




i = 0
while i < 6 :
  i += 1
  if i == 3 :                                # Continue to the next iteration if i is 3:
   	continue                                # With the continue statement we can stop the current iteration, and continue with the next:
  print(i)                                  # Note that number 3 is missing in the result.. In the loop, when i is 3, jump directly to the next iteration.







                ### for loop

'''Python For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, 
and works more like an iterator method as found in other object-orientated programming languages.
With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc. '''


fruits = ["apple", "banana", "cherry"]
for x in fruits:                           # The for loop does not require an indexing variable to set beforehand.
  print(x)


for x in "banana":                          # Even strings are iterable objects, they contain a sequence of characters:
  print(x)




for x in range(6):
  print(x)
else:
  print("Finally finished!")                # The else keyword in a for loop specifies a block of code to be executed when the loop is finished:



a = ['batting', 'bowling', 'keeping', 'fielding']
for x in a :
    print (x)                               # print(a) er output chaile setar ans jeta a te ache setai ashbe. e x  diye new variable er value ber korlam
    if x=='keeping' :                       # nicher break ta jodi print er aage ditam r print seshe ditam tahole output e keeping porjnto na eshe er ager ta porjjnto mane bowling porjnto ashto output
        break                               # With the break statement we can stop the loop before it has looped through all the items:



fruits = ['orange',"apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break                                   # break er por emn print dile output ta banana porjnto na eshe bananar agei sesh hbe APPLE ei
  print(x)




fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue                                # With the continue statement we can stop the current iteration of the loop, and continue with the next:
  print(x)




for x in range(6):                          # The range() Function -- To loop through a set of code a specified number of times, we can use the range() function,
  print(x)                                  # The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
                                            # Note that range(6) is not the values of 0 to 6, but the values 0 to 5.





for x in range(2, 6):                       # The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
  print(x)



for x in range(2, 30, 3):                       # The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
    print (x)                                   # output e 2 theke 30 porjnto sob ashbe but 3 gap kore kore. jmn 2,5,8,11 evabe




adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj :
  for y in fruits :                         # A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop":
    print(x, y)






for left in range(7):                                                   #nested loop example
    for right in range(left, 7):
        print("[" +str(left) + "|" + str(right) + "]", end = " ")
    print()







for x in [0, 1, 2]:                         # having an empty for loop like this, would raise an error without the pass statement.. 3 bar kore sob ashbe cz for loop dile oputput 3 bar ashe ektai jinish
    pass                                    # for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.