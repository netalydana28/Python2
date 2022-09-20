"""
Create a program that takes two strings and determines if an anagram of the first string is in the second string.
Anagrams of "bag" are "bag", "bga", "abg", "agb", "gab", "gba". 
Since none of those anagrams are in "grab", the answer is false.
A "g", "a", and "b" are in the string "grab", but they're split up by the "r".
Examples
ana_str_str("car", "race") ➞ True
ana_str_str("nod", "done") ➞ True
ana_str_str("bag", "grab") ➞ False
"""

str1 = input()
str2 = input()

ans = []
 
def anagrams(str1, i, length):
    if i == length:
        ans.append(''.join(str1) )
    else:
        for j in range(i, length):
            str1[i], str1[j] = str1[j], str1[i]
            anagrams(str1, i + 1, length)
            str1[i], str1[j] = str1[j], str1[i] 

anagrams(list(str1), 0, len(str1))

def check(ans, str2):
    for i in range(len(ans)):
        if ans[i] in str2:
            return True

    return False

print(f"str1, str2 ---> {check(ans, str2)}")

"""
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*(n-1)

def anagrams(str1):
    ans = set()
    temp = ""
    for i in range(len(str1)+1):
        for j in range(len(str1)-1):
            temp += str1[j]
            print(f"temp: {temp}")
        print(str1[len(str1)-1]) 
        str1 = str1[len(str1)-1] + temp 
        print(str1[len(str1)-1]) 
        ans.add(str1)
        temp=""
        
    if len(ans) == factorial(len(str1)):
        return ans
    else:
        anagrams(str1[::-1])

ans = anagrams(str1)

print(ans)
print(factorial(4))
"""