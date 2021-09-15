import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)			#Check if the string starts with  "The" and ends with "Spain":

if (x):
  print("YES! We have a match!")
else:
  print("No match")



'''RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

Function	Description
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string '''



'''
A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world.

The module re provides full support for Perl-like regular expressions in Python. The re module raises the exception re.error if an error occurs while compiling or using a regular expression.

We would cover two important functions, which would be used to handle regular expressions. Nevertheless, a small thing first: There are various characters, which would have special meaning when they are used in regular expression. To avoid any confusion while dealing with regular expressions, we would use Raw Strings as r'expression'.



Basic patterns that match single chars
Sr.No.	Expression & Matches
1	
a, X, 9, <

ordinary characters just match themselves exactly.

2	
. (a period)

matches any single character except newline '\n'

3	
\w

matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_].

4	
\W

matches any non-word character.

5	
\b

boundary between word and non-word

6	
\s

matches a single whitespace character -- space, newline, return, tab

7	
\S

matches any non-whitespace character.

8	
\t, \n, \r

tab, newline, return

9	
\d

decimal digit [0-9]

10	
^

matches start of the string

11	
$

match the end of the string

12	
\

inhibit the "specialness" of a character.




Compilation flags
Compilation flags let you modify some aspects of how regular expressions work. Flags are available in the re module under two names, a long name such as IGNORECASE and a short, one-letter form such as I.

Sr.No.	Flag & Meaning
1	
ASCII, A

Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.

2	
DOTALL, S

Make, match any character, including newlines

3	
IGNORECASE, I

Do case-insensitive matches

4	
LOCALE, L

Do a locale-aware match

5	
MULTILINE, M

Multi-line matching, affecting ^ and $

6	
VERBOSE, X (for ‘extended’)

Enable verbose REs, which can be organized more cleanly and understandably




The match Function
This function attempts to match RE pattern to string with optional flags.

Here is the syntax for this function −

re.match(pattern, string, flags = 0)




Here is the description of the parameters −

Sr.No.	Parameter & Description
1	
pattern

This is the regular expression to be matched.

2	
string

This is the string, which would be searched to match the pattern at the beginning of string.

3	
flags

You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.




The re.match function returns a match object on success, None on failure. We usegroup(num) or groups() function of match object to get matched expression.

Sr.No.	Match Object Method & Description
1	
group(num = 0)

This method returns entire match (or specific subgroup num)

2	
groups()

This method returns all matching subgroups in a tuple (empty if there weren't any)

Example
Live Demo
#!/usr/bin/python3
import re

line = "Cats are smarter than dogs"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
When the above code is executed, it produces the following result −

matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter




The search Function
This function searches for first occurrence of RE pattern within string with optional flags.





Here is the syntax for this function −

re.search(pattern, string, flags = 0)
Here is the description of the parameters −

Sr.No.	Parameter & Description
1	
pattern

This is the regular expression to be matched.

2	
string

This is the string, which would be searched to match the pattern anywhere in the string.

3	
flags

You can specify different flags using bitwise OR (|). These are modifiers, which are listed in the table below.



The re.search function returns a match object on success, none on failure. We use group(num) or groups() function of match object to get the matched expression.

Sr.No.	Match Object Method & Description
1	
group(num = 0)

This method returns entire match (or specific subgroup num)

2	
groups()

This method returns all matching subgroups in a tuple (empty if there weren't any)

Example
Live Demo
#!/usr/bin/python3
import re

line = "Cats are smarter than dogs";

searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)

if searchObj:
   print ("searchObj.group() : ", searchObj.group())
   print ("searchObj.group(1) : ", searchObj.group(1))
   print ("searchObj.group(2) : ", searchObj.group(2))
else:
   print ("Nothing found!!")



When the above code is executed, it produces the following result −

matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter




Matching Versus Searching
Python offers two different primitive operations based on regular expressions: match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string (this is what Perl does by default).


Example
Live Demo
#!/usr/bin/python3
import re

line = "Cats are smarter than dogs";

matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
   print ("match --> matchObj.group() : ", matchObj.group())
else:
   print ("No match!!")

searchObj = re.search( r'dogs', line, re.M|re.I)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!")


When the above code is executed, it produces the following result −

No match!!
search --> matchObj.group() :  dogs



Search and Replace
One of the most important re methods that use regular expressions is sub.

Syntax
re.sub(pattern, repl, string, max=0)
This method replaces all occurrences of the RE pattern in string with repl, substituting all occurrences unless max is provided. This method returns modified string.

Example
Live Demo
#!/usr/bin/python3
import re

phone = "2004-959-559 # This is Phone Number"

# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)
When the above code is executed, it produces the following result −

Phone Num :  2004-959-559
Phone Num :  2004959559
Regular Expression Modifiers: Option Flags
Regular expression literals may include an optional modifier to control various aspects of matching. The modifiers are specified as an optional flag. You can provide multiple modifiers using exclusive OR (|), as shown previously and may be represented by one of these −

Sr.No.	Modifier & Description
1	
re.I

Performs case-insensitive matching.

2	
re.L

Interprets words according to the current locale. This interpretation affects the alphabetic group (\w and \W), as well as word boundary behavior (\b and \B).

3	
re.M

Makes $ match the end of a line (not just the end of the string) and makes ^ match the start of any line (not just the start of the string).

4	
re.S

Makes a period (dot) match any character, including a newline.

5	
re.U

Interprets letters according to the Unicode character set. This flag affects the behavior of \w, \W, \b, \B.

6	
re.X

Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set [] or when escaped by a backslash) and treats unescaped # as a comment marker.

Regular Expression Patterns
Except for the control characters, (+ ? . * ^ $ ( ) [ ] { } | \), all characters match themselves. You can escape a control character by preceding it with a backslash.



The following table lists the regular expression syntax that is available in Python −




Here is the list of regular expression syntax in Python.
Regular Expression Examples
Literal characters
Sr.No.	Example & Description
1	
python

Match "python".

Character classes
Sr.No.	Example & Description
1	
[Pp]ython

Match "Python" or "python"

2	
rub[ye]

Match "ruby" or "rube"

3	
[aeiou]

Match any one lowercase vowel

4	
[0-9]

Match any digit; same as [0123456789]

5	
[a-z]

Match any lowercase ASCII letter

6	
[A-Z]

Match any uppercase ASCII letter

7	
[a-zA-Z0-9]

Match any of the above

8	
[^aeiou]

Match anything other than a lowercase vowel

9	
[^0-9]

Match anything other than a digit




Special Character Classes
Sr.No.	Example & Description
1	
.

Match any character except newline

2	
\d

Match a digit: [0-9]

3	
\D

Match a nondigit: [^0-9]

4	
\s

Match a whitespace character: [ \t\r\n\f]

5	
\S

Match nonwhitespace: [^ \t\r\n\f]

6	
\w

Match a single word character: [A-Za-z0-9_]

7	
\W

Match a nonword character: [^A-Za-z0-9_]




Repetition Cases
Sr.No.	Example & Description
1	
ruby?

Match "rub" or "ruby": the y is optional

2	
ruby*

Match "rub" plus 0 or more ys

3	
ruby+

Match "rub" plus 1 or more ys

4	
\d{3}

Match exactly 3 digits

5	
\d{3,}

Match 3 or more digits

6	
\d{3,5}

Match 3, 4, or 5 digits




Nongreedy repetition
This matches the smallest number of repetitions −

Sr.No.	Example & Description
1	
<.*>

Greedy repetition: matches "<python>perl>"

2	
<.*?>

Nongreedy: matches "<python>" in "<python>perl>"

Grouping with Parentheses
Sr.No.	Example & Description
1	
\D\d+

No group: + repeats \d

2	
(\D\d)+

Grouped: + repeats \D\d pair

3	
([Pp]ython(,)?)+

Match "Python", "Python, python, python", etc.




Backreferences
This matches a previously matched group again −

Sr.No.	Example & Description
1	
([Pp])ython&\1ails

Match python&pails or Python&Pails

2	
(['"])[^\1]*\1

Single or double-quoted string. \1 matches whatever the 1st group matched. \2 matches whatever the 2nd group matched, etc.




Alternatives
Sr.No.	Example & Description
1	
python|perl

Match "python" or "perl"

2	
rub(y|le)

Match "ruby" or "ruble"

3	
Python(!+|\?)

"Python" followed by one or more ! or one ?




Anchors
This needs to specify match position.

Sr.No.	Example & Description
1	
^Python

Match "Python" at the start of a string or internal line

2	
Python$

Match "Python" at the end of a string or line

3	
\APython

Match "Python" at the start of a string

4	
Python\Z

Match "Python" at the end of a string

5	
\bPython\b

Match "Python" at a word boundary

6	
\brub\B

\B is nonword boundary: match "rub" in "rube" and "ruby" but not alone

7	
Python(?=!)

Match "Python", if followed by an exclamation point.

8	
Python(?!!)

Match "Python", if not followed by an exclamation point.




Special Syntax with Parentheses
Sr.No.	Example & Description
1	
R(?#comment)

Matches "R". All the rest is a comment

2	
R(?i)uby

Case-insensitive while matching "uby"

3	
R(?i:uby)

Same as above

4	
rub(?:y|le))

Group only without creating \1 backreference'''





