# given array A,  intergers N
# 1. Dominator = occurrence > half length of A
# 
# required: returns: -1 if no dominator, and the indices of the dominator if available

# basic edge cases (possibilities)
''' 
1. empty array [] - return -1
2. len(arr) = 1 eg [2] - return the index - 0
3. len(arr) = 2 eg [2, 3] - return ?? but if [3,3] return 0,1
4. general case eg [2,3,5,3,3] - return indices of 3

Assume no possibility of two different numbers dominating?? eg [3,3,3,5,5,5]
'''

# brute force sln:
"""
use nested loops
1. store occurence of each value n - loop through array, using each int
"""

def dominator(arr=[]):
    
    # edge cases 1 - empty array
    if len(arr) ==0:
        return -1
    
    #while position p<=length
    pos=0
    # required value for a dominator = len.arr/2
    while pos<=len(arr)-1:
        domValue = 0
        # create arr of indices
        domIndices = []
        # remove all elements that do not equal to the element, and return the size of the arr
        # use i - should actually loop
        i=0
        while i<=len(arr)-1:
            if arr[i]==arr[pos]:
                # add index - coming back here:
                domIndices.append(i)
                domValue +=1
            i+=1
        # check if the value > half the length
        if domValue > len(arr)/2:
            return domIndices
        else:
            pos +=1
    # if no domValue above len/2
    return -1
       
print(dominator([3,5,5,6,5,5])) #shoulr return [1,2,4,5] 
    