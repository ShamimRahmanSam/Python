x = ('banana', 'grape', 'apple')                    # A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets. touples and list system ek e often just [] eta list er  r () eta tuple e use hoy

print (x)

print(type(x))                                      # class and datat type ta ber korte hoy evabe tai tuple ber hoise output e

print (len(x))                                      # To determine how many items a tuple has, use the len() method:

print (x[1])                                        # can access tuple items by referring to the index number, inside square brackets:
print (x[-1])                                       # Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.


x = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(x[2:5])                                       # This will return the items from position 2 to 5. Remember that the first item is position 0, and note that the item in position 5 is NOT included .. You can specify a range of indexes by specifying where to start and where to end the range.When specifying a range, the return value will be a new tuple with the specified items
print(x[-4:-1])                                     # Negative indexing means starting from the end of the tuple. This example returns the items from index -4 (included) to index -1 (excluded).. Remember that the last item has the index -1,



x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"                                       # once a tuple is created, you cannot change its values. Tuples are unchangeable,or immutable as it also is called.
x = tuple(y)                                        # But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
print(x)                                            # Convert the tuple into a list to be able to change it:



x = ("apple", "banana", "cherry")
for x in x:                                 # we can loop through the tuple items by using a for loop.
  print(x)



x = ("apple", "banana", "cherry")
if "banana" in x:                            # To determine if a specified item is present in a tuple use the in keyword:
  print("Yes, 'apple' is in the fruits tuple")



x = tuple(("apple", "banana", "cherry"))    # It is also possible to use the tuple() constructor to make a tuple.
print(x)



tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2                    # To join two or more tuples you can use the + operator:
print(tuple3)



''' nicher ei last 2 ta program er jnne output er shuru te or last e error dekhabe program tay run holeo'''


thistuple = ("apple", "banana", "cherry")
del thistuple                               # Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
print(thistuple)                            # this will raise an error because the tuple no longer exists




thistuple = ("apple", "banana", "cherry")   # Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
thistuple[3] = "orange "                    # This will raise an error
print(thistuple)                            # You cannot add items to a tuple:



'''
                    Python has two built-in methods that you can use on tuples:

        count()	        Returns the number of times a specified value occurs in a tuple
        index()	        Searches the tuple for a specified value and returns the position of where it was found
        
        
        
        Modifying Lists
While lists and strings are both sequences, a big difference between them is that lists are mutable. 
This means that the contents of the list can be changed, unlike strings, which are immutable. You can add, remove, or modify elements in a list.

You can add elements to the end of a list using the append method. You call this method on a list using dot notation, 
and pass in the element to be added as a parameter. For example, list.append("New data") would add the string "New data" to the end of the list called list.

If you want to add an element to a list in a specific position, you can use the method insert. The method takes two parameters: 
the first specifies the index in the list, and the second is the element to be added to the list.
 So list.insert(0, "New data") would add the string "New data" to the front of the list. 
 This wouldn't overwrite the existing element at the start of the list. It would just shift all the other elements by one. 
 If you specify an index that’s larger than the length of the list, the element will simply be added to the end of the list.

You can remove elements from the list using the remove method. 
This method takes an element as a parameter, and removes the first occurrence of the element. 
If the element isn’t found in the list, you’ll get a ValueError error explaining that the element was not found in the list.

You can also remove elements from a list using the pop method.
 This method differs from the remove method in that it takes an index as a parameter, and returns the element that was removed.
  This can be useful if you don't know what the value is, but you know where it’s located.
   This can also be useful when you need to access the data and also want to remove it from the list.

Finally, you can change an element in a list by using indexing to overwrite the value stored at the specified index.
 For example, you can enter list[0] = "Old data" to overwrite the first element in a list with the new string "Old data".
 
 
 
 
 
 
 
 
 
 Tuples
As we mentioned earlier, strings and lists are both examples of sequences. Strings are sequences of characters, and are immutable. Lists are sequences of elements of any data type, and are mutable. The third sequence type is the tuple. Tuples are like lists, since they can contain elements of any data type. But unlike lists, tuples are immutable. They’re specified using parentheses instead of square brackets.

You might be wondering why tuples are a thing, given how similar they are to lists. 
Tuples can be useful when we need to ensure that an element is in a certain position and will not change. 
Since lists are mutable, the order of the elements can be changed on us. 
Since the order of the elements in a tuple can't be changed, the position of the element in a tuple can have meaning.
 A good example of this is when a function returns multiple values.
  In this case, what gets returned is a tuple, with the return values as elements in the tuple.
   The order of the returned values is important, and a tuple ensures that the order isn’t going to change.
    Storing the elements of a tuple in separate variables is called unpacking. 
This allows you to take multiple returned values from a function and store each value in its own variable.





Iterating Over Lists Using Enumerate
When we covered for loops, we showed the example of iterating over a list. 
This lets you iterate over each element in the list, exposing the element to the for loop as a variable. 
But what if you want to access the elements in a list, along with the index of the element in question? 
You can do this using the enumerate() function. The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. 
The first value of the tuple is the index and the second value is the element itself.'''