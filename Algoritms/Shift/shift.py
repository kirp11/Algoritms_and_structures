

def shift(lst: list, direction,val):
    if not isinstance(lst, list):
        raise ValueError(' не является массивом')

    def shift_one_right(lst: list):
        i = len(lst)-1
        iter = lst[i]
        while i>0:
            lst[i] = lst[i-1]
            i -=1
        lst[0] = iter
        return lst

    def shift_one_left(lst: list):
        i = 0
        iter = lst[i]
        while i<len(lst)-1:
            lst[i] = lst[i+1]
            i +=1
        lst[len(lst)-1] = iter
        return lst

    for j in range(val):
        if direction == "right":
            shift_one_right(lst)
        else:
            shift_one_left(lst)
    return lst


a = [1,2,3,4,5,6,7,8,9]

print(shift(a, "left", 2))