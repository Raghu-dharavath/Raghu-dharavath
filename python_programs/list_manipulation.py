def modify_list(lst):
    result = []
    for i in range(len(lst)):
        if lst[i]!=lst[-1]:
            res = lst[i]*(i-1) + lst[i] + 1
            result.append(res)
        else:
            res = lst[i]*(lst[i]-1) + lst[0]
            result.append(res)
    return result
my_list = [2,5,6,7]
result = modify_list(my_list)
print(result)