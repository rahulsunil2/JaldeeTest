from itertools import permutations

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
    for i in arr:
        for j in arr:
            if i == j:
                print("Continue", i, j)
                continue
            else:
                print("Nope", i, j)
                temp_str = strMix(i, j)
                if temp_str == temp_str[::-1]:
                    res.append([i, j])
    return res


print(findPalindrome(["hello", "hi", "acb", "yellow", "bca", "ih", "rccr", "moon", "aea"]))
# print(strMix("rccr", "aea"))