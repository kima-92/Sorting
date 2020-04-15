"""
Merge Sort   ( Divide & Conquer )

# Devide each item in the array into separate lists ( each item in it's own array )
# Pick two arrays to compare the first item in each list
# Which ever is lowest, add it to a new list
# Repeat:
    # Compare the two items at the front of each list
    # Add the smallest to the new list
# Repeat till the original two lists are empty

# Now grab two more list and repeat that process
# Keep repeating till you have only one list
"""






# Helper function to merge 2 sorted arrays
def merge(left_l, right_l):
    # Set index value for the list to the left, and the list to the right
    i = 0   # Current index in left_l
    j = 0   # Current index in right_l

    # set a new list
    list_length = len(left_l) + len(right_l)
    merged_l = [0] * list_length
    # Set index for the merged_l, to insert the new values
    x = 0

    # Compare left_l[i] with righ_l[j]

    # While i is less than the length of left_l AND j is less than the length of right_l
    while i < len(left_l) and j < len(right_l):
        # if left_l[0] is smaller than right_l[0]
        if left_l[i] < right_l[j]:
            # Set merged_l[0] as left_l[0]
            merged_l[x] = left_l[i]

            # Increment index of both left_l and merged_l
            i += 1      # So we ignore the previous index from now on
            x += 1      # So we can add items to next index

        # else
        else:
            # Set arr[0] as right_l[0]
            merged_l[x] = right_l[j]

            # Increment index of both right_l and merged_l
            j += 1      # So we ignore the previous index from now on
            x += 1      # So we can add items to next index

    # Make sure we add whatever items are left in each array
    while i < len(left_l):
        merged_l[x] = left_l[i]
        
        i += 1
        x += 1

    while j < len(right_l):
        merged_l[x] = right_l[j]
        
        j += 1
        x += 1

    return merged_l
        
        
    """
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    print(f"elements: {elements}")
    print(f"merge_arr: {merged_arr}")

    # Get the length of each array
    list_length = len(arrA) + len(arrB)
    print(f"list_length: {elements}")
    # Set new_array
    new_array = []
    # For i in len(list_length):
    for x in range(0, list_length):
        # Compare item in arrA[0] with arrB[0]
        print(f"x: {x}")
        for i in arrA:
            print(f"i: {i}")
            for j in arrB:
                print(f"j: {j}")
                # If arrA[0] is smaller than arrB[0]
                if i < j:
                    print(f"compared i: {i} and j: {j}")
                    # append arrA[0] to new_array
                    new_array.append(i)
                    print(f"Appended i")

                    arrA.remove(i)
                    print(f"removed {i} from arrA")
                # Else
                else:
                    # Append arrB[0] to new_array
                    new_array.append(j)
                    print("appanded j")
                    arrB.remove(j)
                    print(f"removed {j} from arrB")
                    """
    
    #return new_array


# Implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # Devide the list into individial lists ( A list of lists? )

    sorted_list = []
    
    # Base case
    if len(arr) > 1: 

        # Grab the middle index of that list
        mid = int(len(arr) / 2)
        # Separate arr into two lists 
        left_l = arr[:mid]
        right_l = arr[mid:]
        print("Divided a list")
        # For every two lists, use the merge function
        merge_sort(left_l)  # By the time this gets done, it will be a sorted list
        merge_sort(right_l) # By the time this gets done, it will be a sorted list

        # Merge the separated lists
        sorted_list = merge(left_l, right_l)
        print(f"Merged a list: {sorted_list}")


    return sorted_list

# Testing merge_sort

a = [55, 23, 98, 36, 75, 16, 9, 44, 22]

print(f"\nOriginal array:\n\t{a}")

sorted_array = merge_sort(a)

print(f"\nSorted array:\n\t{a}")



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
