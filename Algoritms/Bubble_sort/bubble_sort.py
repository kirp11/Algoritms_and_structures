
# increase - возрастание
# decrease - убывание
def bubble_sort(lst: list, direction=lambda x,y: x>y):
    if not isinstance(lst, list):
        raise ValueError(' не является массивом')

    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if direction(lst[j], lst[j+1]):
                lst[j], lst[j + 1] = lst[j+1], lst[j]
    return lst