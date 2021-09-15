def rectangle_area(base, height):
  area = base * height
  return area

print("The area is ", rectangle_area(5, 6))






def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else:
    return "Zero"

print(number_group(10))  # Should be Positive
print(number_group(0))  # Should be Zero
print(number_group(-5))  # Should be Negative






def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))







def convert_distance(miles):  # Complete the function to return the result of the conversion
  km = miles * 1.6  # approximately 1.6 km in 1 mile
  return km

miles = 55
km = convert_distance(miles)  # Convert miles to kilometers by calling the function above

print("The distance in kilometers is " + str(km))
print("The round-trip in kilometers is " + str(km * 2))





# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
  if number2 > number1:
    return number1, number2
  else:
    return number2, number1




# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)




def lucky_number(name):
  number = len(name) * 9
  return "Hello " + name + ". Your lucky number is " + str(number)

print(lucky_number("Kay"))
print(lucky_number("Cameron"))


#easy way

name= "manney"
name2="shuv"
number = len(name)*3
number2 = len(name2)*5
print("hey {}, your lucky number is {}".format(name,number))
print("hey {}, your lucky number is {}".format(name2,number))






def month_days(month, days):
  print(month + " has " + str(days) + " days.")

month_days("June", 30)
month_days("July", 31)





def get_seconds(hours, minutes, seconds):
  return 3600 * hours + 60 * minutes + seconds

amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)






bill = 47.28
tip = bill * (15 / 100)
total = bill + tip
share = total / 2
print("Each person needs to pay: " + str(share))





# x = input("Username : ")
# print(x)
def hint_username(username):
  if len(username) < 3:
    print("areh beta cholbona! aro boro name de!")  # idk why this program isn't woring properly





# input("number = ")
def is_positive(number):
  if number > 0:
    return True
  else:
    return False












def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // 4096
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % 4096
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
      return 4096 * (full_blocks + 1)
    return full_blocks * 4096


print(calculate_storage(1))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192






number = int(100)
if number > 11:
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)









def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown














def exam_grade(score):
	if score>95:
		grade = "Top Score"
	elif score>=60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail










def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))













def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))













def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to
# keep just the fractional part of the quotient
 if denominator >0:
    return (numerator % denominator) / denominator

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0







"""Question 2
What's the value of this Python expression: "big" > "small"
True
False
big
small

Incorrect
Not quite .  Python compares strings in alphabetical order, and "big" begins with "b" which alphabetically comes before the "s" in "small"."""






def attempts(n):
  x = 1
  while x <= n:
    print("Attempt " + str(x))
    x += 1
  print("Done")

attempts(5)








def print_prime_factors(number):
  # Start with two, which is the first prime
  factor =2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor +=1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT









def sum_divisors(n):
  i = 1
  sum = 0
    # Return the sum of all divisors of n, not including n
  while i < n:
    if n % i == 0:
      sum += i
      i +=1
    else:
      i+=1
  return sum
print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114







def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n != 0:
    n = n / 2

  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False

print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False









def square(n):
  return n * n

def sum_squares(x):
  sum = 0
  for n in range(x):
    sum += square(n)
  return sum

print(sum_squares(10))  # Should be 285








def factorial(n):
    result = 1
    for x in range(1,n):
        result = result*x
    return result

for n in range(0,10):
    print(n, factorial(n+1))








def factorial(n):
    result = 1
    for i in range(1, n+1):
        result*=i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120









for left in range(7):                                                   #nested loop example
    for right in range(left, 7):
        print("[" +str(left) + "|" + str(right) + "]", end = " ")
    print()









for x in range(1,11):
  print(x**3)










for n in range(0,15):
    result = (n*7)
    print (result)









def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return n

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15















def is_power_of(number, base):
# Base case: when number is smaller than base.
  if number ==1:
    return True
  if number < base:
# If number is equal to 1, it's a power (base**0).
    return False
  number /= base
# Recursive case: keep dividing number by base.

  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
















def is_power_of(number, base):
# Base case: when number is smaller than base.
  if number ==1:
    return True
  if number < base:
# If number is equal to 1, it's a power (base**0).
    return False
  number /= base
# Recursive case: keep dividing number by base.

  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False








number = 1
while number <= 7:
	print(number, end=" ")
	number = number+1








def show_letters(word):
	for x in range(0, len(word)):
		print(word[x])

show_letters("Hello")
# Should print one line per letter







def digits(n):
   count = 0
   if n == 0:
      return 1
   while (n > 0):
      count += 1
      n = n//10
   return count
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

#easy way of this program

def digits(n):
    return len(str(n))

print(digits(25))  # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))  # Should print 1







def multiplication_table(a, b):
    for x in range(a,b+1):
        for y in range(a,b+1):
            print(str(x*y), end=" ")
        print()

multiplication_table(1, 3)













