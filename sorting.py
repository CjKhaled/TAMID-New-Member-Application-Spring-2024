def sort_arrays(arr1: list, arr2: list, k):
    # First, we add the two arrays together (basically just appending the second one to the first)
    # Then we use the sorted function which is o(n log n) complexity
    # Finally we only take the amount of numbers from the argument k by indexing
    return sorted(arr1 + arr2)[0:k]

array_one = [1,3,5,8]
array_two = [1,2,3]
amount = 5

result = sort_arrays(array_one, array_two, amount)
print(result)
