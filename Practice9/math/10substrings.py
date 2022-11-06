"""
A 10-substring of a number is a substring of its digits that sum to 10. For example, the 10-substrings of the number 3523014 are:
•	(352)3014
•	3(523)014
•	3(5230)14
•	35(23014)
A number is called 10-substring-friendly. if every one of its digits belongs to a 10-substring. For example, 3523014 is 10-substring-friendly, but 28546 is not.
Let T(n) be the number of 10-substring-friendly numbers from 1 to 10n(inclusive).
For example T(2) = 9 and T(5) = 3492.
"""

import math

def friendliness_check(n):
    ans_dict = {}
    str_n = str(n)
    for i in range(len(str_n)):
        if str_n[i] == "0": # they doesn't make sense but can ruin the code
            ans_dict[i] = True
        else: 
            ans_dict[i] = False 
    cnt = 0
    i = 0
    it_cnt = 0
    while it_cnt < len(str_n):
        while cnt<10:
            if i >= len(str_n):
                it_cnt = len(str_n)
                for k in range(len(ans_dict)):
                    if ans_dict[k] == False:
                        return False
                return True
                    
            else:
                cnt += int(str_n[i])
                i+= 1
        else:
            if cnt == 10:
                for j in range(it_cnt, i):
                    if ans_dict[j] != True:
                        ans_dict[j] = True
                it_cnt +=1
                i = it_cnt
                cnt = 0
            elif cnt > 10:
                it_cnt +=1
                i = it_cnt
                cnt = 0

def T(n):
    cnt = 0
    for i in range(1, int(math.pow(10, n))+1):
        if friendliness_check(i):
            cnt+=1
    return cnt


n = int(input("Enter your n: "))
            
print(T(n))


