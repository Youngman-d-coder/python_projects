post_code = input("Enter post code:  ")
length = len(post_code)
start = post_code[0 : 2]
start = start.upper()
end = post_code[2 : length]
postcode = start + end
print(postcode)
