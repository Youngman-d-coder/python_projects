from array import *

integers = array('i', [])

for i in range(5):
    integer = int(input("Enter an integer: "))
    integers.append(integer)

integers = sorted(integers)
integers.reverse()
print(integers)
