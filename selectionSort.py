import sys
import random
A = ["Q♠", "A♦", "4♣"] 


for i in range(len(A)):
    A[i].replace("A","1")
    A[i].replace("Q","12")
    A[i].replace("K","13")
    A[i].replace("♠","1")
    A[i].replace("♦","2")
    A[i].replace("♣","3")
    A[i].replace("♥","4")
    print(A[i])
    


  
# Traverse through all array elements 
for i in range(len(A)):
    
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 
  
# Driver code to test above 
print ("Sorted array")
print(A)

