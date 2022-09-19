"""
This cipher replaces every letter with a different letter. 
For instance every a might be replaced with an e, every b might be replaced with an a, etc. 
Write a program that asks the user to enter two strings. 
Then determine if the second string could be an encoded version of the ﬁrst one with a substitution cipher. 
For instance, CXYZ is not an encoded version of BOOK because O got mapped to two separate letters. 
Also, CXXK is not an encoded version of BOOK, because K got mapped to itself. On the other hand, CXXZ would be an encoding of BOOK. 
This problem can be done with or without a dictionary.
"""

word = input()
cipher = input()

def check(word, cipher):
    d = {}
    for i in range(len(word)):
        if word[i] == cipher[i]:
            return False
        elif word[i] in d.keys():
            if d[word[i]] == cipher[i]:
                pass
            else:
                return False
        else:
            d[word[i]] = cipher[i]
        
    return True

print(check(word, cipher))
   
