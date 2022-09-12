#Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

int1 = int(input("Input first integer: "))
int2 = int(input("Input second integer: "))
ans = int1 + int2
if ans <= 20 and ans >= 15:
    print(20)
else:
    print(ans)
