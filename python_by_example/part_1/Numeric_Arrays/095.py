from array import *

nums_1 = array('f', [90.78, 60.53, 52.92, 73.66, 48.51])

num = int(input("Enter a number between 2 and 5:  "))

while True:
    if num >= 2 and num <= 5:
        for i in nums_1:
            ans = i / num
            print(round(ans, 2))
        break
    else:
        print("Invalid Input, Try again!")
