
import random
#direction=lambda x,y: x<y

def hoara_sort(lst, start, end):

    if not isinstance(lst, list):
        raise ValueError(' не является массивом')
    # выбор пивота - опорного элемента, относительно которого сравниваем массив
    if start >= end:
        return lst
    i = start
    j = end

    pivot = lst[((end + start)//2)]

    while i <= j:

        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1

    if start < j:
        hoara_sort(lst, start, j)
    if i < end:
        hoara_sort(lst, i, end)

    return lst

app = [random.randint(-200,140) for m in range(1,25)]
print(app)
print("отсортированный   ")
print(hoara_sort(app,0,len(app)-1))