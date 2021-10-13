def strMix(str_1, str_2):
    new_str = ""
    for i in range(min(len(str_1), len(str_2))):
        new_str += str_1[i] + str_2[i]
    if len(str_1) == len(str_2):
        return new_str
    if len(str_1) > len(str_2):
        new_str += str_1[i+1:]
    else:
        new_str += str_2[i+1:]
    return new_str

def findPalindrome(arr):
    res = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if i == j:
                continue
            else:
                temp_str = strMix(arr[i], arr[j])
                if temp_str == temp_str[::-1]:
                    res.append([arr[i], arr[j]])
    return res


print(findPalindrome(["hello", "hi", "acb", "yellow", "bca", "ih", "rccr", "moon", "aea"]))
# print(strMix("rccr", "aea"))