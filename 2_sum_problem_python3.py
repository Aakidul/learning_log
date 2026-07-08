def sum_dsa(target, array):

    len_of_list = len(array)
    for i in range(len_of_list):
        for x in range(i + 1, len_of_list):
            if x == len_of_list:
                break

            if array[i] + array[x] == target:
               return [i, x]

a = sum_dsa(12, [1, 3, 9, 10, 11, 5])
print(a)
