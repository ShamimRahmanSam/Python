'''Python File Open
File handling is an important part of any web application.

Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

Syntax
To open a file for reading it is enough to specify the name of the file:

f = open("demofile.txt")
The code above is the same as:

f = open("demofile.txt", "rt")
Because "r" for read, and "t" for text are the default values, you do not need to specify them.

Note: Make sure the file exists, or else you will get an error.'''



import os                                         # ei first program ta last e na kore ekhane korsi jate output hisebe created new folder ta delete hoy ei system e tai... niche normally system wise deya hoise programs
os.rmdir("New Folder")                            # Note: You can only remove empty folders.



# uporer '''   ''' lekha gulo nicher egulor jnnei
f = open("Sam.py", "r")
print(f)




f = open("Sam.py", "rt")
print(f)




f = open("Sam.py", "r")
for x in f:
  print(x)




f = open("Sam.py", "r")
print(f.readline())




#f = open("myfile.txt", "x")                               # new  empty file create hoye gese for x..   but nichei remove koray gayeb ow hoye gee tai eta #tag  deya

#f = open("myfile.txt", "w")                               # Create a new file if it does not exist:  but ei name e agerta tei file create houay error ashbe output



import os
os.remove("myfile.txt")                                    # To delete a file, you must import the OS module, and run its os.remove() function  .. upre 1st ei ekta xmple deya ase




'''Check if File exist:
To avoid getting an error, you might want to check if the file exists before you try to delete it:

Example
Check if file exists, then delete it:'''

import os
if os.path.exists("myfile.txt"):                                      # error dekhabe cz agei deleted
  os.remove("myfile.txt")
else:
  print("The file does not exist")





f = open("demofile2.txt", "a")
f.write("Now the file has more content!")                 # a for appending .. so file na  paway neew ekta file ei demofile 2 name e create hoye gese
f.close()                                                 # It is a good practice to always close the file when you are done with it.
                                                          # You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.
f = open("demofile2.txt", "r")                            # open and read the file after the appending:
print(f.read())








f = open("demofile3.txt", "w")                                    # the "w" method will overwrite the entire file.
f.write("Woops! I have deleted the content!")                     # ei file taw na thakay newly created hoise and eta write hoise output wise
f.close()
f = open("demofile3.txt", "r")                                    # open and read the file after the appending:
print(f.read())





'''Delete Folder
To delete an entire folder, use the os.rmdir() method:

Example
Remove the folder "myfolder":'''




'''Opening and Closing Files
Until now, you have been reading and writing to the standard input and output. Now, we will see how to use actual data files.

Python provides basic functions and methods necessary to manipulate files by default. You can do most of the file manipulation using a file object.

The open Function
Before you can read or write a file, you have to open it using Python's built-in open() function. This function creates a file object, which would be utilized to call other support methods associated with it.


Syntax
file object = open(file_name [, access_mode][, buffering])


Here are parameter details −

file_name − The file_name argument is a string value that contains the name of the file that you want to access.

access_mode − The access_mode determines the mode in which the file has to be opened, i.e., read, write, append, etc. A complete list of possible values is given below in the table. This is an optional parameter and the default file access mode is read (r).

buffering − If the buffering value is set to 0, no buffering takes place. If the buffering value is 1, line buffering is performed while accessing a file. If you specify the buffering value as an integer greater than 1, then buffering action is performed with the indicated buffer size. If negative, the buffer size is the system default(default behavior).



Here is a list of the different modes of opening a file −

Sr.No.	Mode & Description
1	
r

Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.

2	
rb

Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.

3	
r+

Opens a file for both reading and writing. The file pointer placed at the beginning of the file.

4	
rb+

Opens a file for both reading and writing in binary format. The file pointer placed at the beginning of the file.

5	
w

Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

6	
wb

Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

7	
w+

Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

8	
wb+

Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

9	
a

Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

10	
ab

Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

11	
a+

Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

12	
ab+

Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

The file Object Attributes
Once a file is opened and you have one file object, you can get various information related to that file.

Here is a list of all the attributes related to a file object −

Sr.No.	Attribute & Description
1	
file.closed

Returns true if file is closed, false otherwise.

2	
file.mode

Returns access mode with which file was opened.

3	
file.name

Returns name of the file.'''


