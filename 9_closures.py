# Python Closures
#  closure is a nested function that helps us access the outer function's variables
# even after the outer function is closed.

# Example 1

def greet():
    # variable defined outside the inner function
    name = "John"

    # return a nested anonymous function
    return lambda: "Hi " + name


# call the outer function
message = greet()

# call the inner function
print(message())

# Output: Hi John


# Example 2

def calculate():
    num = 1

    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func


# call the outer function
odd = calculate()

# call the inner function
print(odd())
print(odd())
print(odd())

# call the outer function again
odd2 = calculate()
print(odd2())
