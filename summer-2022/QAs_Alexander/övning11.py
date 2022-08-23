# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 10:48:03 2022

@author: alexa
"""


#Skapa en matris - använd lista av listor
M = [[1,2,3],
     [4,5,6],]

print(M)
print(M[0])
print(M[1])

#Antalet rader är antalet element i M
print(len(M))

#Antalet kolumner är antalet element i en av M:s listor
print(len(M[0]))

#Iterera över alla element i listan radvis:

print("ITERATION RADVIS:")
#Först alla rader
for i in range(len(M)):
    #Sedan alla kolumner
    for j in range(len(M[0])):
        print(M[i][j])
        
        

#Iterera över alla element i listan kolumnvis:

print("ITERATION KOLUMNVIS:")
#Först alla kolumner
for j in range(len(M[0])):
    #Sedan alla rader
    for i in range(len(M)):
        print(M[i][j])
        
        
def printMatrix(M):
    rows = len(M)
    cols = len(M[0])
    
    for i in range(rows):
        s = ""
        for j in range(cols):
            s = s + str(M[i][j]).ljust(3)
        print(s)
        

def add(A,B):
    #Ta fram rader och kolumner (spelar ingen roll ifrån vilken)
    rows = len(A)
    cols = len(A[0])
    
    #Skapa ny matris
    newM = []
    
    for i in range(rows):
        newM.append([])
        for j in range(cols):
            newM[i].append(A[i][j]+B[i][j])
            
    return newM

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[1,2,3],
     [4,5,6],
     [7,8,9]]
print(add(A,B))
    

def identity(n):
    newM = []
    
    #Iterera över rader
    for i in range(n):
        #Iterera över kolumner
        newM.append([])
        for j in range(n):
            if i == j:
                newM[i].append(1)
            else:
                newM[i].append(0)
    return newM

print(identity(5))


        
printMatrix(identity(5))