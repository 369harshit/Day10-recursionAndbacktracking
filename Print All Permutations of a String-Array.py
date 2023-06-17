def print_permutations(arr):
    n = len(arr)

    # Initialize an array to keep track of the current indices
    indices = [0] * n

    # Print the initial permutation
    print(arr)

    i = 0
    while i < n:
        if indices[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[indices[i]], arr[i] = arr[i], arr[indices[i]]
            
            # Print the current permutation
            print(arr)

            # Reset the indices for the swapped elements
            indices[i] += 1
            i = 0
        else:
            indices[i] = 0
            i += 1

# Test the print_permutations function
input_arr = [1, 2, 3]
print("[")
print_permutations(input_arr)
print("]")
