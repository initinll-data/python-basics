# Nested Function
# We can include one function inside another, known as a nested function.

def outer(x):
    def inner(y):
        return x + y
    return inner


add_five = outer(5)
result = add_five(6)
print(result)  # prints 11


# Output: 11

# Pass Function as Argument
# We can pass a function as an argument to another function in Python.


def add(x, y):
    return x + y


def calculate(func, x, y):
    return func(x, y)


result = calculate(add, 4, 6)
print(result)  # prints 10


# Return a Function as a Value
# In Python, we can also return a function as a return value.

def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello


greet = greeting("Atlantis")
print(greet())  # prints "Hello, Atlantis!"

# Output: Hello, Atlantis!


# Python Decorators

# A decorator takes in a function, adds some functionality and returns it.

def make_pretty1(func):
    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function


def ordinary1():
    print("I am ordinary")


# decorate the ordinary function
decorated_func = make_pretty1(ordinary1)

# call the decorated function
decorated_func()


# @ Symbol With Decorator
# Instead of assigning the function call to a variable,
# Python provides a much more elegant way to achieve this functionality using the @ symbol.

def make_pretty2(func):

    def inner():
        print("I got decorated")
        func()
    return inner


@make_pretty2
def ordinary2():
    print("I am ordinary")


ordinary2()


# Decorating Functions with Parameters


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


divide(2, 5)

divide(2, 0)


# Chaining Decorators in Python

# Multiple decorators can be chained in Python.
# To chain decorators in Python, we can apply multiple decorators
# to a single function by placing them one after the other,
# with the most inner decorator being applied first.

def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer(msg):
    print(msg)

# above syntax is equivalent to - printer = star(percent(printer))


printer("Hello")
