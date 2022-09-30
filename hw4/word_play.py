"""
Write a class called Wordplay. It should have a ﬁeld that holds a list of words. 
The user of the class should pass the list of words they want to use to the class. There should be the following methods:

• words_with_length(length) — returns a list of all the words of length length

• starts_with(s) — returns a list of all the words that start with s

• ends_with(s) — returns a list of all the words that end with s

• palindromes() — returns a list of all the palindromes in the list

• only(L) — returns a list of the words that contain only those letters in L

• avoids(L) — returns a list of the words that contain none of the letters in L
"""

class Wordplay:
    def __init__(self, words):
        self.words = words

    def words_with_length(self, n):
        ans = list()
        for i in range(len(self.words)):
            if len(self.words[i]) == n:
                ans.append(self.words[i])
        return ans

    def starts_with(self, s):
        ans = list()
        for i in range(len(self.words)):
            if self.words[i][0] == s:
                ans.append(self.words[i])
        return ans

    def ends_with(self, s):
        ans = list()
        for i in range(len(self.words)):
            if self.words[i][len(self.words[i])-1] == s:
                ans.append(self.words[i])
        return ans
    
    def palindromes(self):
        ans = list()
        for i in range(len(self.words)):
            if self.words[i] == self.words[i][::-1]:
                ans.append(self.words[i])
        return ans

    def only(self, s):
        ans = list()
        for i in range(len(self.words)):
            if s in self.words[i]:
                ans.append(self.words[i])
        return ans

    def avoid(self, s):
        ans = list()
        for i in range(len(self.words)):
            if s not in self.words[i]:
                ans.append(self.words[i])
        return ans
    
with open("word_list.txt", "r") as words:
    word_list = words.read().split("\n")
    to_play = Wordplay(word_list)

print(f"A list of all the words of length 4:\n  {to_play.words_with_length(4)}")
print(f"A list of all the words that start with a:\n  {to_play.starts_with('a')}")
print(f"A list of all the words that ends with n:\n  {to_play.ends_with('n')}")
print(f"Palidromes:\n  {to_play.palindromes()}")
print(f"A list of the words that contain m letter:\n  {to_play.only('m')} ")
print(f"A list of the words that contain none of o letter:\n  {to_play.avoid('o')} ")
