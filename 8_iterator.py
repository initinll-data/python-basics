# Python Iterators
# Iterators are methods that iterate collections like lists, tuples, etc.
# Using an iterator method, we can loop through an object and return its elements.

# Technically, a Python iterator object must implement two special methods,
# __iter__() and __next__(), collectively called the iterator protocol.

# Iterating Through an Iterator
# In Python, we can use the next() function to return the next item in the sequence.

# define a list
my_list = [4, 7, 0]

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))  # prints 4

# get the second element of the iterator
print(next(iterator))  # prints 7

# get the third element of the iterator
print(next(iterator))  # prints 0


# Using for Loop
# A more elegant way of automatically iterating is by using the for loop.

# define a list
my_list = [4, 7, 0]

for element in my_list:
    print(element)

# Working of for loop for Iterators
# The for loop in Python is used to iterate over a sequence of elements,
# such as a list, tuple, or string.

# create a list of integers
my_list = [1, 2, 3, 4, 5]

# create an iterator from the list
iterator = iter(my_list)

# iterate through the elements of the iterator
for element in iterator:

    # Print each element
    print(element)
