my_dict = {}

for i in range(4):
    name = input("Enter a name:  ")
    age = int(input("Enter age:  "))
    shoe_size = int(input("Enter shoe size:  "))
    my_dict[name] = {"Age":age, "Shoe size":shoe_size}

for n in my_dict:
    print((n), my_dict[n] ["Age"])
