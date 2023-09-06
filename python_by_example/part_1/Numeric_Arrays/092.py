from array import *
import random

var_arr_1 = array('i', [])
var_arr_2 = array('i', [])

for i in range(5):
    n = random.randint(1, 10)
    var_arr_1.append(n)

for x in range(3):
    m = int(input("Enter a number:  "))
    var_arr_2.append(m)

large_arr = var_arr_1 + var_arr_2
large_arr = sorted(large_arr)

for y in large_arr:
    print(y)
