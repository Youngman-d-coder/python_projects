countries = ("Ghana", "Niger", "Spain", "Mali", "Togo")

for i in countries:
    print(i)

count_inp = input("Enter a country you liked  from the list:  ").capitalize()

ans = countries.index(count_inp)

print(ans)
