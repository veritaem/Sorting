# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for sec_index in range(cur_index, len(arr)):
            if arr[sec_index] < arr[cur_index]:
                mem_var = arr[sec_index]
                arr[sec_index]= arr[cur_index]
                arr[cur_index] = mem_var
        # TO-DO: swap
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swaps = True
    while swaps == True:
        count_swaps = 0
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                hold = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = hold
                count_swaps += 1
        if count_swaps == 0:
            swaps = False
    


    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    # make sure array isnt sorted by fiat
    if len(arr) > 0:
        #make sure no negatives
        for i in arr:
            if i < 0:
                return 'Error, negative numbers not allowed in Count Sort'
        # store appearances of elements in dictionary
        store = {}
        for i in arr:
            if i in store:
                store[i] += 1
            else:
                store[i] = 1

        # create list length of data
        l = [0] * (max(arr)+1)

        # initially fill list with appearances of each element
        for k in store:
            l[k] = store[k]

        # summing appearances for each number
        sum = 0
        for i in range(0, len(l)):
            sum += l[i]
            l[i] = sum
        arr = [None]*len(l)

        # iterate over store and use value in summed list to output final positions
        for k in store:
            while store[k] != 0:
                arr[l[k]-1] = k
                print(store[k])
                store[k] -= 1
                print(arr)
        arr = [a for a in arr if not a == None]
    return arr

print(count_sort([0, 5, 6, 13, 14, 9, 0, 2, 3, 3]))