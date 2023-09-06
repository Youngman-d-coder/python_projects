my_dict = {"John":{"N":3056,"S":8463,"E":8441, "W":2694},
        "Tom":{"N":4832,"S":6786, "E":4737, "W":3612},
        "Anne":{"N":5239, "S":4802, "E":5820, "W":1859},
        "Fiona":{"N":3904, "S":3645, "E":8821, "W":2451}}

for i in my_dict:
    print(i)

name = input("Enter a name:  ")

for x in my_dict[name]:
    print(x)

region = input("Enter a region:  ")

print(my_dict[name] [region])

print("Enter name and region you want to alter")

name = input("Enter a name:  ")
region = input("Enter a region:  ")
new_data = int(input("Enter new data:  "))

my_dict[name] [region] = new_data

print(my_dict[name])

