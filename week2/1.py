#Write a Python program to print alphabet pattern 'O'.

a = list()
a.append(" *** ")
for i in range(5):
    a.append("*   *")
a.append(" *** ")

for i in range(len(a)):
    print(a[i])