def counter(start, stop):
	x = start
	if x>stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x>stop:
				return_string += ","
			x=x-1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x<stop:
				return_string += ","
			x=x+1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"








def even_numbers(maximum):
	return_string = ""
	for x in range(2,maximum+1):
		if x%2==0:
			return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed








for x in range(1, 10, 3):
    print(x)










def double_word(word):
    return word * 2 + str(len(word * 2))
print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0







def first_and_last(message):
    if not message or message[0] == message[-1]:
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))









word = "supercalifragilisticexpialidocious"
print(word.index("x"))







def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS








def to_celcius(x):
    return (x-32)*5/9
    for x in range(0,101,10):
        print("{:>3} F | {:>6.2f} C".format(x, to_celcius()))                           #this code is unreachable









def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	input_string =input_string.lower()
	# Traverse through each letter of the input string
	for x in input_string:
		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
		if x!=" ":
			new_string = new_string + x
			reverse_string = x + reverse_string
	# Compare the strings
	if new_string==reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True











def convert_distance(miles):
	km = miles * 1.6
	result = "{} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km










def nametag(first_name, last_name):
	return("{} {}.".format(first_name, last_name[0]))

print(nametag("Jane", "Smith"))
# Should display "Jane S."
print(nametag("Francesco", "Rinaldi"))
# Should display "Francesco R."
print(nametag("Jean-Luc", "Grand-Pierre"))
# Should display "Jean-Luc G."











def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = sentence.rfind(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"









def get_word(sentence, n):
	# Only proceed if n is positive
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words
		if n <= len(words):
			return words[n-1]
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing









def file_size(file_info):
	name, file_extension, bytes = file_info
	return("{:.2f}".format(bytes / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21








def skip_elements(elements):
	# code goes here
	elements = [v for i, v in enumerate(elements) if i % 2 == 0]
	return elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']







multiples = []
for x in range(1,11):                                                           #list comprenhensions example
    multiples.append(x*7)
    print(multiples)




multiples=[x*7 for x in range(1,11)]                                             #list comprenhensions example
print(multiples)




languages=["python","java","go", "perl","c", "basic", "c++", "js"]                   #list comprenhensions example
lengths = [len(languages) for languages in languages]
print(lengths)





z=[x for x in range(0,101) if x%3==0]
print(z)









filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [e.replace('.hpp','.h') for e in filenames]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]










def pig_latin(text):
  say = []

  # Separate the text into words

  words = text.split()
  for word in words:

    # Create the pig latin word and add it to the list

    word = word[1:] + word[0] + "ay"
    say.append(word)

    # Turn the list back into a phrase

  return " ".join(say)

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"

print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"












def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for i in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if i >= value:
                result += letter
                i -= value
            else:
                result += "-"
    return result

print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------

















def group_list(group, users):
  members = ', '.join(users)
  return "{}: {}".format(group, members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"










def guest_list(guests):
	for guest in guests:
		name, age, job = guest
		print("{} is {} years old and works as {}".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""










toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc ["Epilogue"] = 39     # Epilogue starts on page 39
toc ["Chapter 3"] = 24    # Chapter 3 now starts on page 24
print(toc)                # What are the current contents of the dictionary?
print("Chapter 5" in toc) # Is there a Chapter 5?












cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for key, value in cool_beasts.items():
    print("{} have {}".format(key, value))










wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item, color in wardrobe.items():
	for colorsub in color:
		print("{} {}".format(colorsub,item))










def email_list(domains):
	emails = []
	for email, users in domains.items():
	  for user in users:
	    emails.append("{}@{}".format(user, email))
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))












def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for users in group_dictionary[group]:
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary
			if users in user_groups:
				user_groups[users].append(group)
			else:
				user_groups[users] = [group]
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))











def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for items, price in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44












def format_address(address_string):
    # Declare variables
    house_number = ' '
    street_name = " "

    # Separate the address string into parts
    x = address_string.split(" ")
    # Traverse through the address parts
    for y in x:
        # Determine if the address part is the
        # house number or part of the street name
        if (y.isdigit()):
            house_number = y
        else:
            street_name += y
            street_name += ' '
    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(house_number, street_name)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"












def highlight_word(sentence, word):
	return((sentence.replace(word,word.upper())))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))









def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order
    new_list = list2
    for i in reversed(range(len(list1))):
        new_list.append(list1[i])
        return new_list
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print(combine_lists(Jamies_list, Drews_list))










def squares(start, end):
	squares = [value ** 2 for value in range(start,end+1)]
	return [squares]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]








def car_listing(car_prices):
  result = ""
  for carname, carprice in car_prices.items():
    result += "{} costs {} dollars".format(carname,carprice) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))











class Apple:
    color=""
    flavor=""
    j=Apple()
    j.color="red"
    j.flavor="sweet"

    print(j.flavor)
    print(j.color)


















