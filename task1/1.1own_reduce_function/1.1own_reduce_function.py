
"""
Problem Statement​ ​1:
Write a Python Program to implement your own myreduce() function which works exactly like
Python's built-in function reduce()

"""


# Reduce will produce a single result
def myreduce(anyfunc, sequence):
    # Get first item in sequence and assign to result
    result = sequence[0]
    # iterate over remaining items in sequence and apply reduction function
    for item in sequence[1:]:
        result = anyfunc(result, item)

    return result

# test myreduce function
def sum(x, y): return x + y


print("Sum on list [1,2,3] using custom reduce function " + str(myreduce(sum, [1, 2, 3])))

