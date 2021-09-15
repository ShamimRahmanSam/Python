'''Dictionary
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.'''


thisdict = dict(brand="Ford", model="Mustang", year=1964)       # note that keywords are not string literals
print(thisdict)                                                 # note the use of equals rather than colon for the assignment

x =  dict({                                         # emn dict( ) data type key word dileo hoy na dileo hoy nicher tar mto. { } manei dictionary
    'Name' : 'S.R.Sam',
    'ID' : 201611044094,
    'Age' : 22
    })
print (x)


x =  {
    'Name' : 'S.R.Sam',
    'ID' : 201611044094,
    'Age' : 22
    }
print (x)                                           # easily evabe dictionaryr output pawa jay ei program wise
print (type(x))                                     # icche hole evabe type jana jabe
print (len(x))                                      # for getting the length of the set




x =  {
    'Name' : 'S.R.Sam',
    'ID' : 201611044094,
    'Age' : 22
    }

y = x['ID']                                 # we can access the items of a dictionary by referring to its key name, inside square brackets:
print (y)

z = x.get('Age')                            # evabeo values ber kora jay keys call kore by this way. output ashbe 22
print (z)

print (x)                                   # output e sob keys & values ashbe x er






x =  {
    'Name' : 'S.R.Sam',
    'ID' : 201611044094,
    'Age' : 22,
    'Address' : 'Mohammadpur',
    'sub' : 'CSE'
    }
x['Name'] = 'Shamim Rahman Sam'
x['Age'] = 24                               # we can change the value of a specific item by referring to its key name: like this age & name..

del x['ID']                                 # The del keyword removes the item with the specified key name:
x.pop('Address')                            # also that's how we can delete any values
x.popitem()                                 # The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

print (x)                                   # output just name & age ashbe taw change kora hoise jegula seta uprer program wise r kih.. and baki keys delete koray just ei 2 ta keys output e ashbe taw changed ta jodi change na krtm tahole x er vitre jevabe ase sevabei ashto






x = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for y in x:  # You can loop through a dictionary by using a for loop.
    print(y)                                # new variable cl koray just keys ber hobe etay.. print(x) dile output e 3 bar ashto set ta.




x =	{
  "brand" : "Ford",
  "model" : "Mustang",
  "year" : 1964
}
for y in x:                             # You can loop through a dictionary by using a for loop.
    print(x[y])                         # but there are methods to return the values as well. eta values ouput pawar system. print(variable[variable])

for y in x.values():                    # can also use the values() function to return values of a dictionary:
    print(y)





x = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
for y in x:
    print(x[y], '--', y)                # When looping through a dictionary, the return value are the keys of the dictionary,  eta eksthe 2 ta output neyar system

for y, z in x.items():                  # Loop through both keys and values, by using the items() function:  but uprer system tai best.
        print(y, z)





x =  {
    'Name' : 'S.R.Sam',
    'ID' : 201611044094,
    'Age' : 22
}

x ['Sub'] = 'CSE'                                   # Adding an item to the dictionary is done by using a new index key and assigning a value to it:
print (x)

if 'age' in x:
    print ('Yes')
else:                                               # evabe if else ow use kore key ase naki ta ber kora jay. but etay age thakteo NO bolse cz Age chilo likhsi age and python small/capital letters follow kore. wrong dile hyna
    print ('No')





x = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = x.copy()                                       # evabe copy kora jay onno variable e easily
print(mydict)




x = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(x)                                        # evabeo copy kora jay
print(mydict)




family = {                                              # nested loops and if you want to nest three dictionaries that already exists as dictionaries:
  "sis" : {                                             # A  dictionary can also contain many dictionaries, this is called nested dictionaries.
    "name" : "Emil",
    "year" : 2004
  },
  "bro ": {
    "name" : "Tobias",
    "year" : 2007
  },
  "cousin" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(family)





sis= {
  "name" : "Emil",
  "year" : 2004
}
bro = {
  "name" : "Tobias",
  "year" : 2007
}
cousin = {
  "name" : "Linus",
  "year" : 2011
}

family = {
  "sis" : sis,
  "bro" : bro,
  "cousin" : cousin
}                                           # Create three dictionaries, than create one dictionary that will contain the other three dictionaries:
print(family)                               # uprer ta r ei program 2 tar output e ek e ashbe




thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()                            # clear() deyay output ashbe just {}
print (thisdict)
del thisdict
print(thisdict)                             # this will cause an error at last or in start .. because "thislist" no longer exists after deletion.





'''Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()  	Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items() 	    Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary




Dictionaries Defined
Dictionaries are another data structure in Python. They’re similar to a list in that they can be used to organize data into collections. However, data in a dictionary isn't accessed based on its position. Data in a dictionary is organized into pairs of keys and values. You use the key to access the corresponding value. Where a list index is always a number, a dictionary key can be a different data type, like a string, integer, float, or even tuples.

When creating a dictionary, you use curly brackets: {}. When storing values in a dictionary,
 the key is specified first, followed by the corresponding value, separated by a colon. 
 For example,  animals = { "bears":10, "lions":1, "tigers":2 } creates a dictionary with three key value pairs, 
 stored in the variable animals. The key "bears" points to the integer value 10, 
 while the key "lions" points to the integer value 1, and "tigers" points to the integer 2. You can access the values by referencing the key,
 like this: animals["bears"]. This would return the integer 10, since that’s the corresponding value for this key.

You can also check if a key is contained in a dictionary using the in keyword. Just like other uses of this keyword, it will return True if the key is found in the dictionary; otherwise it will return False.

Dictionaries are mutable, meaning they can be modified by 
adding, removing, and replacing elements in a dictionary, similar to lists. '
You can add a new key value pair to a dictionary by assigning a value to the key, like this: animals["zebras"] = 2.
 This creates the new key in the animal dictionary called zebras, and stores the value 2. 
 You can modify the value of an existing key by doing the same thing. So animals["bears"] = 11 would change the value stored in the bears key from 10 to 11.
  Lastly, you can remove elements from a dictionary by using the del keyword. By doing del animals["lions"] you would remove the key value pair from the animals dictionary.
  
  
  
  
  
  
  
  
  Iterating Over Dictionaries
You can iterate over dictionaries using a for loop, just like with strings, lists, and tuples. 
This will iterate over the sequence of keys in the dictionary. If you want to access the corresponding values associated with the keys,
 you could use the keys as indexes. Or you can use the items method on the dictionary, 
 like dictionary.items().
  This method returns a tuple for each element in the dictionary, 
  where the first element in the tuple is the key and the second is the value.
  
  
  
  
  Dictionary Methods Cheat Sheet
Dictionary Methods Cheat Sheet
Definition

x = {key1:value1, key2:value2}

Operations

len(dictionary) - Returns the number of items in the dictionary
for key in dictionary - Iterates over each key in the dictionary
for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
if key in dictionary - Checks whether the key is in the dictionary
dictionary[key] - Accesses the item with key key of the dictionary
dictionary[key] = value - Sets the value associated with key
del dictionary[key] - Removes the item with key key from the dictionary
Methods

dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
dict.keys() - Returns a sequence containing the keys in the dictionary
dict.values() - Returns a sequence containing the values in the dictionary
dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
dict.clear() - Removes all the items of the dictionary
Check out the official documentation for dictionary operations and methods.
  

If you only wanted to access the keys in a dictionary, you could use the keys() method on the dictionary: dictionary.keys(). If you only wanted the values, you could use the values() method: dictionary.values().'''