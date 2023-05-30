import time
import numpy

import heapsort
import quicksort
import insertionsort

array = numpy.random.randint(100_000, 500_000, 10_000)
heapsort_array = array.copy()
quicksort_array = array.copy()
insertionsort_array = array.copy()


start_time = time.perf_counter()
heapsort.heapsort(heapsort_array)
end_time = time.perf_counter()
print('heapsort: ', heapsort_array)
print(f'Czas wykonywania heapsort: {end_time - start_time} sekund')


start_time = time.perf_counter()
quicksort.quicksort(quicksort_array, 0, len(quicksort_array) - 1)
end_time = time.perf_counter()
print('quicksort: ', quicksort_array)
print(f'Czas wykonywania quicksort: {end_time - start_time} sekund')


start_time = time.perf_counter()
insertionsort.insertionsort(insertionsort_array, len(insertionsort_array))
end_time = time.perf_counter()
print('insertionsort: ', insertionsort_array)
print(f'Czas wykonywania insertionsort: {end_time - start_time} sekund')