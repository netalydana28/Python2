"""
Write a function called findall that given a string and a single character, 
returns a list containing all of the locations of that character in the string. 
It should return an empty list if there are no occurrences of the character in the string
"""

word = input()
target = input()

def findall(word, target):
    ans = list()
    cnt = -1
    for i in word:
        cnt+=1
        if target == i:
            ans.append(cnt)
    return ans

print(findall(word, target))