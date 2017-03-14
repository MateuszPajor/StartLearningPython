# Functional programming
def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5


print (apply_twice(add_five, 10))
# Pure functions - czyste funkcje - return a value that depends only on their arguments.
# example pure function
def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x+y)
print (pure_function(2, 3))
# example impure function
some_list = []

def impure(arg):
    some_list.append(arg)

# ----------------------------------------------------------------------------------------------------------------------
