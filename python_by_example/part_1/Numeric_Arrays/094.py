from array import *

nums = array('i', [3, 5, 1, 6, 8])

print(nums)

num = int(input("Select a number:  "))

while True:
    if num in nums:
        print(nums.index(num) + 1)
        break
    else:
        num = int(input("Wrong number, try again:  "))
