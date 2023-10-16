def merge_sort(arr):

    #возвращаем массив если длина меньше или равна 1, так как он уже отсортирован
    if len(arr) <=1:
        return arr
    
    # находим середину массива
    mid= len(arr) // 2

    #определяем левую и правую части массива
    left_half = arr[mid:]
    right_half = arr[:mid]

    #рекурсивно сортируем обе половины
    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = 0 # переменная k служит индексом для записи элементов в исходный массив arr в правильном порядке в процессе слияния.

     # Копируем данные из временных массивов обратно в основной массив
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    # Проверяем, остались ли элементы в обеих половинах и копируем их
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Пример использования
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Отсортированный массив:", arr)



