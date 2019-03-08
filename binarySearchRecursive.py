# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 12:40:31 2018

@author: b
"""

def binarySearch(L, e, start, end):
    if start > end:
        return False
    else:
        mid = (start + end) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            return binarySearch(L, e, start, mid - 1)
        else:
            return binarySearch(L, e, mid + 1, end)

mylist = [5, 7, 9, 12, 15]
searchValue = 7

for searchValue in [7, 18, 6, 15]:
    if not binarySearch(mylist, searchValue, 0, len(mylist)-1):
        print(searchValue, 'does not exist')
    else:
        print(searchValue,'exists')
