# in an array, dominator appears n times where n>len/2

# steps:
# Sort - O(NlogO)


def dominator(arr=[]):
    # sort, and return sorted array
    arr2 = sorted(arr)
    
    # check from el 0 to half the arr
    pos=0
    while pos<len(arr)/2:
        # check if el at position pos is equal to at position pos+half+1
        end = pos+(len(arr)//2)
        if arr2[pos]==arr2[end]:
            # resort to the initial array,, check positions of arr2[pos]
            return [x for x, el in enumerate(arr) if el==arr2[pos]]
        else:
            pos+=1
            
    return -1

print(dominator([2,5,5,5,9,5]))