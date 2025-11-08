
import random

def merge_sort(lst: list):

    if not isinstance(lst, list):
        raise ValueError(' не является массивом')
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right, direction=lambda x,y: x<y):
    sorted_list = []
    i = j = 0
    while direction(i, len(left)) and direction(j, len(right)):
        if direction(left[i], right[j]):
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

app = [random.randint(-2000,1400) for m in range(1,10)]
print(app)
print("отсортированный   ")
print(merge_sort(app))