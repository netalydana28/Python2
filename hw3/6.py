"""
Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes.
INVALIDS are:
42536258796157867 #17 digits in card number → Invalid                          done
4424444424442444 #Consecutive digits are repeating 4 or more times → Invalid   done
5122-2368-7954 - 3214 #Separators other than '-' are used → Invalid            done
44244x4424442444 #Contains non digit characters → Invalid                      done
0525362587961578 #Doesn't start with 4, 5 or 6 → Invalid                       done

Sample Input
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Sample Output

Valid
Valid
Invalid
Valid
Invalid
Invalid
"""
import re

n = int(input())
cards = list()

for i in range(n):
    temp = input()
    cards.append(temp)

def validity(card_num):
    if re.findall("-", card_num):
        if re.findall("[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{4}", card_num):
            card_num = re.sub("-", "", card_num)
            
        else:
            return False
    if not len(card_num) == 16:
        #print("len != 17")
        return False
    else:
        try: 
            int(card_num)
        except:
            #print("has no digit characters")
            return False
        else:
            if card_num[0] == "4" or card_num[0] == "5" or card_num[0] == "6":
                for i in card_num:
                    temp = i + "{" + "4,}"
                    if re.findall(f"{temp}", card_num):
                        #print(f"{i} ocurs more than 4 times")
                        return False
                else:

                    return True

for i in range(n):
    if validity(cards[i]):
        print("VALID")
    else:
        print("INVALID")