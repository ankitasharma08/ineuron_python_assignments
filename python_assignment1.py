#1
for i in range(2000,3201):
    if(i%7==0):
        if(i%5==0):
            continue
        print(i,end=',')
        
#2
first_name = input("Enter First Name:")
Last_name = input("Enter Last Name:")
print(first_name[::-1]+" "+Last_name[::-1])

#3
pi = 3.1415926535897931
r= 12.0
V= 4/3*pi*r**3
print('Volume of Sphare is',V)