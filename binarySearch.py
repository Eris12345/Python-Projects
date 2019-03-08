# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 11:00:46 2018

@author: user
"""

def binary_search(L, e):
    first, last = 0, len(L)-1
    while first <= last:
        mid = (first + last) // 2
        if e < L[mid]:
            last = mid - 1
        elif e > L[mid]:
            first = mid + 1
        else:
            return mid
    return None

myList = [5, 7, 2, 6, 3]
myList.sort() 
print('sorted list:', myList)

for searchValue in [7, 8, 6, 3, 1]:
    pos = binary_search(myList, searchValue)
    if pos == None:
        print(searchValue, 'does not exist')
    else:
        print(searchValue,'exists at index', pos)

