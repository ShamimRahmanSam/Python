import random
print(random.randrange(5,50))       # ekhane 5 to 50 er moddhe jekono random number show hbe output e r print krte evabei random. randthen range (numbers ditehoy) ei system wise
                                       # Python does not have a random() function to make a random number,
                                           # but Python has a built-in module called random that can be used to make random numbers ..thik jevabe upore kora hoise

              # now we will see how to convert a number into another data type of numbers
x = 1                       # int
y = 2.8                     # float
z = 1j                      # complex

print(x,y,z)

a = float(x)                # convert from int to float.. r float(1) likhleo hoto but agei variable neyay ekhane variable fdeya hoise
b = int(y)                  # convert from float to int:
c = complex(x)              # convert from int to complex:

            # we cannot convert complex numbers into another number type.

print(a)                    # converted result
print(b)
print(c)

print(x)                    # original jeta chilo aage
print(y)
print(z)

print(type(a))              # converted types egula
print(type(b))
print(type(c))

print(type(x))              # original j types chilo
print(type(y))
print(type(z))



'''Here are some examples of numbers.

int	        float	        complex
10      	0.0	            3.14j
100     	15.20	        45.j
-786	    -21.9	        9.322e-36j
080	        32.3+e18	    .876j
-0490	    -90.	        -.6545+0J
-0×260	    -32.54e100	    3e+26J
0×69	    70.2-E12	    4.53e-7j

A complex number consists of an ordered pair of real floating-point numbers denoted by a + bj, where a is the real part
and b is the imaginary part of the complex number.



Number Type Conversion
Python converts numbers internally in an expression containing mixed types to a common type for evaluation. Sometimes, you need to coerce a number explicitly from one type to another to satisfy the requirements of an operator or function parameter.

Type int(x) to convert x to a plain integer.

Type long(x) to convert x to a long integer.

Type float(x) to convert x to a floating-point number.

Type complex(x) to convert x to a complex number with real part x and imaginary part zero.

Type complex(x, y) to convert x and y to a complex number with real part x and imaginary part y. x and y are numeric expressions




Mathematical Functions
Python includes the following functions that perform mathematical calculations.

Sr.No.	Function & Returns ( Description )
1	abs(x)
The absolute value of x: the (positive) distance between x and zero.

2	ceil(x)
The ceiling of x: the smallest integer not less than x.

3	
cmp(x, y)

-1 if x < y, 0 if x == y, or 1 if x > y. Deprecated in Python 3. Instead use return (x>y)-(x<y).

4	exp(x)
The exponential of x: ex

5	fabs(x)
The absolute value of x.

6	floor(x)
The floor of x: the largest integer not greater than x.

7	log(x)
The natural logarithm of x, for x > 0.

8	log10(x)
The base-10 logarithm of x for x > 0.

9	max(x1, x2,...)
The largest of its arguments: the value closest to positive infinity

10	min(x1, x2,...)
The smallest of its arguments: the value closest to negative infinity.

11	modf(x)
The fractional and integer parts of x in a two-item tuple. Both parts have the same sign as x. The integer part is returned as a float.

12	pow(x, y)
The value of x**y.

13	round(x [,n])
x rounded to n digits from the decimal point. Python rounds away from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0.

14	sqrt(x)
The square root of x for x > 0.




Random Number Functions
Random numbers are used for games, simulations, testing, security, and privacy applications. Python includes the following functions that are commonly used.

Sr.No.	Function & Description
1	choice(seq)
A random item from a list, tuple, or string.

2	randrange ([start,] stop [,step])
A randomly selected element from range(start, stop, step).

3	random()
A random float r, such that 0 is less than or equal to r and r is less than 1

4	seed([x])
Sets the integer starting value used in generating random numbers. Call this function before calling any other random module function. Returns None.

5	shuffle(lst)
Randomizes the items of a list in place. Returns None.

6	uniform(x, y)
A random float r, such that x is less than or equal to r and r is less than y.

Trigonometric Functions
Python includes the following functions that perform trigonometric calculations.

Sr.No.	Function & Description
1	acos(x)
Return the arc cosine of x, in radians.

2	asin(x)
Return the arc sine of x, in radians.

3	atan(x)
Return the arc tangent of x, in radians.

4	atan2(y, x)
Return atan(y / x), in radians.

5	cos(x)
Return the cosine of x radians.

6	hypot(x, y)
Return the Euclidean norm, sqrt(x*x + y*y).

7	sin(x)
Return the sine of x radians.

8	tan(x)
Return the tangent of x radians.

9	degrees(x)
Converts angle x from radians to degrees.

10	radians(x)
Converts angle x from degrees to radians.

Mathematical Constants
The module also defines two mathematical constants −

Sr.No.	Constants & Description
1	
pi

The mathematical constant pi.

2	
e

The mathematical constant e.'''