"""
Write a program that rotates the element so that the element at the ﬁrst index moves to the second index, 
the element in the second index moves to the third index, etc., and the element in the last index moves to the ﬁrst index. 
Print out result.

String
"""

word = input()

def rotate_string(word):
    ans = word[len(word)-1]
    for i in range(len(word)-1):
        ans+= word[i]
    return ans


print(rotate_string(word))
