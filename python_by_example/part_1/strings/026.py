word = input("Enter a word:  ")

w_l = len(word)
f_l = word[0]
r_w = word[1 : w_l]

if (f_l == 'a' or f_l == 'e' or f_l == 'i' or f_l == 'o' or f_l == 'u'):
    word = word + 'way'
    print(word.lower())
else:
    word = r_w + f_l + 'ay'
    print(word.lower())
