#Write a Python program to print alphabet pattern'R'

a = list()
a.append("****")
for i in range(2):
    a.append("*   *")
a.append("****")

for i in range(3):
    line = "*" + (" " * (i+1)) +"*"
    a.append(line)

for i in range(len(a)):
    print(a[i])