# -*- coding: utf-8 -*-

def bubbleSort1(L):    
    for passnum in range(0, len(L)):
        for i in range(len(L) - passnum -1):    
            if L[i] > L[i+1]:
                 L[i], L[i+1] =  L[i+1], L[i]
#                temp = L[i]
#                L[i] = L[i+1]
#                L[i+1] = temp


# A bubble sort can be modified to stop early if it finds 
# that the list has become sorted. 
def bubbleSort2(L):
    issorted = False
    passnum = 0
    while passnum < len(L)-1 and not issorted:
        issorted = True
        for k in range(len(L)-passnum-1):
            if L[k] > L[k+1]:
                issorted = False
                L[k], L[k+1] =  L[k+1], L[k]
        passnum += 1      
    

  
myList = [5, 7, 2, 6, 3, 9, 1]               
# myList = [8, 0, 5, 7, 2, 6, 3, 9, 1, 4]
print('unsorted list:', myList)

bubbleSort2(myList)
print('sorted list:', myList)



