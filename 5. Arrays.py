'''What is an Array?
An array is a special variable, which can hold more than one value at a time.

If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
The solution is an array!
    An array can hold many values under a single name, and you can access the values by referring to an index number.'''


cars = ["Ford", "Volvo", "BMW"]                 # Python does not have built-in support for Arrays, but Python Lists can be used instead.
print(cars)                                     # Arrays are used to store multiple values in one single variable:
print(len(cars))                                # the len() method to return the length of an array (the number of elements in an array)... :
                                                # The length of an array is always one more than the highest array index.






cars = ["Ford", "Volvo", "BMW"]
cars[2] = 'Marcedes'                            # Modify the value of the first array item:
x = cars[1]
print(cars)
print(x)




cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")                        # You can use the append() method to add an element to an array.
print(cars)





cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)                                  # u can use the pop() method to remove an element from the array.
cars.remove('BMW')
print(cars)







'''You can also use the remove() method to remove an element from the array.

Example
Delete the element that has the value "Volvo":

cars.remove("Volvo")
Note: The list's remove() method only removes the first occurrence of the specified value.'''



''''Array Methods
Python has a set of built-in methods that you can use on lists/arrays.


append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.'''