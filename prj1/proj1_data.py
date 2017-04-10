import time
import sys
import csv
from random import *

def bubblesort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def partition(alist, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if alist[i] <= alist[begin]:
            pivot += 1
            alist[i], alist[pivot] = alist[pivot], alist[i]
    
    alist[pivot], alist[begin] = alist[begin], alist[pivot]
    return pivot

def quicksort(alist, begin=0, end=None):
    if end is None:
        end = len(alist) - 1
    def _quicksort(alist, begin, end):
        if begin >= end:
            return
        pivot = partition(alist, begin, end)
        _quicksort(alist, begin, pivot-1)
        _quicksort(alist, pivot+1, end)

    return _quicksort(alist, begin, end)

def gen_rand_list(length):
    print("\nConstructing Dataset . . .")
    print("Dataset Size: " + str(length))

    x = []
    for i in range(0, length):
        new_val = randint(0, sys.maxsize/4)
        x.extend([new_val])

    print("Dataset Constructed, running benchmarks. . . \n")
    return x

def effDC(dataset):
    start = time.time()
    quicksort(dataset)
    end = time.time()
    print("Divide & Conquer: " + str(end-start))
    return end-start

def effBF(dataset):
    start = time.time()
    bubblesort(dataset)
    end = time.time()
    print("Brute Force: " + str(end-start))
    return end-start

def run_algs(size):
    alist = gen_rand_list(size)
    dc_val = effDC(alist)
    bf_val = effBF(alist)
    print("***********************************")
    row_vals = [size, dc_val, bf_val]
    out.writerow(row_vals)

column_names = ["Set Size", "DC", "BF"]
out = csv.writer(open("data.csv", "w"), delimiter=',', quoting=csv.QUOTE_ALL)
'out.writerow(column_names)'
curr_size = 10
while curr_size <= 100000:      
    run_algs(curr_size)
    if(curr_size < 1000):
        curr_size+=10
    elif(curr_size < 10000):
        curr_size+=100
    elif(curr_size < 100000):
        curr_size+=1000
    else:
        print("Overflow of dataset occured")



