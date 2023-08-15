#!/usr/bin/python3
from array import *

nums = array('i',[])

while (len(nums) < 6):
    num = int(input("Enter a number :  "))
    if num > 10 and num < 20:
        nums.append(num)
    else:
        print("Outside the range")

print("Thank you!")
for i in nums:
    print(i)
