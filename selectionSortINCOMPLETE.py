import random
import time
import sys
import numpy as np
import matplotlib as plt

def createRandomIntList(numInts,xMin=-50,xMax=50):
    listOfInts=[]

    for i in range(numInts):
        listOfInts.append(random.randint(xMin,xMax))

    return listOfInts

def findMaximumValuePosition(l,end):
    #TASK A: TO DO IMPLEMENT LOOP TO RETURN THE POSITION OF THE MAXIMUM VALUE BETWEEN 0 AND END
    max_list = max(l)
    return(l.index(max_list))

def swapValuesInList(l,i,j):
    #TASK B: TO DO implement function that swaps values in positions i and j in l.
    l[i],l[j]=l[j],l[i]

#TaskB1
def bubbleUp(l,end):
    for i in range(end):
        for j in range(end-1,i,-1):
            if l[j-1]>l[j]:
                swapValuesInList(l,j-1,j)
    return l

def binarySearch(l,x):
    if x in l:
        return(l.index(x))
    else:
        return("-1")


if __name__=="__main__":
    data_points = 50
    selection_sort=[]
    bubble_sort = []
    binary_search = []
    for i in range(data_points):
        #TASK C: Modify this value and make a table with the output times
        n=10000

        #O(n), create a list of integers
        start = time.time()
        myList=createRandomIntList(n)
        end = time.time()
        # print("finished data generation with Linear ( O(n) )  complexity in (TIME 1) "+str(end - start))

        mySecondList = list(myList)

        #O(1)
        start = time.time()
        randomIndex=random.randint(0,n-1)
        randomListValue=myList[randomIndex]
        end = time.time()
        # print("finished accessing random data with constant O(1) complexity in (TIME 2) "+str(end - start))

        #O(n*n)
        start = time.time()
        i=n-1
        while i>0:
            maximumIndex=findMaximumValuePosition(myList,i)
            swapValuesInList(myList,i,maximumIndex)
            i=i-1
        end = time.time()
        selection_sort.append(end - start)
        print("finished sorting list with quadratic O(n*n) complexity in (TIME 3) "+str(end - start))

        #taskB2
        start = time.time()
        sortedList = bubbleUp(mySecondList,n)
        end = time.time()
        bubble_sort.append(end - start)
        print("finished bubble sorting complexity in (TIME 4) "+str(end - start))

        #taskC
        randx = random.randint(-50,50)
        start = time.time()
        binary = binarySearch(sortedList,randx)
        end = time.time()

        binary_search = []
        print(binary)
        print("finished binary search complexity in (TIME 5) "+str(end - start))
        i += 1


    selectmean = np.mean(selection_sort)
    print(selectmean)
    bubblemean = np.mean(bubble_sort)
    print(bubblemean)
    binarymean = np.mean(binary_search)
    print(binarymean)

