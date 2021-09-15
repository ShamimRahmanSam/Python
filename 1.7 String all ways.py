'''Basic String Methods
In Python, strings are immutable. This means that they can't be modified. So if we wanted to fix a typo in a string, we can't simply modify the wrong character. We would have to create a new string with the typo corrected. We can also assign a new value to the variable holding our string.

If we aren't sure what the index of our typo is, we can use the string method index to locate it and return the index.
 Let's imagine we have the string "lions tigers and bears" in the variable animals.
 We can locate the index that contains the letter g using animals.index("g"),
 which will return the index; in this case 8. We can also use substrings to locate the index where the substring begins.
  animals.index("bears") would return 17, since that’s the start of the substring.
   If there’s more than one match for a substring,
the index method will return the first match.
If we try to locate a substring that doesn't exist in the string,
we’ll receive a ValueError explaining that the substring was not found.

We can avoid a ValueError by first checking if the substring exists in the string.
This can be done using the in keyword. We saw this keyword earlier when we covered for loops.
In this case, it's a conditional that will be either True or False. If the substring is found in the string,
it will be True. If the substring is not found in the string, it will be False. Using our previous variable animals,
we can do "horses" in animals to check if the substring "horses" is found in our variable.
 In this case, it would evaluate to False, since horses aren’t included in our example string.
  If we did "tigers" in animals, we'd get True, since this substring is contained in our string.




  Advanced String Methods
We've covered a bunch of String class methods already,
 so let's keep building on those and run down some more advanced methods.

The string method lower will return the string with all characters changed to lowercase.
The inverse of this is the upper method, which will return the string all in uppercase.
 Just like with previous methods, we call these on a string using dot notation, like "this is a string".upper().
 This would return the string "THIS IS A STRING".
  This can be super handy when checking user input, since someone might type in all lowercase, all uppercase, or even a mixture of cases.

You can use the strip method to remove surrounding whitespace from a string. Whitespace includes spaces, tabs, and newline characters.
You can also use the methods  lstrip and rstrip to remove whitespace only from the left or the right side of the string, respectively.

The method count can be used to return the number of times a substring appears in a string.
 This can be handy for finding out how many characters appear in a string, or counting the number of times a certain word appears in a sentence or paragraph.

If you wanted to check if a string ends with a given substring, you can use the method endswith.
This will return True if the substring is found at the end of the string, and False if not.

The isnumeric method can check if a string is composed of only numbers.
If the string contains only numbers, this method will return True.
We can use this to check if a string contains numbers before passing the string to the int() function to convert it to an integer, avoiding an error. Useful!

We took a look at string concatenation using the plus sign, earlier. We can also use the join method to concatenate strings.
 This method is called on a string that will be used to join a list of strings. The method takes a list of strings to be joined as a parameter,
  and returns a new string composed of each of the strings from our list joined using the initial string.
  For example, " ".join(["This","is","a","sentence"]) would return the string "This is a sentence".

The inverse of the join method is the split method. This allows us to split a string into a list of strings.
By default, it splits by any whitespace characters. You can also split by any other characters by passing a parameter.






String Reference Cheat Sheet
String Reference Cheat Sheet
In Python, there are a lot of things you can do with strings. In this cheat sheet, you’ll find the most common string operations and string methods.

String operations
len(string) Returns the length of the string
for character in string Iterates over each character in the string
if substring in string Checks whether the substring is part of the string
string[i] Accesses the character at index i of the string, starting at zero
string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.
String methods
string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
string.count(substring) Returns the number of times substring is present in the string
string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter
Check out the official documentation for all available String methods.




Formatting expressions
Expr	Meaning	Example
{:d}	integer value	'{:d}'.format(10.5) → '10'
{:.2f}	floating point with that many decimals	'{:.2f}'.format(0.5) → '0.50'
{:.2s}	string with that many characters	'{:.2s}'.format('Python') → 'Py'
{:<6s}	string aligned to the left that many spaces	'{:<6s}'.format('Py') → 'Py    '
{:>6s}	string aligned to the right that many spaces	'{:>6s}'.format('Py') → '    Py'
{:^6s}	string centered in that many spaces	'{:^6s}'.format('Py') → '  Py '






Old string formatting (Optional)
The format() method was introduced in Python 2.6. Before that, the % (modulo) operator could be used to get a similar result. While this method is no longer recommended for new code, you might come across it in someone else's code. This is what it looks like:

"base string with %s placeholder" % variable

The % (modulo) operator returns a copy of the string where the placeholders indicated by %  followed by a formatting expression are replaced by the variables after the operator.

"base string with %d and %d placeholders" % (value1, value2)

To replace more than one value, the values need to be written between parentheses. The formatting expression needs to match the value type.

"%(var1) %(var2)" % {var1:value1, var2:value2}

Variables can be replaced by name using a dictionary syntax (we’ll learn about dictionaries in an upcoming video).

"Item: %s - Amount: %d - Price: %.2f" % (item, amount, price)

The formatting expressions are mostly the same as those of the format() method.

Check out the official documentation for old string formatting.

Formatted string literals (Optional)
This feature was added in Python 3.6 and isn’t used a lot yet. Again, it's included here in case you run into it in the future, but it's not needed for this or any upcoming courses.

A formatted string literal or f-string is a string that starts with 'f' or 'F' before the quotes. These strings might contain {} placeholders using expressions like the ones used for format method strings.

The important difference with the format method is that it takes the value of the variables from the current context, instead of taking the values from parameters.

Examples:

>>> name = "Micah"

>>> print(f'Hello {name}')

Hello Micah

>>> item = "Purple Cup"

>>> amount = 5

>>> price = amount * 3.25

>>> print(f'Item: {item} - Amount: {amount} - Price: {price:.2f}')

Item: Purple Cup - Amount: 5 - Price: 16.25

Check out the official documentation for f-strings.


'''





