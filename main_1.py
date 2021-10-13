def consecutiveSum(arr, target):
    res = []
    for i in range(len(arr)):
        temp_arr = []
        for j in range(i, len(arr)):
            temp_arr.append(j)
            if sum(temp_arr) > target:
                break
            if sum(temp_arr) == target and len(temp_arr) > 1:
                res.append(temp_arr)
                break
    return res

print(consecutiveSum([1,2,3,4,5,6,7,8,9,10], 9))