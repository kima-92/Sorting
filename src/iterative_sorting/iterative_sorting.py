# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    #for i in range(0, len(arr) - 1):
        #cur_index = i
        #smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        # grab arr[0]
        for i in range(0, len(arr)):
            print(f"grabbed index {i} from outer loop")
            # set current index as arr[0]
            current_index = i
            # set lowest number
            smallest_index = current_index

            # grab last index
            
            # grab arr[1]
            #j = i + 1  # item to the right of i

            for j in range(i+1, len(arr)):
                print(f"grabed index {j} from inner loop")
                
                # if arr[0] is grater than arr[1]
                if arr[j] < arr[smallest_index]:
                    # set lowerst number to item in arr[1]
                    smallest_index = j
                    print(f"Set smallest_index to: {j}")

            if current_index != smallest_index:
                # Swap
                #arr[current_index] = arr[smallest_index]
                #arr[smallest_index] = arr[current_index]
                arr[current_index], arr[smallest_index] = arr[smallest_index], arr[current_index]
                print(f"Swapped item in index {current_index} with index {smallest_index}")
            
        return arr

print("\n\tSelection Sort\n")
a = [9, 1, 8, 4, 3, 5, 6, 10, 7, 2]
print(f"\nOLD list: {a}")
new_list1 = selection_sort(a)
print(f"\nNew list: {a}")



def bubble_sort( arr ):

    # Set didSwap to True
    did_swap = True
    
    # While didSwap == True
    while did_swap == True:
        # grab arr[0]
        for i in range(0, len(arr)):
            print(f"Grabed index {i} in outer loop")

            #current_num = arr[i]
            
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
"""
print("\n\tBubble Sort\n")

b = [9, 1, 8, 4, 3, 5, 6, 10, 7, 2]

print(f"\nOLD list: {b}")
new_list2 = bubble_sort(b)
print(f"NEW list: {new_list2}")

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
    """