print('ja mon chay evabei lekha jay words or characters or anything we wanted to see in output')


a = 'Shamim Rahman Sam'                              # evabei ' ' / "  " er moddhe words character egulo deya jay easily. onno language er mto pera nai string niye
print (a)                                            # evabe easily variable call kore output pawa jay


a = '''evabe ja mon chay print kora jay 
line breaks korei emn
and ja mo chay evabe lekha jay
poetry design e xD ei single quotation 3 ta 
or double quotation 3 bar use kore aage r pore emn'''
print (a)                                            # aager variable a ei output tay prob na korar reason holo agaer ta agei output ber kora hoise print diye XD  nicher gulateo same variable thakleo prob hbena jodi putput seta agei ber hoy print kore


a = 'hgauGsuguwgdasdKsdiuawgd7HK'
print(a[1])                                          # evabe nirdishto ekta ber kora jay. 0 theke binary count kore tai 4 e G ashche s na eshe


a = 'fjhdufhdifhieshfkqwnfwjkgf7uwtgfwikfnhi'
print(a[:])                                          # just : use koray sob ashche output e and 0: dileo same shob ashto but 1/2 or jekono number dile setar theke ouput ashto jmn nicher ta


a = 'jkshASkfhisjfisfiosdjfioe8sfwienr'
print(a[5:])                                         # etate S ashche evabe jekono number use korle setar por theke ashbe bu8t ending number dile :  etar por then sekhanei sesh hbe just like slicing way xD

a =  'jhdSishfiesjfglehfMtMgriesofe8tgweknrewhf'
print(a[3:19])                                       # emn vabei ending e number dile setar agei sesh hobe ouput


a =  'dja6ihfpsfosdfiokhsduSfhidsf9sf5'
print(a[-17:-3])                                     # evabe negative way te ulto output ow sob way te ber kora jabe,.. but ekhane arekside - er bodole + dile outpout ektu onnorokm ashto


a = 'sjhduhfkslfmiosuf8hdlsamdoiasdsahdsmd9osayfi'
print(len(a))                                        # len use kore jekono string er length ber korte parbo emn



a = 'DSJKDBSFHSjdgsudsfnioHUIDHFIKSDHFI  OSHFKjkhkdsfikfhFYUDSKLISDEHFUSBD,MSADS'
print(a.lower())                                     # ei lower use korle sob capital gulo lower case hoye jabe

txt = "hello world! 123"
print(txt.islower())                                 # sob small thkle true bolbe nahoy false... r hae number dile doesn't fact



a = 'jkdshfiuefkdnfkshdhawjed ajkdehawihdasjkJKBUHDSIHIK  SDHFIUWJKbajhuhdidsjgidjhfuisgdjjqaniofhxdifhijkhiuIQJ'
print(a.upper())                                     # ei lower r upper e jodi ilower r isupper dei tahole output e eta bolbe j sob lower naki upper true false output diye. seta arek data type

