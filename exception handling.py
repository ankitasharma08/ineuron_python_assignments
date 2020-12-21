#1. Write a function to compute 5/0 and use try/except to catch the exceptions.

def try_except(a,b):
    try:
        return a/b
    except ZeroDivisionError as ZE:
        print(ZE)
    except:
        print("Exception occur")
    else:
        print("Code run without exception ")

try_except(5,0)
    
    
#2. Implement a Python program to generate all sentences where subject is in
#["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
#["Baseball","cricket"].

subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]


for i in subjects:
    for j in verbs:
        for k in objects:
            print(i,j,k+".")