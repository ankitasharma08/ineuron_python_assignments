#1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
#formula.
#area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#Function to take the length of the sides of triangle from user should be defined in the parent
#class and function to calculate the area should be defined in subclass.

class triangle_parent:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: ')) 

class triangle_child(triangle_parent):
    def __init__(self, a, b,c):
        super().__init__(a, b, c)
    def area(self):    
        s = (a+b+c)/2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5
    
p1 = triangle_child(a,b,c)
print("area : {}".format(p1.area()))     

#1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
#the list of words that are longer than n.

def filter_long_words(lst,n):
    long_list = []
    for i in lst:
        if len(i) > n:
            long_list.append(i)
    
    return long_list
    
filter_long_words(["hey","what","where","hi"],2)


#2.1 Write a Python program using function concept that maps list of words into a list of integers
#representing the lengths of the corresponding words.

def return_length(lst):
    length_list = []
    for i in lst:
        length_list.append(len(i))
    return length_list

return_length(["whats","up"])

#using Map
result = map(lambda x : len(x),["hey","wowoo"])
list(result)

#2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
#it is a vowel, False otherwise.

def vowel(character):
    vowels_list = ["a","e","i","o","u"]
    if(character in vowels_list):
        return True
    else:
        return False
vowel("a")