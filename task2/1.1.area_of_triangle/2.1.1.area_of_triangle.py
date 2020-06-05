""""
1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.
"""

class perentclass:

    def __init__(s, n):
        s.no_of_sides = n

    def print_num_sides(s):
        print('No of side is ', format(s.no_of_sides ))
        
class side(perentclass):

    def __init__(s, lofsides):
        perentclass.__init__(s, 3)
        s.lofsides = lofsides 

    def area(s):
        
        a, b, c = s.lofsides

        s = (a + b + c) / 2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5
    

triagle = side([5,5,5])
print("Area is")
print(triagle.area())
print()
triagle.print_num_sides()
