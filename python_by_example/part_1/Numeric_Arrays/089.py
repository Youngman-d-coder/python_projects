from array import *
import random

nums = array('i', [])

for i in range(5):
    num = random.randint(1, 99)
    nums.append(num)

for num in nums:
    print(num)
