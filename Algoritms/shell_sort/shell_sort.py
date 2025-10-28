
import random

def shell_sort(lst: list, direction=lambda x,y: x<y):

    if not isinstance(lst, list):
        raise ValueError(' не является массивом')
    n = len(lst)
    interval = n//2
    while interval>0:
        for i in range(interval, n):
            iterator = lst[i]
            j = i
            while direction(iterator, lst[j-interval]) and j>=interval:
                lst[j-interval], lst[j] = lst[j], lst[j-interval]
                j-=interval
        interval //=2
    return lst

app = [random.randint(-2000,1400) for m in range(1,10)]
print(app)
print("отсортированный   ")
print(shell_sort(app))