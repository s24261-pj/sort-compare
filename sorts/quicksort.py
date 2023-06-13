def partition(array, p, r):
    pivot = array[r]
    smaller = p

    for i in range(p, r):
        if array[i] <= pivot:
            array[smaller], array[i] = array[i], array[smaller]
            smaller += 1

    array[smaller], array[r] = array[r], array[smaller]

    return smaller


def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)
