

def inversion(lst: list):
    if not isinstance(lst, list):
        raise ValueError(' не является массивом')
    for i in range(len(lst)//2):
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
    return lst


a = [1,2,3,4,5,6,7,8,9]

print(inversion(a))
