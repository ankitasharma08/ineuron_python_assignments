#1 Create the below pattern using nested for loop in Python.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

for i in range(0,5):
    for j in range(0,i+1):
        print("* ",end="") 
    print("\r")   
    
for i in range(5,0,-1):
    for j in range(0,i-1):
        print("* ",end="") 
    print("\r")


#2. Write a Python program to reverse a word after accepting the input from the user.

Comany_Name = input("Input Word: ")
print("Output Word: ",Comany_Name[::-1])