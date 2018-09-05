#Q.1- Write a python program to print the cube of each value of a list using list comprehension.
l1=[1,2,3,4]
l2=[i**3 for i in l1]
print(l2)

#Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension.
lst=[i for i in range(2,20) if all(i%j!=0 for j in range(2,i))]
print(lst)

#Q.3- Write the main differences between List Comprehension and Generator Expression.
'''
The difference between List Comprehension and Generator Expression is:
1. Syntax Differences- In list comprehension we use [] but in generator expression we use ()
2. List comprehension stores the values in the form of a list but generator expression yields one item at a time so we need to use iterator
when printing items through generator expressions.
3.Memory occupied by generator expressions is less than that occupied through list comprehensions.
'''

'''  Lambda & MAP  '''
#Q.1- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
Celsius = [39.2, 36.5, 37.3, 37.8]
l1=list(map(lambda x:(x*1.8)+32,Celsius))
print(l1)

#Q.2- Apply an anonymous function to square all the elements of a list using map and lambda.
lst1=[i for i in range(1,10)]
lst2=list(map(lambda x:x**2,lst1))
print(lst2)

'''  Filter & Reduce  '''
#Q.1- Filter out all the primes from a list.
lst=[i for i in range(2,20)]
flag=0
def isprime(number):
    flag=0
    j=2
    while (j<number and flag==0):
        if (number%j!=0):
            flag=0
        else:
            flag=1
        j+=1
    if(flag==1):
        return False
    else:
        return True
primes=list(filter(isprime,lst))
print(primes)

#Q.2- Write a python program to multiply all the elements of a list using reduce.
from functools import *
l1=[i for i in range(1,6)]
r=reduce(lambda x,y:x*y,l1)
print(r)