a = 'GHDNJD 324'
print (a.isupper())                                  # shob upper naki eta bujhate.. ekhaneoo  number doesn't fact



a = 't.R.Sam'
print(a.replace('t','S'))                            # replace korte emn krte hoy.,. but same letter thakle setar age 0/1/2 egulo use kore kaj krle different output ta ashbe

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)



txt = "We are the so-called 'Vikings' from the north."
print(txt)                                          # we will get an error if you use double quotes inside a string that are surrounded by double quotes/single quotes..


txt = "We are the so-called \"Vikings\" from the north."
print(txt)                                          # same single or double quotes use korle tokhon bachar jnne emn \ ei slash use krte hbe emn age r pore


txt = 'It\'s alright.'
print(txt)                                          # evabe same single quotes use korle emn way tei krte hoy


txt = "This will insert one \\ (backslash)."        # blackslash double dile ekta show hbe
print(txt)


txt = "Hello\nWorld!"                               # new line \n use krte hoy c programming lang er mto
print(txt)


txt = "Hello\rWorld!"                               # etaw new line create hoy but in here etay ager ta baad hoye jay r porer ta thake output e r diyeo jodi ki na carriage return bujhay..
print(txt)


txt = "Hello\tWorld!"
print(txt)                                          # ouput e tab wise pete \t use kora hoy


txt = "Hello \bWorld!"                              # This example erases one character (backspace): r 1 tar beshi \b dile ekhane ovabei 1 ta kore alphabet slice hoye baad jabe...and 1 tar beshi space dile tokhn 5 ta soace dile 4 ta space khali theke output ashbe ..
print(txt)


txt = "Hello \f World!"                             # \f dile ekta form ashe
print(txt)


txt = "\110\145\154\154\157"                        # A backslash followed by three integers will result in a octal value:
print(txt)


txt = "\110\145\154\154\157"                        # A backslash followed by three integers will result in a octal value: \ooo
print(txt)


txt = "\x48\x65\x6c\x6c\x6f"                        # A backslash followed by an 'x' and a hex number represents a hex value: xhh
print(txt)


txt = "H\te\tl\tl\to"                               # A number specifying the tabsize. Default tabsize is 8. ekhane 4 ta space nise jjayga idk why
x =  txt.expandtabs(3)                              # evabe variable.expandtabs(number) dile toto ta space hoy output but upre must be prottekk alphabet er por \t agei use krte hbe. nahoy ashbena output. r ei type ta use na kore uprer \t diye evabe likhle output e emn space auto e ashe 4/5 ta space diye
print(x)                                            # evabe variable mna niye nicher mto direct korai better
print(txt)
print(txt.expandtabs())                             # etay uprer tar mto output ashbe.. eta dile default size  8 tai hoy
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))


txt = "Hello, welcome to my world."
print (txt.endswith("my world."))                   # The endswith() method returns True if the string ends with the specified value, otherwise False.. ekhane onnno kiichu andaje dile or bhul dile output false ashto. r etar mto thik diyeo , comma diye then onno kichu dile jeta nai string tay tmn kichu dileo false e show krbe output.


txt = "My name is Ståle"
print(txt.encode())                                              # UTF-8 encode the string:
print(txt.encode(encoding="ascii",errors="backslashreplace"))    # uses a backslash instead of the character that could not be encoded
print(txt.encode(encoding="ascii",errors="ignore"))              # ignores the characters that cannot be encoded
print(txt.encode(encoding="ascii",errors="namereplace"))         # replaces the character with a text explaining the character
print(txt.encode(encoding="ascii",errors="replace"))             # replaces the character with a questionmark
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))   # replaces the character with an xml character
# print(txt.encode(encoding="ascii",errors="strict"))            # Default, raises an error on failure tai etar output e ashena baki uprer gula diffrent ashleo


txt = "I love apples, apples are my favorite fruit"
print(txt.count("apples", 5))                                    # count dile emn count kore ktobar ase + bengal scientist etaw bujhe j onno words string  hisebe dile output er jnne then ura. r erpor nmbr dile kmn hoynjha ta output ei dkhtsi


txt = "banana"
print(txt.center(50))                                            # Print the word "banana", taking up the space of 50 characters, with "banana" in the middle:


txt = "banana"
print(txt.center(20, "O"))                                       # check out the output..Using the letter "O" as the padding character:


