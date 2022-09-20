"""
4 - Suppose you are given the following list of strings:
L = ['aabaabac', 'cabaabca', 'aaabbcba', 'aabacbab', 'acababba']
Patterns like this show up in many places, including DNAsequencing. 
The user has a string of their own with only some letters ﬁlled in and the rest as asterisks.
An example is a**a****. The user would like to know which of the strings in the list ﬁt with their pattern. 
In the example just given, the matching strings are the ﬁrst and fourth. (1 point)
One way to solve this problem is to create a dictionary whose keys are the indices in the user’s string of the non-asterisk characters and whose values are those characters.
Write a program implementing this approach (or some other approach) to ﬁnd the strings that match a user-entered string.
"""

L = eval(input())
pattern = input()

def check(word, pattern):
    if len(word) != len(pattern):
        return False
    else:
        for i in range(len(word)):
            if word[i]==pattern[i]:
                pass
            elif pattern[i] == "*":
                pass
            else:
                return False
    return True

for i in range(len(L)):
    print(f"{L[i]} --> {check(L[i], pattern)}")