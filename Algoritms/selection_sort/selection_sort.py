

def selection_sort(lst: list, direction=lambda x,y: x>y):

    if not isinstance(lst, list):
        raise ValueError(' не является массивом')
    for i in range(len(lst)):
        index_min_element = i
        for j in range(i+1, len(lst)):
            if direction(lst[index_min_element], lst[j]):
                index_min_element = j
        lst[i], lst[index_min_element] = lst[index_min_element], lst[i]
    return lst

lst_1 = [0,5,3,4,20,0]
print(selection_sort(lst_1))
