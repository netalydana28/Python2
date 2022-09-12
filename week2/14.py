#Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.

integers = list()
statement = True
while statement:
    a = int(input()) 
    if a == 0:
        statement = False
    else:
        integers.append(a)

sum_int = 0
for i in range(len(integers)):
    sum_int += integers[i]

print(f"sum: {sum_int} \n average: {sum_int/len(integers)}")