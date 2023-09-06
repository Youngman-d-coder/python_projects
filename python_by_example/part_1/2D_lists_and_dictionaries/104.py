my_dict = {}

for i in range(4):
    name = input("Enter a name:  ")
    age = int(input("Enter age:  "))
    shoe_size = int(input("Enter shoe size:  "))
    my_dict[name] = {"Age":age, "Shoe size":shoe_size}

rid = input("Who do you not want anymore:  ")
del my_dict[rid]

for name in my_dict:
    print((name), my_dict[name] ["Age"], my_dict[name] ["Shoe size"])
