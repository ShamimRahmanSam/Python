x = {"apple", "banana", "cherry"}                   # A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
print (x)                                           # Sets are unordered, so you cannot be sure in which order the items will appear.
print (len(x))                                      # To determine how many items a set has, use the len() method.



x = {"apple", "banana", "cherry"}
for x in x:                                         # You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
  print(x)                                          # But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword. r print er aage indentation or space use korar karon hocche for loop use hoise tai



x = {'banana', 'orange', 'mango'}
print ('mango' in x)                                # ask if a specified value is present in a set, by using the in keyword.
print ('banana' not in x)                           # not in keywords ow usekorar example





x = set(("apple", "banana", "cherry"))              # It is also possible to use the set() constructor to make a set.
print(x)					                        # Note: the set list is unordered, so the result will display the items in a random order.






x = {'banana', 'orange', 'mango', 'cherry'}         # Once a set is created, you cannot change its items, but you can add new items.

x.add('Blueberry')                                  # To add one item to a set use the add() method.
print (x)

x.update(['Raspberry', 'Coconut', 'Malta', 'lemon'])        #Add multiple items to a set, using the update() method: and ekhane [] etar moddhe na rekhe ager tar moto just ()rakhle  prottek ta alphabet alada show hoto tai ([evabe kora hoise])
print (x)





x = {"a", "b" , "c"}
y = {1, 2, 3}

x.update(y)                                          # the update() method that inserts all the items from one set into another:..  update() will exclude any duplicate items.
print(x)

z = x.union(y)                                       # You can use the union() method that returns a new set containing all items from both sets
print(z)




x = {"apple", "banana", "cherry,'Raspberry', 'Coconut', 'Malta', 'lemon'"}

x.remove("banana")                                   # To remove an item in a set, use the remove(), If the item to remove does not exist, remove() will raise an error.
print(x)

x.discard("apple")                                   # To remove an item in a set, use the discard().. If the item to remove does not exist, discard() will NOT raise an error.
print(x)


x = {"apple", "banana", "cherry"}                    # You can also use the pop(), method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.
z = x.pop()                                          # The return value of the pop() method is the removed item.
print(z)                                             # removed item
print(x)                                             # the set after removal



x = {"apple", "banana", "cherry"}
x.clear()
print(x)



x = {"apple", "banana", "cherry"}
del x
print(x)                                             # this will raise an error because the set no longer exists




'''
          Python has a set of built-in methods that you can use on sets.

        add()	                        Adds an element to the set
        clear()     	                Removes all the elements from the set
        copy()      	                Returns a copy of the set
        difference()	                Returns a set containing the difference between two or more sets
        difference_update() 	        Removes the items in this set that are also included in another, specified set
        discard()	                    Remove the specified item
        intersection()	                Returns a set, that is the intersection of two other sets
        intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
        isdisjoint()	                Returns whether two sets have a intersection or not
        issubset()	                    Returns whether another set contains this set or not
        issuperset()                    Returns whether this set contains another set or not
        pop()	                        Removes an element from the set
        remove()	                    Removes the specified element
        symmetric_difference()	        Returns a set with the symmetric differences of two sets
        symmetric_difference_update()	inserts the symmetric differences from this set and another
        union()	                        Return a set containing the union of sets
        update()	                    Update the set with the union of this set and others'''