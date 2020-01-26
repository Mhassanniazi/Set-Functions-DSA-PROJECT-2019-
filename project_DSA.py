#!/usr/bin/env python
# coding: utf-8

# In[9]:


########## FUNCTION 01 ###########
def union(array1,array2):
    emptylist=[]
    for i in array1:
        if i not in emptylist:
            emptylist.append(i)
    for j in array2:
        if j not in emptylist:
            emptylist.append(j)
    emptylist.sort()
    print(emptylist)
#union([6,7,8,9,9,9],[9,1,2,5])
arr1=[34,45,73,38,39,62,64,69,56,51,59,63,52,71,68,70,58,41,37,48,40,72,44,60,47,46,54,43,35,49,55,67,65,75,74,36,61,66,57,53,42,50]
arr2= [52,6,103,44,70,67,92,77,56,69,101,57,105,49,66,60,40,58,104,80,75,95,71,89,86,73,84,97,88,9,93,48,63,74,79,45,41,98,81,87,76,55,85,43,64,96,72,59,83,107,46,61,50,54,102,82,78,68,51,53,42,91,47,106,99,100,65,94]
union(arr1,arr2)


# In[1]:


########## FUNCTION 02 ############
def sett(array):
    newarray=[]
    for i in array:
        if i not in newarray:
            newarray.append(i)
    newarray.sort()
    return newarray
########## FUNCTION 03 ###########
def intersection(array1,array2):
    a=len(array1)
    b=len(array2)
    newlist=[]
    if a<b:
        array1,array2=array2,array1
    for i in array1:
        if i in array2:
            newlist.append(i)
    return newlist
#print(intersection([6,7,8,9,9,9],[9,1,2,5]))

#lst1 = [3, 8, 6, 20, 7] 
#lst2=[7, 1, 5, 2, 3, 6]
#lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
#lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(sett(lst1),sett(lst2)))


# In[2]:


####### FUNCTION 04 #############
def difference(A,B):
    difference = []
    for i in A:
        if i not in B:
            difference.append(i)
    return difference
setA = [10, 20, 30, 40, 80]
setB = [100, 30, 80, 40, 60]
#print(difference(setA,setB))
print(difference(setB,setA))


# In[3]:


########### FUNCTION 05 ############
def disjointsets(A,B):
    disjoint = [value for value in A if value in B] 
    if disjoint==[]:
        return True 
    else:
        return False
A=[1,2,3,4,5,6]
B=[6,7,8,9,10]
print(disjointsets(A,B))


# In[4]:


############# FUNCTION 06 #############
def symmetricDifference(A, B,a,b): 
    i = 0
    j = 0
    while (i < a and j < b): 
        if (A[i] < B[j]): 
            print(A[i], end = " ") 
            i=i+1
          
        elif (B[j] < A[i]): 
            print(B[j], end = " ") 
            j=j+1
        else:          
            i=i+1
            j=j+1

# Driver code 
A = [1,2,4,5,6] 
B = [2,3,4,5,7,8] 
a = len(A) 
b = len(B) 
print("SYMMETRIC DIFFERENCE:-")

symmetricDifference(A,B,a,b) 

