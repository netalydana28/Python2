"""
Write a Python program to combine each line from first file with the corresponding line in second file. 
And the output should be written into another third file.
"""

with open("students.txt", "r") as st1:
    stud_list1 = list(st1.read().split("\n"))

with open("students2.txt", "r") as st2:
    stud_list2 = list(st2.read().split("\n"))


#with open("students.txt", "r") as st3:

with open("strudent3.txt", "w") as st3:
    for i in range(len(stud_list1)):
        ans = f"{stud_list1[i]} --- {stud_list2[i]}"
        st3.write(ans + "\n")



