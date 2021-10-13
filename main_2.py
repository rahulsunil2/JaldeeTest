def mergeSorted(arr_1, arr_2):
    arr_1.extend(arr_2)
    return sorted(arr_1)

print(mergeSorted(["cat", "ox", "c3", "156", "02", "goat"], ["rat", "yellow", "5", "c3", "tiger"]))