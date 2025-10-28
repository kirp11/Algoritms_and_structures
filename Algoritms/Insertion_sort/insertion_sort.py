


def insertion_sort(lst: list, direction=lambda x,y: x<y):

    if not isinstance(lst, list):
        raise ValueError(' не является массивом')
    for i in range(1, len(lst)):
        iterator = lst[i]
        j = i - 1
        while direction(iterator, lst[j]) and j>=0:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            j-=1
    return lst

app = [0,1,3,2,5]
print(insertion_sort(app))