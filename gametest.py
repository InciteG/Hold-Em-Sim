dict = {
1 : [41,42],
3 : [21,25],
6 : [65, 22]
}
v= 3

for (k,s) in dict.items():
    if v == k:
        value = s[0]
        suit = s[1]
        print(value,suit)
