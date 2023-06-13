def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapify(array, i, heap_size):
    l = left(i)
    r = right(i)

    if l <= heap_size and array[l] > array[i]:
        largest = l
    else:
        largest = i

    if r <= heap_size and array[r] > array[largest]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        max_heapify(array, largest, heap_size)

    return array


def build_max_heap(array):
    heap_size = len(array) - 1

    for i in range(len(array) // 2 - 1, -1, -1):
        max_heapify(array, i, heap_size)

    return array


def heapsort(array):
    heap_size = len(array) - 1
    build_max_heap(array)

    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heap_size -= 1
        max_heapify(array, 0, heap_size)

    return array
