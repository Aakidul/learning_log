def sorting_algo(array):
    sorted_array = []
    for x in range(len(array)):
        for y in range(len(array) + 1):
            if y == len(array):
                    break
            if array[x] > array[y]:
                array[x], array[y] = array[y], array[x]
                sorted_array.append(array[x])
                sorted_array.append(array[y])
    print(sorted_array)


# sorting_algo([5, 8, 19, 3, 67])
