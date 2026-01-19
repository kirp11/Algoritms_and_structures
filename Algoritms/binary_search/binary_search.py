

def binary_search(lst: list, val):
    if not isinstance(lst, list):
        raise ValueError(' не является массивом')
    if val not in lst:
        return -1

    middle = len(lst)//2
    if val == lst[middle]:
        return middle
    elif val < lst[middle]:
        result = binary_search(lst[:middle], val)
        return result
    elif val > lst[middle]:
        result = binary_search(lst[middle:], val)
        return middle + result
    print(middle)


a = [1,2,3,4,5,6,7,8,9]

print(binary_search(a, 7))