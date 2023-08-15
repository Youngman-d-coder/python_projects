#!/usr/bin/python3

from array import *

nums = array('i', [2,4,2,5,4])

for i in nums:
    print(i)

num = int(input("Enter a number from the array :  "))

count = 0

for i in nums:
    if i == num:
        count += 1

print(f"{i} appears in the array {count} times")
