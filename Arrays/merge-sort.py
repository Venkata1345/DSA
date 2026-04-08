def merge_sort(arr):
    if len(arr)<=1:
        return arr 
    
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    mergeed_arr=[]
    i,j = 0,0

    while i< len(left) and j<len(right):
        if left[i] <= right[j]:
            mergeed_arr.append(left[i])
            i+=1
        else:
            mergeed_arr.append(right[j])
            j+=1 
    
    while i< len(left):
        mergeed_arr.append(left[i])
        i+=1

    while j < len(right):
        mergeed_arr.append(right[j])
        j+=1
    return mergeed_arr

sorted_list = merge_sort([7,4,1,5,3])
print(sorted_list)