'''The Match object has properties and methods used to retrieve information about the search, and the result:
search	    Returns a Match object if there is a match anywhere in the string

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match





Metacharacters
Metacharacters are characters with a special meaning:

[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"world$"	
*	Zero or more occurrences	"aix*"	
+	One or more occurrences	"aix+"	
{}	Exactly the specified number of occurrences	"al{2}"	
|	Either or	"falls|stays"	
()	Capture and group	




 	 
Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain" r"ain\b"	
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain" r"ain\B"	
\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	





Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:

[arn]	Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
	
	
	
	
	
	
	
	Python provides two very important features to handle any unexpected error in your Python programs and to add debugging capabilities in them −

Exception Handling − This would be covered in this tutorial. Here is a list standard Exceptions available in Python − Standard Exceptions.

Assertions − This would be covered in Assertions in Python 3 tutorial.




Standard Exceptions
Here is a list of Standard Exceptions available in Python. −

Sr.No.	Exception Name & Description
1	
Exception

Base class for all exceptions

2	
StopIteration

Raised when the next() method of an iterator does not point to any object.

3	
SystemExit

Raised by the sys.exit() function.

4	
StandardError

Base class for all built-in exceptions except StopIteration and SystemExit.

5	
ArithmeticError

Base class for all errors that occur for numeric calculation.

6	
OverflowError

Raised when a calculation exceeds maximum limit for a numeric type.

7	
FloatingPointError

Raised when a floating point calculation fails.

8	
ZeroDivisonError

Raised when division or modulo by zero takes place for all numeric types.

9	
AssertionError

Raised in case of failure of the Assert statement.

10	
AttributeError

Raised in case of failure of attribute reference or assignment.

11	
EOFError

Raised when there is no input from either the raw_input() or input() function and the end of file is reached.

12	
ImportError

Raised when an import statement fails.

13	
KeyboardInterrupt

Raised when the user interrupts program execution, usually by pressing Ctrl+c.

14	
LookupError

Base class for all lookup errors.

15	
IndexError

Raised when an index is not found in a sequence.

16	
KeyError

Raised when the specified key is not found in the dictionary.

17	
NameError

Raised when an identifier is not found in the local or global namespace.

18	
UnboundLocalError

Raised when trying to access a local variable in a function or method but no value has been assigned to it.

19	
EnvironmentError

Base class for all exceptions that occur outside the Python environment.

20	
IOError

Raised when an input/ output operation fails, such as the print statement or the open() function when trying to open a file that does not exist.

21	
OSError

Raised for operating system-related errors.

22	
SyntaxError

Raised when there is an error in Python syntax.

23	
IndentationError

Raised when indentation is not specified properly.

24	
SystemError

Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.

25	
SystemExit

Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit.

26	
TypeError

Raised when an operation or function is attempted that is invalid for the specified data type.

27	
ValueError

Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified.

28	
RuntimeError

Raised when a generated error does not fall into any category.

29	
NotImplementedError

Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented.

Assertions in Python
An assertion is a sanity-check that you can turn on or turn off when you are done with your testing of the program.

The easiest way to think of an assertion is to liken it to a raise-if statement (or to be more accurate, a raise-if-not statement). An expression is tested, and if the result comes up false, an exception is raised.

Assertions are carried out by the assert statement, the newest keyword to Python, introduced in version 1.5.

Programmers often place assertions at the start of a function to check for valid input, and after a function call to check for valid output.

The assert Statement
When it encounters an assert statement, Python evaluates the accompanying expression, which is hopefully true. If the expression is false, Python raises an AssertionError exception.

The syntax for assert is −

assert Expression[, Arguments]
If the assertion fails, Python uses ArgumentExpression as the argument for the AssertionError. AssertionError exceptions can be caught and handled like any other exception, using the try-except statement. If they are not handled, they will terminate the program and produce a traceback.

Example
Here is a function that converts a given temperature from degrees Kelvin to degrees Fahrenheit. Since 0° K is as cold as it gets, the function bails out if it sees a negative temperature −

Live Demo
#!/usr/bin/python3

def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

print (KelvinToFahrenheit(273))
print (int(KelvinToFahrenheit(505.78)))
print (KelvinToFahrenheit(-5))
When the above code is executed, it produces the following result −

32.0
451
Traceback (most recent call last):
File "test.py", line 9, in <module>
print KelvinToFahrenheit(-5)
File "test.py", line 4, in KelvinToFahrenheit
assert (Temperature >= 0),"Colder than absolute zero!"
AssertionError: Colder than absolute zero!'''




