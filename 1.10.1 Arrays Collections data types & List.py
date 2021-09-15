'''Python Collections (Arrays)
There are four collection data types in the Python programming language:
    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered and unindexed. No duplicate members.
    Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
When choosing a collection type, it is useful to understand the properties of that type.
Choosing the right type for a particular data set could mean retention of meaning,
and, it could mean an increase in efficiency or security.'''



          ### A list is a collection which is ordered and changeable. In Python lists are written with square brackets/ 3rd brackets.


x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print (x)

print(len(x))                               # To determine how many items a list has, use the len() function:

print (x[3])                                # we can access the list items by referring to the index number: binary number wise 0 theke started
print (x[-3])                               # Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc

print (x[2:5])                              # Return the third, fourth, and fifth item: ... Remember that the first item is position 0, and note that the item in position 5 is NOT included..this is Range of Indexes. You can specify a range of indexes by specifying where to start and where to end the range. When specifying a range, the return value will be a new list with the specified items.
print (x[:4])                               # Remember that index 0 is the first item, and index 4 is the fifth item..Remember that the item in index 4 is NOT included.. so,This will return the items from index 0 to index 4.
print (x[2:])                               # This will return the items from index 2 to the end.. Remember that index 0 is the first item, and index 2 is the third

print (x[-5:-2])                            # Negative indexing means starting from the end of the list. This example returns the items from index -5 (included) to index -2 (excluded).. Remember that the last item has the index -2,
print (x[-5:])                              # this example returns the items from index -5 (included) and then -1 = mango porjnto. - dilei end list er ta 1st e count hoy jani amra
print (x[:-2])                              # ekhane last e -2 deyay rules wise kiwi tei thambe but start hbe 0 means apple theke cause etay start neg na positive theke jehetu : etar age kichui nai


x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
x[4] = 'grape'                              # kiwi er bodole nicher print output tay 'grape' ditei ei variable cl kora holo index system er
print (x)                                   # To change the value of a specific item, refer to the index number:


x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for y in x:                                 # loop through the list items by using a for loop:..  x er value toh deya achei sekhane y namer value in korte hole in er sthe agei evabe for loop use krte hbe.
    print (y)                               # loop ta use koray ekhane print er aage space or indentation ditei hbe


x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if 'Blackberry' in x:                       # To determine if a specified item is present in a list use the in keyword:.
    print ('Yes')                           # evabe chaile if else condition statement ow use kora jay. for, if, else egulor pore must be : ei colon ditei hoy nahoy run hbena
else:
    print('No')




x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

x.append('BlueBerry')                       # to add an item to the end of the list, use the append() method:
print (x)

x.insert(2, 'RaspBerry')                    # To add an item at the specified index, use the insert() method:
print (x)




x = list(("apple", "banana", "cherry"))     # It is also possible to use the list() constructor to make a new list.
print(x)



x = ["apple", "banana", "cherry"]
mylist = list(x)                            # Another way to make a copy is to use the built-in method list(). to another new variable
print (x)
print (mylist)



x = ["apple", "banana", "cherry"]
mylist = x.copy()                           # Make a copy of a list with the copy() method:
print (x)
print(mylist)



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2                        # There are several ways to join, or concatenate, two or more lists in Python.
print(list3)                                 # One of the easiest ways are by using the + operator.



list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)                            # Another way to join two lists are by appending all the items from list2 into list1, one by one:
print(list1)



list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)                          # Or you can use the extend() method, which purpose is to add elements from one list to another list:  Use the extend() method to add list2 at the end of list1:
print(list1)




x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

x.remove('apple')                            # The remove() method removes the specified item:
print(x)

x.pop()                                      # The pop() method removes the specified index, (or the last item if index is not specified):
print(x)

del x[2]                                     # The del keyword removes the specified index:
print (x)

x.clear()                                    # The clear() method empties the list: and returns []
print (x)

