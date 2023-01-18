num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 1
for i in range(1, 11):
    for j in num:
        if i == j:
            count *= 1
    print(count, 'x', i, '=', count*i)
    
num = 3
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
    
        
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 1
for i in range(1, 11):
    for j in num:
        if i == j:
            count *= 1
    print(count, 'x', i, '=', count*i)
    
    num = 3
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
    
alphabet = 'a, b, c, d, e, f, g, h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
consonants = 'bcdfghjklmnpqrstvwxyz'
print(sum(consonant in consonants for consonant in alphabet))

alphabet = 'a, b, c, d, e, f, g, h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
consonants = 'bcdfghjklmnpqrstvwxyz'
count = 0
for i in alphabet:
    for j in consonants:
        if i == j:
            count += 1
print(count)

alphabet = 'a, b, c, d, e, f, g, h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
consonants = 'bcdfghjklmnpqrstvwxyz'
print(sum(consonant in consonants for consonant in alphabet))

for i in range(1, 11):
    for j in range(1, 11):
        print(i, 'x', j, '=', i*j)
    print()
    
    alphabet = 'a, b, c, d, e, f, g, h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
consonants = 'bcdfghjklmnpqrstvwxyz'
count = 0
for i in alphabet:
    for j in consonants:
        if i == j:
            count += 1
print(count)

num = 3
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
    
num = 3
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
    
num = (int(input()) + int(input()) + int(input()))
if num == 180:
    print("The triangle is valid")
else:
    print(" The triangle is not valid")

A = int(input())
B = int(input())
H = int(input())
if A >= 5 or B <= 10 and H <= 8:
    print("Normal")
if A >= 5 and B <= 10 and H >= 10:
    print("Excess")
if A >= 5 and B <= 10 and H < 5:
    print("Deficiency")

A = int(input())
B = int(input())
H = int(input())
if A >= 5 and B <= 10 and H == 8:
    print("Normal")
if A >= 5 and B <= 10 and H >= 10:
    print("Excess")
if A > 5 and B <= 9 and H < 3:
    print("Deficiency")

import math
x = int(input())
print(math.expm1(x) - 1)

import math
x = int(input())
y = int(input())
print(math.copysign(x,y))

import random
n = int(input())
random.seed(n)
print(random.randint(-100, 100))

def multiply(strng):
    result = 1
    if 'x' in strng:
        mylist = strng.split('x')
        print(mylist)
        for i in range(len(mylist)):
            result = result * int(mylist[i])
            #result *= int(mylist[i])
    return result

mycalc = multiply('1x2x3x4x5x6x7')
print(mycalc)