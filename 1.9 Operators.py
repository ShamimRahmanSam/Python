'''Python Operators
Operators are used to perform operations on variables and values.
Python divides the operators in the following groups:
    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators



    Python Comparison Operators
These operators compare the values on either side of them and decide the relation among them. They are also called Relational operators.

Assume variable a holds the value 10 and variable b holds the value 20, then −

Show Example

Operator	Description	Example
==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
!=	If values of two operands are not equal, then condition becomes true.	(a!= b) is true.
>	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
<	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
>=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
<=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.
Python Assignment Operators
Assume variable a holds the value 10 and variable b holds the value 20, then −

Show Example

Operator	Description	Example
=	Assigns values from right side operands to left side operand	c = a + b assigns value of a + b into c
+= Add AND	It adds right operand to the left operand and assign the result to left operand	c += a is equivalent to c = c + a
-= Subtract AND	It subtracts right operand from the left operand and assign the result to left operand	c -= a is equivalent to c = c - a
*= Multiply AND	It multiplies right operand with the left operand and assign the result to left operand	c *= a is equivalent to c = c * a
/= Divide AND	It divides left operand with the right operand and assign the result to left operand	c /= a is equivalent to c = c / ac /= a is equivalent to c = c / a
%= Modulus AND	It takes modulus using two operands and assign the result to left operand	c %= a is equivalent to c = c % a
**= Exponent AND	Performs exponential (power) calculation on operators and assign value to the left operand	c **= a is equivalent to c = c ** a
//= Floor Division	It performs floor division on operators and assign value to the left operand	c //= a is equivalent to c = c // a
Python Bitwise Operators
Bitwise operator works on bits and performs bit-by-bit operation. Assume if a = 60; and b = 13; Now in binary format they will be as follows −

a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a = 1100 0011

Python's built-in function bin() can be used to obtain binary representation of an integer number.

The following Bitwise operators are supported by Python language −

Show Example

Operator	Description	Example
& Binary AND	Operator copies a bit, to the result, if it exists in both operands	(a & b) (means 0000 1100)
| Binary OR	It copies a bit, if it exists in either operand.	(a | b) = 61 (means 0011 1101)
^ Binary XOR	It copies the bit, if it is set in one operand but not both.	(a ^ b) = 49 (means 0011 0001)
~ Binary Ones Complement	It is unary and has the effect of 'flipping' bits.	(~a ) = -61 (means 1100 0011 in 2's complement form due to a signed binary number.
<< Binary Left Shift	The left operand's value is moved left by the number of bits specified by the right operand.	a << 2 = 240 (means 1111 0000)
>> Binary Right Shift	The left operand's value is moved right by the number of bits specified by the right operand.	a >> 2 = 15 (means 0000 1111)
Python Logical Operators
The following logical operators are supported by Python language. Assume variable a holds True and variable b holds False then −

Show Example

Operator	Description	Example
and Logical AND	If both the operands are true then condition becomes true.	(a and b) is False.
or Logical OR	If any of the two operands are non-zero then condition becomes true.	(a or b) is True.
not Logical NOT	Used to reverse the logical state of its operand.	Not(a and b) is True.
Python Membership Operators
Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples. There are two membership operators as explained below −

Show Example

Operator	Description	Example
in	Evaluates to true if it finds a variable in the specified sequence and false otherwise.	x in y, here in results in a 1 if x is a member of sequence y.
not in	Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.	x not in y, here not in results in a 1 if x is not a member of sequence y.
Python Identity Operators
Identity operators compare the memory locations of two objects. There are two Identity operators as explained below −

Show Example

Operator	Description	Example
is	Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.	x is y, here is results in 1 if id(x) equals id(y).
is not	Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.	x is not y, here is not results in 1 if id(x) is not equal to id(y).
Python Operators Precedence
The following table lists all operators from highest precedence to the lowest.

Show Example

Sr.No.	Operator & Description
1
**

Exponentiation (raise to the power)

2
~ + -

Complement, unary plus and minus (method names for the last two are +@ and -@)

3
* / % //

Multiply, divide, modulo and floor division

4
+ -

Addition and subtraction

5
>> <<

Right and left bitwise shift

6
&

Bitwise 'AND'

7
^ |

Bitwise exclusive `OR' and regular `OR'

8
<= < > >=

Comparison operators

9
<> == !=

Equality operators

10
= %= /= //= -= += *= **=

Assignment operators

11
is is not

Identity operators

12
in not in

Membership operators

13
not or and

Logical operators'''



                 #  Arithmetic Operators

x, y = 13, 5