x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
del x                                        # this will cause an error at last or in start at the runtime. because you have succsesfully deleted "thislist".
print (x)





'''


Lists and Tuples Operations Cheat Sheet
Lists and Tuples Operations Cheat Sheet
Lists and tuples are both sequences, 
so they share a number of sequence operations. But, because lists are mutable, 
there are also a number of methods specific just to lists. 
This cheat sheet gives you a run down of the common operations first, and the list-specific operations second.


Common sequence operations
len(sequence) Returns the length of the sequence
for element in sequence Iterates over each element in the sequence
if element in sequence Checks whether the element is part of the sequence
sequence[i] Accesses the element at index i of the sequence, starting at zero
sequence[i:j] Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.
for index, element in enumerate(sequence) Iterates over both the indexes and the elements in the sequence at the same time
Check out the official documentation for sequence operations.



List-specific operations and methods

list[i] = x Replaces the element at index i with x
list.append(x) Inserts x at the end of the list
list.insert(i, x) Inserts x at index i
list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
list.remove(x) Removes the first occurrence of x in the list
list.sort() Sorts the items in the list
list.reverse() Reverses the order of items of the list
list.clear() Removes all the items of the list
list.copy() Creates a copy of the list
list.extend(other_list) Appends all the elements of other_list at the end of list
Most of these methods come from the fact that lists are mutable sequences. For more info, see the official documentation for mutable sequences and the list specific documentation.



List comprehension
[expression for variable in sequence] Creates a new list based on the given sequence. Each element is the result of the given expression.
[expression for variable in sequence if condition] Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true.


List Comprehensions
You can create lists from sequences using a for loop, but there’s a more streamlined way to do this: list comprehension.
 List comprehensions allow you to create a new list from a sequence or a range in a single line.

For example, [ x*2 for x in range(1,11) ] is a simple list comprehension. 
This would iterate over the range 1 to 10, and multiply each element in the range by 2. 
This would result in a list of the multiples of 2, from 2 to 20.

You can also use conditionals with list comprehensions to build even more complex and powerful statements. 
You can do this by appending an if statement to the end of the comprehension.
 For example, [ x for x in range(1,101) if x % 10 == 0 ] would generate a list containing all the integers divisible by 10 from 1 to 100. 
 The if statement we added here evaluates each value in the range from 1 to 100 to check if it’s evenly divisible by 10. If it is, it gets added to the list.

List comprehensions can be really powerful, but they can also be super complex, resulting in code that’s hard to read.
Be careful when using them, since it might make it more difficult for someone else looking at your code to easily understand what the code is doing.



Python has a set of built-in methods that you can use on lists.

    append()	    Adds an element at the end of the list
    clear()	        Removes all the elements from the list
    copy()	        Returns a copy of the list
    count()	        Returns the number of elements with the specified value
    extend()	    Add the elements of a list (or any iterable), to the end of the current list
    index()	        Returns the index of the first element with the specified value
    insert()    	Adds an element at the specified position
    pop()	        Removes the element at the specified position
    remove()	    Removes the item with the specified value
    reverse()	    Reverses the order of the list
    sort()	        Sorts the list
     
     
     
     
   
     
     Basic List Operations
Lists respond to the + and * operators much like strings; they mean concatenation and repetition here too, except that the result is a new list, not a string.

In fact, lists respond to all of the general sequence operations we used on strings in the prior chapter.

Python Expression	Results	Description
len([1, 2, 3])	3	Length
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	Concatenation
['Hi!'] * 4	['Hi!', 'Hi!', 'Hi!', 'Hi!']	Repetition
3 in [1, 2, 3]	True	Membership
for x in [1,2,3] : print (x,end = ' ')	1 2 3	Iteration




Indexing, Slicing and Matrixes
Since lists are sequences, indexing and slicing work the same way for lists as they do for strings.

Assuming the following input −

L = ['C++'', 'Java', 'Python']
Python Expression	Results	Description
L[2]	'Python'	Offsets start at zero
L[-2]	'Java'	Negative: count from the right
L[1:]	['Java', 'Python']	Slicing fetches sections





Built-in List Functions and Methods
Python includes the following list functions −

Sr.No.	Function & Description
1	len(list)
Gives the total length of the list.

2	max(list)
Returns item from the list with max value.

3	min(list)
Returns item from the list with min value.

4	list(seq)
Converts a tuple into list.

Python includes the following list methods −

Sr.No.	Methods & Description
1	list.append(obj)
Appends object obj to list

2	list.count(obj)
Returns count of how many times obj occurs in list

3	list.extend(seq)
Appends the contents of seq to list

4	list.index(obj)
Returns the lowest index in list that obj appears

5	list.insert(index, obj)
Inserts object obj into list at offset index

6	list.pop(obj = list[-1])
Removes and returns last object or obj from list

7	list.remove(obj)
Removes object obj from list

8	list.reverse()
Reverses objects of list in place

9	list.sort([func])
Sorts objects of list, use compare func if given









Basic Tuples Operations
Tuples respond to the + and * operators much like strings; they mean concatenation and repetition here too, except that the result is a new tuple, not a string.

In fact, tuples respond to all of the general sequence operations we used on strings in the previous chapter.

Python Expression	Results	Description
len((1, 2, 3))	3	Length
(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	Concatenation
('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	Repetition
3 in (1, 2, 3)	True	Membership
for x in (1,2,3) : print (x, end = ' ')	1 2 3	Iteration
Indexing, Slicing, and Matrixes
Since tuples are sequences, indexing and slicing work the same way for tuples as they do for strings, assuming the following input −

T=('C++', 'Java', 'Python')
Python Expression	Results	Description
T[2]	'Python'	Offsets start at zero
T[-2]	'Java'	Negative: count from the right
T[1:]	('Java', 'Python')	Slicing fetches sections
No Enclosing Delimiters
No enclosing Delimiters is any set of multiple objects, comma-separated, written without identifying symbols, i.e., brackets for lists, parentheses for tuples, etc., default to tuples, as indicated in these short examples.

Built-in Tuple Functions
Python includes the following tuple functions −

Sr.No.	Function & Description
1	cmp(tuple1, tuple2)
Compares elements of both tuples.

2	len(tuple)
Gives the total length of the tuple.

3	max(tuple)
Returns item from the tuple with max value.

4	min(tuple)
Returns item from the tuple with min value.

5	tuple(seq)
Converts a list into tuple.









Built-in Dictionary Functions and Methods
Python includes the following dictionary functions −

Sr.No.	Function & Description
1	cmp(dict1, dict2)
No longer available in Python 3.

2	len(dict)
Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.

3	str(dict)
Produces a printable string representation of a dictionary

4	type(variable)
Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.





Python includes the following dictionary methods −

Sr.No.	Method & Description
1	dict.clear()
Removes all elements of dictionary dict

2	dict.copy()
Returns a shallow copy of dictionary dict

3	dict.fromkeys()
Create a new dictionary with keys from seq and values set to value.

4	dict.get(key, default=None)
For key key, returns value or default if key not in dictionary

5	dict.has_key(key)
Removed, use the in operation instead.

6	dict.items()
Returns a list of dict's (key, value) tuple pairs

7	dict.keys()
Returns list of dictionary dict's keys

8	dict.setdefault(key, default = None)
Similar to get(), but will set dict[key] = default if key is not already in dict

9	dict.update(dict2)
Adds dictionary dict2's key-values pairs to dict

10	dict.values()
Returns list of dictionary dict's values






A Python program can handle date and time in several ways. Converting between date formats is a common chore for computers. Python's time and calendar modules help track dates and times.




What is Tick?
Time intervals are floating-point numbers in units of seconds. Particular instants in time are expressed in seconds since 12:00am, January 1, 1970(epoch).

There is a popular time module available in Python which provides functions for working with times, and for converting between representations. The function time.time() returns the current system time in ticks since 12:00am, January 1, 1970(epoch).

Example
Live Demo
#!/usr/bin/python3
import time;      # This is required to include time module.

ticks = time.time()
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
This would produce a result something as follows −

Number of ticks since 12:00am, January 1, 1970: 1455508609.34375
Date arithmetic is easy to do with ticks. However, dates before the epoch cannot be represented in this form. Dates in the far future also cannot be represented this way - the cutoff point is sometime in 2038 for UNIX and Windows.




What is TimeTuple?
Many of the Python's time functions handle time as a tuple of 9 numbers, as shown below −

Index	Field	Values
0	4-digit year	2016
1	Month	1 to 12
2	Day	1 to 31
3	Hour	0 to 23
4	Minute	0 to 59
5	Second	0 to 61 (60 or 61 are leap-seconds)
6	Day of Week	0 to 6 (0 is Monday)
7	Day of year	1 to 366 (Julian day)
8	Daylight savings	-1, 0, 1, -1 means library determines DST



For Example −

Live Demo
import time

print (time.localtime());
This would produce a result as follows −

time.struct_time(tm_year = 2016, tm_mon = 2, tm_mday = 15, tm_hour = 9, 
   tm_min = 29, tm_sec = 2, tm_wday = 0, tm_yday = 46, tm_isdst = 0)



The above tuple is equivalent to struct_time structure. This structure has following attributes −

Index	Attributes	Values
0	tm_year	2016
1	tm_mon	1 to 12
2	tm_mday	1 to 31
3	tm_hour	0 to 23
4	tm_min	0 to 59
5	tm_sec	0 to 61 (60 or 61 are leap-seconds)
6	tm_wday	0 to 6 (0 is Monday)
7	tm_yday	1 to 366 (Julian day)
8	tm_isdst	-1, 0, 1, -1 means library determines DST
Getting current time
To translate a time instant from seconds since the epoch floating-point value into a timetuple, pass the floating-point value to a function (e.g., localtime) that returns a time-tuple with all valid nine items.




Live Demo
#!/usr/bin/python3
import time

localtime = time.localtime(time.time())
print ("Local current time :", localtime)
This would produce the following result, which could be formatted in any other presentable form −

Local current time : time.struct_time(tm_year = 2016, tm_mon = 2, tm_mday = 15, 
   tm_hour = 9, tm_min = 29, tm_sec = 2, tm_wday = 0, tm_yday = 46, tm_isdst = 0)
Getting formatted time
You can format any time as per your requirement, but a simple method to get time in a readable format is asctime() −




Live Demo
#!/usr/bin/python3
import time

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
This would produce the following result −

Local current time : Mon Feb 15 09:34:03 2016
Getting calendar for a month
The calendar module gives a wide range of methods to play with yearly and monthly calendars. Here, we print a calendar for a given month ( Jan 2008 ) −




Live Demo
#!/usr/bin/python3
import calendar

cal = calendar.month(2016, 2)
print ("Here is the calendar:")
print (cal)
This would produce the following result −

Here is the calendar:
   February 2016
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29




The time Module
There is a popular time module available in Python, which provides functions for working with times and for converting between representations. Here is the list of all available methods.

Sr.No.	Function & Description
1	time.altzone
The offset of the local DST timezone, in seconds west of UTC, if one is defined. This is negative if the local DST timezone is east of UTC (as in Western Europe, including the UK). Use this if the daylight is nonzero.

2	time.asctime([tupletime])
Accepts a time-tuple and returns a readable 24-character string such as 'Tue Dec 11 18:07:14 2008'.

3	time.clock( )
Returns the current CPU time as a floating-point number of seconds. To measure computational costs of different approaches, the value of time.clock is more useful than that of time.time().

4	time.ctime([secs])
Like asctime(localtime(secs)) and without arguments is like asctime( )

5	time.gmtime([secs])
Accepts an instant expressed in seconds since the epoch and returns a time-tuple t with the UTC time. Note − t.tm_isdst is always 0

6	time.localtime([secs])
Accepts an instant expressed in seconds since the epoch and returns a time-tuple t with the local time (t.tm_isdst is 0 or 1, depending on whether DST applies to instant secs by local rules).

7	time.mktime(tupletime)
Accepts an instant expressed as a time-tuple in local time and returns a floating-point value with the instant expressed in seconds since the epoch.

8	time.sleep(secs)
Suspends the calling thread for secs seconds.

9	time.strftime(fmt[,tupletime])
Accepts an instant expressed as a time-tuple in local time and returns a string representing the instant as specified by string fmt.

10	time.strptime(str,fmt = '%a %b %d %H:%M:%S %Y')
Parses str according to format string fmt and returns the instant in time-tuple format.

11	time.time( )
Returns the current time instant, a floating-point number of seconds since the epoch.

12	time.tzset()
Resets the time conversion rules used by the library routines. The environment variable TZ specifies how this is done.

There are two important attributes available with time module. They are −

Sr.No.	Attribute & Description
1	
time.timezone

Attribute time.timezone is the offset in seconds of the local time zone (without DST) from UTC (>0 in the Americas; <=0 in most of Europe, Asia, Africa).

2	
time.tzname

Attribute time.tzname is a pair of locale-dependent strings, which are the names of the local time zone without and with DST, respectively.

The calendar Module
The calendar module supplies calendar-related functions, including functions to print a text calendar for a given month or year.

By default, calendar takes Monday as the first day of the week and Sunday as the last one. To change this, call the calendar.setfirstweekday() function.






Here is a list of functions available with the calendar module −

Sr.No.	Function & Description
1	
calendar.calendar(year,w = 2,l = 1,c = 6)

Returns a multiline string with a calendar for year year formatted into three columns separated by c spaces. w is the width in characters of each date; each line has length 21*w+18+2*c. l is the number of lines for each week.

2	
calendar.firstweekday( )

Returns the current setting for the weekday that starts each week. By default, when calendar is first imported, this is 0, meaning Monday.

3	
calendar.isleap(year)

Returns True if year is a leap year; otherwise, False.

4	
calendar.leapdays(y1,y2)

Returns the total number of leap days in the years within range(y1,y2).

5	
calendar.month(year,month,w = 2,l = 1)

Returns a multiline string with a calendar for month month of year year, one line per week plus two header lines. w is the width in characters of each date; each line has length 7*w+6. l is the number of lines for each week.

6	
calendar.monthcalendar(year,month)

Returns a list of lists of ints. Each sublist denotes a week. Days outside month month of year year are set to 0; days within the month are set to their day-of-month, 1 and up.

7	
calendar.monthrange(year,month)

Returns two integers. The first one is the code of the weekday for the first day of the month month in year year; the second one is the number of days in the month. Weekday codes are 0 (Monday) to 6 (Sunday); month numbers are 1 to 12.

8	
calendar.prcal(year,w = 2,l = 1,c = 6)

Like print calendar.calendar(year,w,l,c).

9	
calendar.prmonth(year,month,w = 2,l = 1)

Like print calendar.month(year,month,w,l).

10	
calendar.setfirstweekday(weekday)

Sets the first day of each week to weekday code weekday. Weekday codes are 0 (Monday) to 6 (Sunday).

11	
calendar.timegm(tupletime)

The inverse of time.gmtime: accepts a time instant in time-tuple form and returns the same instant as a floating-point number of seconds since the epoch.

12	
calendar.weekday(year,month,day)

Returns the weekday code for the given date. Weekday codes are 0 (Monday) to 6 (Sunday); month numbers are 1 (January) to 12 (December).





Other Modules and Functions
If you are interested, then here you would find a list of other important modules and functions to play with date & time in Python −

The datetime Module
The pytz Module
The dateutil Module

'''