txt = "Hello, And Welcome To My World!"
print(txt.casefold())                                            # Make the string lower case: just like lower data type of string.. This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.


txt = "hello, and welcome to my world."
print (txt.capitalize())                                         # just like upper types. just first alphabet tai capital banay.. See what happens if the first character is a number: hahah same tai ashe reply.. cz number capital hyna xD


a = "\u0033"                                                     # unicode for 3
b = "\u0047"                                                     # unicode for G
print(a.isdecimal())                                             # decimal hole true r na hole false ashbe result niher tar mto
print(b.isdecimal())


a = 'CompanyX'
b = "Company10"                                                  # eta alpha na tai false ashbe output
print(a.isalpha())                                               # alpha bujhate.
print(b.isalpha())


a = "MyFolder"
b = "Demo002"
c = "2bring"                                                     # number aage use koray eta false hbe
d = "my demo"                                                    # space majhe use koray false ashbe. but uprer 1st duita thik thakay true ashbe
print(a.isidentifier())                                          # The isidentifier() method returns True if the string is a valid identifier, otherwise False.  A string is considered a valid identifier if it only contains alphanumer   A valid identifier cannot start with a number, or contain any spaces.ic letters (a-z) and (0-9), or underscores (_).
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())


a = "HELLO, AND WELCOME TO MY WORLD"                             # The istitle() method returns True if all words in a text start with a upper case letter,
b = "Hello"                                                      # AND the rest of the word are lower case letters, otherwise False.
c = "22 Names"
d = "This Is %'!?"
print(a.istitle())                                               # Symbols and numbers are ignored.
print(b.istitle())
print(c.istitle())
print(d.istitle())


a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"
print(a.isupper())                                              # The isupper() method returns True if all the characters are in upper case, otherwise False.
print(b.isupper())                                              # Numbers, symbols and spaces are not checked, only alphabet characters.
print(c.isupper())


a = "\u0030" 							                        # unicode for 0
b = "\u00B2" 							                        # unicode for ²
c = "10km2"                                                     # The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False
d = '3664489'                                                   # if all the characters in the text are numeric:
print(a.isnumeric())
print(b.isnumeric())                                            # Exponents, like ² and ¾ are also considered to be numeric values.
print(c.isnumeric())
print(d.isnumeric())


txt = "Hello!\nAre you #1?"                                     # \n shoralei true bolbe output e .
print (txt.isprintable())                                       # The isprintable() method returns True if all the characters are printable, otherwise False.


txt = "    s    "                                               # s ta remove korlei eta true hoye jabe
print (txt.isspace())                                           # The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.


myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)
                        # The join() method takes all items in an iterable and joins them into one string.
                        # A string must be specified as the separator.
myTuple = ("John", "Peter", "Vicky")
z = "#".join(myTuple)
print(z)


txt = "banana"
x = txt.ljust(20)                                   # he ljust() method will left align the string, using a specified character (space is default) as the fill character.
print(x, "is my favorite fruit.")                   # In the result, there are actually 14 whitespaces to the right of the word banana

txt = "banana"
x = txt.ljust(20, "O")                              # Using the letter "O" as the padding character:
print(x)

txt = "banana"
x = txt.rjust(20)                                   # right justified version etay n the result, there are actually 14 whitespaces to the left of the word banana.
print(x, "is my favorite fruit.")

txt = "banana"
x = txt.rjust(20, "O")                              #The rjust() method will right align the string, using a specified character (space is default) as the fill character.
print(x)




'''The index method finds the first occurrence of the specified value.
     this method raises an exception if the value is not found.
       The index() method is almost the same as the find() method.
         the only difference is that the find() method returns -1 if the value is not found. (See example below)'''

txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)                           # Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
print(x)

txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10)
print(x)

txt = "Hello, welcome to my world."
x = txt.index("e")                                  # Where in the text is the first occurrence of the letter "e"?:
print(x)

txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x)

txt = "Hello, welcome to my world."                 # Where in the text is the word "welcome"?:
x = txt.index("welcome")
print(x)

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)


txt = "Hello, welcome to my world."
#print(txt.index("q"))
print(txt.find("q"))                                # If the value is not found, the find() method returns -1, but the index() method will raise an exception:

txt = "Hello, welcome to my world."
print(txt.rfind("q"))
#print(txt.rindex("q"))                             # If the value is not found, the find() method returns -1, but the index() method will raise an exception:



