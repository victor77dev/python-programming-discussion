def insertion_sort(list):
    count = 0
    for i in range(len(list)):
        j = i
        while j > 0:
            count += 1
            if list[j] >= list[j - 1]:
                break
            else:
                # swap j, j - 1
                temp = list[j - 1]
                list[j - 1] = list[j]
                list[j] = temp

            j -= 1
    return count


list = [21, 5, 22, 20, 12, 3, 11, 5, 13, 16]
list2 = [1, 2, 30, 4, 5, 6, 12, 20, 25, 30]
print(len(list), insertion_sort(list))
print(len(list2), insertion_sort(list2))
print(list)
print(list2)

list.reverse()
print(len(list2), insertion_sort(list2))
print(list2)