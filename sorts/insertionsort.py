def insertionsort(array, r):
    for i in range(1, r):
        x = array[i]
        j = i - 1

        while j >= 0 and x < array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = x

    return array
