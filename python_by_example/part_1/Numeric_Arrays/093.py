from array import *

nums = array('i', [])
numb = array('i', [])

for i in range(5):
    num = int(input("Enter a number:  "))
    nums.append(num)

nums = sorted(nums)

print(nums)

n = int(input("Select a number:  "))

numb.append(n)
nums.remove(n)

print(nums)
print(numb)
