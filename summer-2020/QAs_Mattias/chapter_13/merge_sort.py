def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # Identify the "middle" of the list
        L = arr[:mid]       # Dividing the array elements into two parts
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Copy data from L and R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        # i and j have not necessarily reached the last index of L and R
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            

arr = [12, 11, 13, 5, 6, 7]
print("Given array is", end="\n")
print(arr)
merge_sort(arr)
print("Sorted array is: ", end="\n")
print(arr)
