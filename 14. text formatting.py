'''To make sure a string will display as expected, we can format the result with the format() method.

String format()
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:

baki gulo 1.7 string all ways  ei ase though I'm coppying here'''


price = 49
txt = "The price is {} dollars"
print(txt.format(price))


price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))



a = 36
b = "My name is John, and I am {}"
print(b.format(a))                                   # we know that it can't possible to print numbers and string together but we can do that by using format data types r hae print e ei format use erjnne uprer string variable er jekhane number chai sekhane { } eta use krte hbe 1st or 3rd braccket dile soutpuyt e number na eshe setai ashbe lol



txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36) # named indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)						# numbered indexes:
txt3 = "My name is {}, I'm {}".format("John",36)                        # empty placeholders:
print(txt1)
print(txt2)
print(txt3)



'''Named Indexes
You can also use named indexes by entering a name inside the curly brackets {carname}, 
but then you must use names when you pass the parameter values txt.format(carname = "Ford")'''
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))



txt = "We have {:<8} chickens."                       # Use "<" to left-align the value:    {:>8} dile ki ashto check korei dekho. right align jete kaje lage r ki
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

print('I want 3 pieces of item 567 for 49.95 usd.')                         # chaile evabe direct ow ber krte pari number string eksthe