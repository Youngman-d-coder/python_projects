nums = []
count = 0

while (count < 3):
    num = int(input("Enter a number: "))
    nums.append(num)
    print(nums)
    count += 1
wish = input("Do wish the last number to be saved (y/n): ")
if (wish == 'n'):
    nums.remove(num)
print(nums)
