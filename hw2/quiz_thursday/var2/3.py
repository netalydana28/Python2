#Please write a program which count and print the numbers of each character in a string input by console

a = input()

def count(a):
    d = {}
    for i in range(len(a)):
        if a[i] in d.keys():
            d[a[i]]+=1
        else:
            d[a[i]] = 1
    return d

print(count(a))