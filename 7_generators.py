# Python Generators

# In Python, a generator is a function that returns an iterator that produces
# a sequence of values when iterated over.

# Generators are useful when we want to produce a large sequence of values,
# but we don't want to store all of them in memory at once.

# Create Python Generator
# def generator_name(arg):
#     # statements
#     yield something

def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1


# iterate over the generator object produced by my_generator
for value in my_generator(3):

    # print each value produced by generator
    print(value)

# We can also create a generator object from the generator function by
# calling the function like we would any other function as,

generator = iter([1, 2, 3])
print(next(generator))  # 0
print(next(generator))  # 1
print(next(generator))  # 2

# Python Generator Expression
# (expression for item in iterable)

# create the generator object
squares_generator = (i * i for i in range(5))

# iterate over the generator and print the values
for i in squares_generator:
    print(i)