txt = "Hello, welcome to my world."
x = txt.find('world')                               # find type use kore specifically ekta alphabet or words search kora possible evabei
print(x)

txt = "Mi casa, su casa."
x = txt.rfind("casa")                               # The rfind() method finds the last occurrence of the specified value. The rfind() method returns -1 if the value is not found. The rfind() method is almost the same as the rindex() method. See example below.
print(x)


txt = "Company 12"                                  # The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
print(txt.isalnum())                                # Example of characters that are not alphanumeric: (space)!#%&? etc.
txt = "Company12"                                   # etay space nai so etai true hbe
print(txt.isalnum())



a = "hello"
b = "welcome to the jungle"
c = "10.000"
print(a.zfill(10))                                  # The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
print(b.zfill(10))                                  # If the value of the len parameter is less than the length of the string, no filling is done.
print(c.zfill(10))                                  # structure ->     string.zfill(len)



txt = "Welcome to my world"                         # The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
print(txt.title())
txt = "Welcome to my 2nd world"                     # If the word contains a number or a symbol, the first letter after that will be converted to upper case.
print(txt.title())
txt = "hello b2b2b2 and 3g3g3g"                     # Note that the first letter after a non-alphabet letter is converted into a upper case letter:
print(txt.title())


txt = "Hello My Name Is sam"
print(txt.swapcase())                               # The swapcase() method returns a string where all the upper case letters are lower case and vice versa.


txt = "Hello, welcome to my world."
x = txt.startswith("Hello")                         # The startswith() method returns True if the string starts with the specified value, otherwise False.
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)                    # evabe range er mddhe ase naki etaw pawa jay
print(x)



a = "Hello,hjhshf,dhjsdgsksznfhs,fnccf, World!"
print(a.split(','))                                  # split diye alada quotation e neya jay string e ja thake alada words but comma use krte hbe uprer mto.. r chaile egulo alada variable rekkhe setake output e print(b) diye ber krte parbo

txt = "apple#banana#cherry#orange"
print(txt.split("#"))                                # output check krlei bujha jabe j sob alada words hoise # uthe giye

txt = "apple#banana#cherry#orange"                   # setting the maxsplit parameter to 1, will return a list with 2 elements!
print(txt.split("#", 1))

txt = "apple, banana, cherry"                        # The rsplit() method splits a string into a list, starting from the right.
print(txt.rsplit(", "))                              # If no "max" is specified, this method will return the same as the split() method.. When maxsplit is specified, the list will contain the specified number of elements plus one.

txt = "apple, banana, cherry"                        # setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)                              # Split the string into a list with maximum 2 items:
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
print(txt.splitlines())                              # splitlines(True) dile uprer \n taw ashbe output e.



'''Search for the last occurrence of the word "bananas", and return a tuple with three elements:
        1 - everything before the "match"
        2 - the "match"
        3 - everything after the "match" 
    The rpartition() method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.

    The first element contains the part before the specified string.

    The second element contains the specified string.

    The third element contains the part after the string. '''

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")                                            # If the specified value is not found, the rpartition() method returns a tuple containing: 1 - the whole string, 2 - an empty string, 3 - an empty string:
print(x)


'''The partition() method searches for a specified string, and splits the string into a tuple containing three elements.

    The first element contains the part before the specified string.

    The second element contains the specified string.

    The third element contains the part after the string.

    Note: This method search for the first occurrence of the specified string.'''

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)




a = '  djhdjkhdasjdiojd    d           iohdiojddkjaiod                diosjdoisajdolsajdosakdpkdps   m               '
print(a.strip())                                     # a variable erpor evabe a.strip() use koray string er aage r porer sob white space chole jabe but er vitor kono space dile seta output e show korbe

txt = "     banana     "
x = txt.strip()                                      # The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
print("of all fruits", x, "is my favorite")

txt = "     banana     "
x = txt.lstrip()                                     # The lstrip() method removes any leading characters (space is the default leading character to remove)
print("of all fruits", x, "is my favorite")

txt = "     banana     "
x = txt.rstrip()                                     # The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
print("of all fruits", x, "is my favorite")

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt")                               # that's how we can Remove the leading and trailing characters:
print(x)

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)                                             # Remove the leading characters:

txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")                              # Remove the trailing characters:
print(x)




