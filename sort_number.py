arreglo2 = [23, 6, 2, 45]


def sort_numbers(array: list) -> bool:
    sorted2: bool = False
    while not sorted2:
        sorted2 = True
        for i in range(0, len(array) - 1):
            x = array[i + 1]
            if array[i] > array[i + 1]:
                sorted2 = False
                array[i + 1] = array[i]
                array[i] = x
    return array
a = [5,8,1,10,6,7,8,9,0,6,0,3]
print(sort_numbers(a))

