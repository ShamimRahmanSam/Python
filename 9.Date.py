import datetime

x = datetime.datetime.now()                             # Python Dates -- A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

print(x)

print(x.year)                                           # evabe sob ber kora jay.these are examples
print(x.month)
print(x.date())

print(x.strftime('%a'))                                 # saturday er shortform Sat ashbe output e
print(x.strftime("%A"))                                 # for day.. as like today is saturday

print(x.strftime('%b'))                                 # Month name, short version	Dec
print(x.strftime('%B'))                                 # Month name, full version	December

print(x.strftime('%c'))                                 # Local version of date and time as like-	Sat Feb 29 09:47:59 2020
print(x.strftime('%C'))                                 # year bujhay maybe 2020 er 20 dekhacche output

print(x.strftime('%d'))                                 # Day of month like 01 theke 31.
print(x.strftime('%D'))                                 # Day of month 02/29/20

print(x.strftime("%w"))                                 # Weekday as a number 0-6, 0 is Sunday
print(x.strftime("%W"))                                 # Week number of year, Monday as the first day of week, 00-53.... 0 theke start hoy

print(x.strftime('%p'))                                 # am pm show kore .. bakigulo niche lekha ase lagle use korbo. enough practiced



'''Date Output of upper program--
When we execute the code from the example above the result of print(x) will be:

2020-02-29 09:33:06.627131

The date contains year, month, day, hour, minute, second, and microsecond.
The datetime module has many methods to return information about the date object.
Here are a few examples, you will learn more about them later in this chapter:'''




'''A reference of all the legal format codes:

%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%'''


