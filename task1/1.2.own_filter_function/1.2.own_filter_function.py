
"""
Problem Statement​ ​2:
Write a Python program to implement your own myfilter() function which works exactly like
Python's built-in function filter()
"""



# Custom filter function
def myfilter(anyfunc, sequence):
    # Initialize empty list
    result = []
    # iterate over sequence of items in sequence and apply filter function
    for item in sequence:
        if anyfunc(item):
            result.append(item)

    # return funal output
    return result

# test myfilter function
def ispositive(x):
    if (x <= 0):
        return False
    else:
        return True

print("Filter only positive Integers on list [0,1,-2,3,4,5] using custom filter function" + str(
    myfilter(ispositive, [0, 1, -2, 3, 4, 5])))