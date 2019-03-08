# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 10:46:45 2018

@author: user
"""

# assumption -- L is unsorted
def linear_search(L, e):
    found = False
    for i in range(len(L)):
        if e == L[i]:
            found = True
    return found

# assumption -- L is sorted
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


myList = [5, 7, 2, 6, 3]
sVal = 6
inList = linear_search(myList, sVal)
print(sVal, 'exists in list: ', inList)
sVal = 4
inList = linear_search(myList, sVal)
print(sVal, 'exists in list: ', inList)

myList.sort()
print('sorted list:', myList)
sVal = 6
inList = search(myList, sVal)
print(sVal, 'exists in list: ', inList)