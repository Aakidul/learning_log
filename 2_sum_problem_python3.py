def sum_dsa(target, array):

    len_of_list = len(array)
    for i in range(len_of_list):
        for x in range(i + 1, len_of_list):
            if x == len_of_list:
                break

            if array[i] + array[x] == target:
               return [i, x]

"""
a = sum_dsa(12, [1, 3, 9, 10, 11, 5])
print(a)
"""
***things to remember are***

   selection we use combination and order doesn't matter 
   so, it will always match the target if there are 2 indices which
   equals to the target. and for onlt one valid answer as per rule we dont 
   need orders to check, just need one valid answer and it already exists in
   linear list.

   and if problem is about order then we use permutations.
"""
"""


"""2026"""
