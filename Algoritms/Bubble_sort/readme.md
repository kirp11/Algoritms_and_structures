### Сортировка "пузырьком"

#### Алгоритм на естественном языке
Сравниваются текущий и последующий элементы (пары соседних), и если 
они в неправильном порядке, согласно признаку сортировки, они меняются 
местами. Этот процесс повторяется, пока массив не будет отсортирован.

###### функция принимает в себя:
 - список, который необходимо отсортировать
 - ключ сортировки
 - направление сортировки

```bash
def bubble_sort(lst, key, direction)

 ```