import time
import sys
from random import *

sm_min = 1
sm_max = 1000
md_min = sm_max+1
md_max = 100000
lg_min = md_max+1
lg_max = 1000000

print("----------------------------------------")
print("CS2223 Project 1 | Jonathan Gaines")
print("\n1 - Small Set (" + str(sm_min)+ " - " + str(sm_max) + ")")
print("2 - Medium Set (" + str(md_min) + " - " + str(md_max) + ")")  
print("3 - Large Set (" + str(lg_min) + " - " + str(lg_max) + ")")

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

def effBF(dataset):
    start = time.time()
    bubblesort(dataset)
    end = time.time()
    print("Brute Force: " + str(end-start))


def run_algs(setVal):
    if int(setVal) == 1:
        sm_val = randint(sm_min, sm_max)
        alist = gen_rand_list(sm_val)
    elif int(setVal) == 2:
        md_val = randint(md_min, md_max)
        alist = gen_rand_list(md_val)
    elif int(setVal) == 3:
        lg_val = randint(lg_min, lg_max)
        alist = gen_rand_list(lg_val)
    
    effDC(alist)
    effBF(alist)
    print("***********************************")

setSize = 0
while int(setSize) != -1:
   
    print("\nEnter 1, 2, 3, or -1 to quit")
    setSize = input("Choose a set size: ")
    
    if int(setSize) != -1: 
        run_algs(setSize)