print (x + y)                                   # Additional
print (x - y)                                   # Minus
print (x * y)                                   # multiplication
print (x / y)                                   # Division
print (x % y)                                   # Modulus: returns the Remainder when first operand is divided by the second
print (x ** y)                                  # Exponentiation.. same as 13*13*13*13*13
print (x // y)                                  # The floor division // rounds the result down to the nearest whole number.. 13/5= remainder 2.something tai whole number nearest 2 ans.



                 # Comparison Operators

p, k = 20, 7

print (p > k)                                   # p is greater than k
print (p < k)                                   # p is lower than k
print (p == k)                                  # p Equal to k
print (p != k)                                  # p not equal to k
print (p >= k)                                  # p is greater than k or equal to K
print (p <= k)                                  # p is lower than k or equal to k



                 # Logical Operators

s = 100

print (s>50 and s<150)                          # Returns True. if both statements are true.. returns True because 5 is greater than 3 AND 5 is less than 10
print (s>500 or s<50)                           # retuens false. s<101 dileo ans true ashto cause we know 101>100. r etay 1st condition true na holeo porer true hole ans true bolbe r duitai false hole toh false e
print (not(s>500 or s<50))                      # returns True.. because not is used to reverse the result..ager tar mtoi eta false holeo tai true bolse output e not er jnnei. r hae ekhane or er bodole and ow use korte partam vitre.



                 # Assignment Operators (1st part)
                                              # these are kinda arithmatic operators with this = equal sign...
a = 10

a += 5                                        # this += operator means a+new number. 10+5=15. etai set kora hoise a namer ei variable tay
print (a)

a -= 3                                        # it means 10-5 .  but uprer tay kaj houay setar output 15 theke 3 substract houay output 12
print (a)

a *= 2                                        # it means 10*2.. but uprer tay kaj houay setar output 12 er sthe 2 multiply hoise output e
print (a)

a /= 2                                        # uprer tay output 24 houyay now 24/2=12 hbe output
print (a)

a %= 5                                        # etay Remainder ashbe. ager tay output 12 houayay 12/5= 2 ber hobe ((5*2=10. 12-2= 2)) bhagsesh or remainder
print (a)

a **= 3
print (a)                                     # it means a to the power 3 ( a^3 ) .. output ager tay 2 houay 2^3 = 8 hobe etay output

a //= 2                                       # it means ager tar output hisebe a er value 8 houayay 8/2 = 4 hobe now a er value then baki process hbe banano program jeta thakbe setay
print (a)

                # Assignment Operators (2nd part) These are also just like Bitwise Operators
a = 10                                        # ekhane new value neya hoise a variable tar just output pete. ager output jeta ber holo last a er jnne setar jnne perfectly hoyna program ta run tai changed value

a |= 2                                        # this |	OR	Sets each bit to 1 if one of two bits is 1 .. and it means x |= 3	x = x | 3
print (a)

a &= 3                                        # this & 	AND	Sets each bit to 1 if both bits are 1... and it means x &= 3	x = x & 3 then ashbe output. output ager tay 4 houayay 4&3 hbe
print (a)

a ^= 3                                        #  this ^	XOR	Sets each bit to 1 if only one of two bits is 1 ...
print (a)

a >>= 3                                       # it means x >>= 3	x = x >> 3          and this >> means Signed right shift    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print (a)

a <<= 3                                       # it means x <<= 3	x = x << 3          and this << means	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
print (a)
                                              #  and this new one means      ~ 	NOT	Inverts all the bits




                # Identity Operators

f = ['banana', 'mango', 'apple']
r = ['banana', 'mango', 'apple']                # chaile list tuple eshob baad diye int or numbers diyeo kora jeto nicher membership operators er sehe ja dekhano holo r ki
t = f

print (f is t)                                  # returns True because t is the same object as f
print (f is r)                                  # returns False because f is not the same object as r, even if they have the same content
print (f == r)                                  # this comparison returns True . to demonstrate the difference betweeen "is" and "==" this one made... because f is equal to r but not have the same object that's why ager tay false ashbe output etay true ashleo for equalization
print (f is not t)                              # returns False because t is the same object as f
print (f is not r)                              # returns True because f is not the same object as r, even if they have the same content
print (f != r)                                  # this comparison returns False ...to demonstrate the difference betweeen "is not" and "!=" this one made. because f is equal to r



                # Membership Operators

x = ["apple", "banana"]
y = [13, 15, 100]
print ('banana' in x)                            # returns True because a sequence with the value "banana" is in the list
print ('banana' not in x)                        # returns False because a sequence with the value "banana" is in the list we know.. but onno konokichu dile true bolto jeta nai uprer list tay x er moddhe..
print (100 in y)                                 # evabe int or number eo hoy string er list tuple eshob charaw
print (50 not in y)

'''             # Python Bitwise Operators  

Bitwise operators are used to compare (binary) numbers:
Operator	Name	Description
    & 	AND	Sets each bit to 1 if both bits are 1
    |	OR	Sets each bit to 1 if one of two bits is 1
    ^	XOR	Sets each bit to 1 if only one of two bits is 1
    ~ 	NOT	Inverts all the bits
    <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
    >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
(these have no extra examples or programs. uprer gula dekhei bujh ajay egular kaj tai...)'''