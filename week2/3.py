"""
Write a Python program to calculate a dog's agein dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years.
After that, each dog year equals 4 human years.
Expected Output:Input a dog's age in human years: 15
The dog's age in dog's years is 73
"""

age = int(input("Input a dog's age in human years: "))
ans = 0
if age > 2:
    after2 = age - 2
    print(f"The dog's age in dog's years is {21 + 4 * after2}")
else:
    print(f"The dog's age in dog's years is {int(age * 10.5)}")