def insSort(lst): 
    for i in range(1, len(lst)): 
        key = lst[i] 
        # move elements of the right sublist greater than the key
        # one position to the right
        j = i-1
        while j >= 0 and key < lst[j] : 
                lst[j+1] = lst[j] 
                j -= 1
        lst[j+1] = key 