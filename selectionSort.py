# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 13:44:17 2018

@author: b
"""

# this version swaps smaller values with the one at index suffixStart
def selectionSort1(L):
    """Assumes that L is a list of elements that can be
         compared using >.
       Sorts L in ascending order"""
    suffixStart = 0
    while suffixStart != len(L):
        #look at each element in suffix
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                #swap position of elements
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1

# this version swaps smaller values with the one at index suffixStart
def selectionSort2(L):    
    for suffixStart in range(len(L)):
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                L[suffixStart], L[i] = L[i], L[suffixStart]        

# this version locates the min element after suffixStart
# and swaps the min element with the one at index suffixStart 
def selectionSort3(L):
    for suffixStart in range(len(L)):
        minIndex = suffixStart       
        for i in range(suffixStart + 1, len(L)):
            if L[i] < L[minIndex]:
                minIndex = i   
        L[suffixStart], L[minIndex] = L[minIndex], L[suffixStart]       


# myList = [5, 7, 2, 6, 3, 9, 1]
myList = [8, 0, 5, 7, 2, 6, 3, 9, 1, 4]
print('unsorted list:', myList)

selectionSort3(myList)
print('sorted list:', myList)
