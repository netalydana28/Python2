"""
Write a program that rotates the element so that the element at the ﬁrst index moves to the second index, 
the element in the second index moves to the third index, etc., and the element in the last index moves to the ﬁrst index. 
Print out result.

List
"""
input_list = eval(input())

def rotate_list(input_list):
    ans = list()
    ans.append(input_list[len(input_list)-1])
    for i in range(len(input_list)-1):
        ans.append(input_list[i])
    return ans

print(rotate_list(input_list))