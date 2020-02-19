# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    #elements = len( arrA ) + len( arrB )
    #merged_arr = [0]*elements
    merged_arr = []
    while (len(arrA) > 0) & (len(arrB) > 0):
        if (arrA[0]<arrB[0]):
            merged_arr.append(arrA[0])
            arrA.pop(0)
        else:
            merged_arr.append(arrB[0])
            arrB.pop(0)
    if (len(arrA) == 0):
        merged_arr.extend(arrB)
         
    else:
        merged_arr.extend(arrA)
        
    

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if(len(arr)<=1):
        return arr
    else:
        arra,arrb = arr[:(len(arr)//2)],arr[(len(arr)//2):]
        return merge(merge_sort(arra),merge_sort(arrb))

     
#print(merge_sort([6,8,12,1,23,9]))
#print(merge([6,8],[3,7]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