a = "The rain in Spain stays mainly in the plain"
print('rain' in a)                                    # 'ain' in a diye bujhay text ta True bujhate....r chaile etake agei arekta variable b = 'ain' not in txt emnvabe rekhe output e just print(b) sei variable call dilei hoto

a = "The rain in Spain stays mainly in the plain"
print('x' not in a)                                   #  chaile quotation er vitor kichu na dileo hoy Amr proof. r w3 scl er mto "ain" dileo diye setay single quotation ow deya jay r not in a diye bujhay text ta false


a,b = "Hello", " World"                              # evabe direct koyekta variable eksthe cl korte pari chaile shortcut way te
print(a + b)                                         # etay evabe na diye c=a+b diye print (c) evabe variabvle cl korleo hoto r hae print(a + " " + b) evabe majhe space chaile sheta string er mtoi print korate hoy output e or variable cl kore xD

a = 36
b = "My name is John, and I am {}"
print(b.format(a))                                   # we know that it can't possible to print numbers and string together but we can do that by using format data types r hae print e ei format use erjnne uprer string variable er jekhane number chai sekhane { } eta use krte hbe 1st or 3rd braccket dile so utput e number na eshe setai ashbe lol

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36) # named indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)						# numbered indexes:
txt3 = "My name is {}, I'm {}".format("John",36)                        # empty placeholders:
print(txt1)
print(txt2)
print(txt3)


txt = "We have {:<9} chickens."                       # Use "<" to left-align the value:    {:>8} dile ki ashto check korei dekho. right align jete kaje lage r ki
print(txt.format(49))

txt = "We have {:^8} chickens."                       # Use "^" to center-align the value:
print(txt.format(49))

txt = "The temperature is {:=8} degrees celsius."     # Use "=" to place the plus/minus sign at the left most position:
print(txt.format(-5))

txt = "The temperature is between {:+} and {:+} degrees celsius."           # Use "+" to always indicate if the number is positive or negative:
print(txt.format(-3, 7))

txt = "The temperature is between {:-} and {:-} degrees celsius."           # Use ":-" to always indicate if the number is negative (positive numbers are displayed without any sign):
print(txt.format(-3, 7))

txt = "The temperature is between {: } and {: } degrees celsius."           # Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
print(txt.format(-3, 7))

txt = "The universe is {:,} years old."
print(txt.format(13800000000))				                            	# Use "," to add a comma as a thousand separator:

txt = "The universe is {:_} years old."
print(txt.format(13800000000))												# Use "_" to add a underscore character as a thousand separator:

txt = "We have {:d} chickens."										    	#Use "d" to convert a number, in this case a binary number, into decimal number format:
print(txt.format(0b101))

txt = "We have {:e} chickens."
print(txt.format(5))												    	# Use "e" to convert a number into scientific number format (with a lower-case e):

txt = "We have {:E} chickens."                                              # Use "E" to convert a number into scientific number format (with an upper-case E):
print(txt.format(5))

x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))				                                    	# Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

txt = "The price is {:f} dollars."
print(txt.format(x))				                                    	# same example, but with a lower case f:


txt = "The octal version of {0} is {0:o}"				                	# Use "o" to convert the number into octal format:
print(txt.format(10))


txt = "The Hexadecimal version of {0} is {0:x}"					        	# Use "x" to convert the number into Hex format:
print(txt.format(255))


txt = "The Hexadecimal version of {0} is {0:X}"				        		# Use "X" to convert the number into upper-case Hex format:
print(txt.format(255))


txt = "You scored {:%}"                                                     # Use "%" to convert the number into a percentage format:
print(txt.format(0.25))


txt = "You scored {:.0%}"                                                   # #Or, without any decimals:
print(txt.format(0.25))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for  dollars."
print(myorder.format(quantity, itemno, price))                              # just like this way we can get so many numbers in any string. dollatrs er age { } na deyay asheni output e


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))      # emn ultaplata aage pore variable cl dile output ow ultapalta ashe tai eta theke bachetei {2} {0} evabe select kore dite pari tokhn variable age pore holeo jhamela hoyna.



txt = "The binary version of {0} is {0:b}"									# Use "b" to convert the number into binary format:
print(txt.format(5))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))                                                # evabeo kora jay

print('I want 3 pieces of item 567 for 49.95 usd.')                         # chaile evabe direct ow ber krte pari number string eksthe but jodi uprer mto alada kykta variable cl kora hoy tokhn uprer format way chara output e emn pawa impossible