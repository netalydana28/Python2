"""
1. Wordplay – Use the ﬁle wordlist.txt (write big enough text) for this problem. Find the following:
(a) All words ending in ime
(b) All words whose second, third, and fourth letters are ave
(c) How many words contain at least one of the letters r, s, t, l, n, e
(d) The percentage of words that contain at least one of the letters r, s, t, l, n
(e) All words with no vowels
(f) All words that contain every vowel
"""
import re

with open("wordlist.txt", "r") as wl:
    wl_list = wl.read().split("\n")
    a, b, c, d, e, f = list(), list(), 0, 0, list(), list()
    for each in wl_list:
        if re.findall("ime$", each):
            a.append(each)
        if re.findall(".ave", each):
            b.append(each)
        if re.findall("r", each) or re.findall("s", each) or re.findall("t", each) or re.findall("l", each) or re.findall("n", each) or re.findall("e", each):
            c+=1
        if re.findall("r", each) or re.findall("s", each) or re.findall("t", each) or re.findall("l", each) or re.findall("n", each):
            d+=1
        if not re.findall("e", each) and not re.findall("u", each) and not re.findall("o", each) and not re.findall("a", each) and not re.findall("i", each) and not re.findall("y", each):
            e.append(each)
        if re.findall("e", each) and re.findall("u", each) and re.findall("o", each) and re.findall("a", each) and re.findall("i", each) and re.findall("y", each):
            f.append(each)

    print(f"All words ending in ime: {a}")
    print(f"All words whose second, third, and fourth letters are ave: {b}")
    print(f"How many words contain at least one of the letters r, s, t, l, n, e: {c}")
    print(f"The percentage of words that contain at least one of the letters r, s, t, l, n: {int(d/len(wl_list) * 100)}%")
    print(f"All words with no vowels: {e}")
    print(f"All words that contain every vowel: {f}")