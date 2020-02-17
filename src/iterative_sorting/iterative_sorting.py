# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        small_num = arr[i]
        current_index = i
        for j in range(i+1,len(arr)):
            if (small_num > arr[j]):
                small_num = arr[j]
                current_index = j
        arr[current_index] = arr[i]
        arr[i] = small_num
        print(arr)    



        # TO-DO: swap




    return arr

my_list = [3,6,8,1,9,2,4,7,5]
print(selection_sort(my_list))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr