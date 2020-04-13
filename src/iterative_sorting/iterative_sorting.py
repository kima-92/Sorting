# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


def bubble_sort( arr ):

    # Set didSwap to True
    did_swap = True

    # While didSwap == True
    while did_swap == True:
        # grab arr[0]
        for i in range(0, len(arr)):
            print(f"Grabed index {i} in outer loop")
            
            # grab arr[1]
            for j in range(i+1, len(arr)):
                print(f"Grabed index {j} in inner loop")

                # If arr[1] > arr[0]
                if arr[j] < arr[i]:
                    # Swap them
                    arr[j], arr[i] = arr[i], arr[j]
                    # Set didSwap to True
                    did_swap = True
                    print(f"Swapped {arr[i]} with {arr[j]} and set did_swap to True")
                
                # Else:
                else:
                    # Don't swap them 
                    # Set didSwap to False
                    did_swap = False
                    print(f"Did not swap {arr[i]} with {arr[j]}, set did_swap to False")

    return arr

a = [9, 1, 8, 4, 3, 5, 6, 10, 7, 2]

print(f"\nOLD list: {a}")
new_list = bubble_sort(a)
print(f"NEW list: {new_list}")

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr