import time
import sys
from random import *

sm_min = 1
sm_max = 1000
md_min = sm_max+1
md_max = 100000
lg_min = md_max+1
lg_max = 10000000

print("----------------------------------------")
print("CS2223 Project 1 | Jonathan Gaines")
print("\n1 - Small Set (" + str(sm_min)+ " - " + str(sm_max) + ")")
print("2 - Medium Set (" + str(md_min) + " - " + str(md_max) + ")")  
print("3 - Large Set (" + str(lg_min) + " - " + str(lg_max) + ")")
   
def gen_rand_list(length):
    print("\nConstructing Dataset . . .")
    print("Dataset Size: " + str(length) + "\n")

    x = []
    for i in range(0, length):
        new_val = randint(0, sys.maxsize/4)
        x.extend([new_val])
    return x

def effDC(dataset):
    start = time.time()
    search_dc()
    end = time.time()
    print("Divide & Conquer: " + str(end-start))

def effBF(dataset):
    start = time.time()
    search_bf()
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

