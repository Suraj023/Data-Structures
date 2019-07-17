""" insertion sort checking time complexity also"""
import time
def Insertion(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
          a[j+1]=a[j]
          j-=1
        a[j+1]=key
        
start = time. time()      #when program start
a=[]        
n=int(input("Number of elements: "))
print("Enter the elements\n")
for i in range(1,n+1):
    i=input()
    a.append(i)
Insertion(a) 
print("Sorted elements are \n")
for i in range(len(a)): 
    print (a[i])         
end = time. time()    # program end
print("Time Complexity(in ms): ",end - start)    #time diiference 

#algorithm From Cormen
"""for i=2 to a.length()
  key =a[i]
  j=i-1
  while j>0 and a[j]>key
      a[j+1]=a[j]
      j=j-1
  a[i+1]=key """   


"""Time Complexity: O(n*2) and Auxiliary Space: O(1)"""
