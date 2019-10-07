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
    # store how many times each number appears
    store = {}
    for i in arr:
        if i in store:
            store[i] += 1
        else:
            store[i] = 1
    
    # make a list the length of my max value ie from 0 to max(arr)
    l = [0] * (max(arr)+1)

    
    # insert values of the dict into the list
    for k in store:
        l[k] = store[k]

    # sum previous elements of list to current value of list
    cum_sum = 0
    for i in range(0, len(l)):
        cum_sum += l[i]
        l[i] = cum_sum


    # use store dict and summed list to output positions into new list
    arr = [None]*len(l)
    for k in store:

        arr[l[k]-1] = k


    return arr