#1.1 Write a Python Program to implement your own myreduce() function which works exactly
#like Python's built-in function reduce()

def myreduce(n):
    lst = list(range(0,n+1))
    add = 0
    
    for i in lst:
        add = add+i
    return add

myreduce(7)    


#1.2 Write a Python program to implement your own myfilter() function which works exactly
#like Python's built-in function filter()
def myfilter(n):
    lst = list(range(0,n+1))
    even_lst =[]
    odd_lst =[]

    for i in lst:
        if i%2 == 0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
            
    return even_lst,odd_lst
output = myfilter(9)
print("Even No List:",output[0])  
print("Odd No List:",output[1])   


#2. Implement List comprehensions to produce the following lists.
#Write List comprehensions to produce the following Lists
#['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
#['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
#['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
#[[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
#[4, 5, 6, 7], [5, 6, 7, 8]]
#[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

word ='ACADGILD'
lst = [i for i in list(word)]
lst

lst_1 =list('xyz')
lst_2 =[i*n for i in lst_1 for n in range(1,5)]
lst_2

lst_3=[i*n for i in range(1,5) for n in lst_1 ]
lst_3

lst_4 = [2,3,4]
lst_5 = [[i+n] for i in lst_4 for n in range(0,3)]
lst_5

lst_6 = [2,3,4,5]
lst_7 = [[i+n for i in range(0,4)] for n in lst_6 ]
lst_7

lst_8 = [1,2,3]
lst_9 = [(j,i) for i in lst_8 for j in lst_8]
lst_9
