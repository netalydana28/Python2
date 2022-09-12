"""
Write a Python program that prints each item and its corresponding type from the following list.
SampleList: datalist = [1452, 11.23, 1+2j, True,'student', (0, -1), [5,12], {"class":'V', "section":'A'}]
"""
datalist = [1452, 11.23, 1+2j, True,'student', (0, -1), [5,12], {"class":'V', "section":'A'}]
for i in range(len(datalist)):
    print(f"item: {datalist[i]}  type: {type(datalist[i])}")