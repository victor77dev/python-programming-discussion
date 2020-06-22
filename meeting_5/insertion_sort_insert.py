def insertion_sort_insert(list):
    # This is a fake insertion sort as time complexity is higher than O(n^2) due to insert operator
    # https://wiki.python.org/moin/TimeComplexity
    for i in range(len(list)):
        j = i
        ele = list.pop(i) # This is O(i)
        while j > 0:
            if (list[j - 1] <= ele):
                list.insert(j, ele) # This is O(n)
                break
            else:
                j -= 1
                continue

        if j == 0:
            list.insert(0, ele)

list = [21, 5, 22, 20, 12, 3, 11, 5, 13, 16]
print(len(list), insertion_sort_insert(list))
print(list)

list = [1, 2, 30, 4, 5, 6, 12, 20, 25, 30]
print(len(list), insertion_sort_insert(list))
print(list)

list.reverse()
print(len(list), insertion_sort_insert(list))
print(list)
