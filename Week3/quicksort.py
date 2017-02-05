from random import randint, seed, randrange
from enum import Enum
from statistics import median

class part_style(Enum):
    RANDOM = 0
    FIRST = 1
    LAST = 2
    MED_OF_THREE = 3


def swap(arr, i, j):
    if (i == j):
        return
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def partition(arr, start, end, partition_element):
    # Check for base case
    if end < start or end - start < 2:
        return arr

    # Get a random position to partition around.
    swap(arr, start, partition_element)

    # set up the pre and post variables

    small = start + 1
    same = start + 1

    for i in range(start + 1, end):
        # variable is the same as the partition

        if arr[i] == arr[start]:
            swap(arr, i, same)
            same += 1
            continue

        # variable is smaller than the partition
        if arr[i] < arr[start]:
            swap(arr, small, same)
            if (same != i):
                swap(arr, small, i)
            small += 1
            same += 1
            continue

        # variable is larger than the partition then do nothing.

    swap(arr, start, small - 1)
    return (small - 1, same - 1)


# start is inclusive, end is not.
def quicksortImpl(arr, start, end, partStyle):

    if (len(arr) <= 1 or end - start <= 1):
        return 0

    if (partStyle == part_style.RANDOM):
        partition_element = randint(start, end - 1)
    if (partStyle == part_style.FIRST):
        partition_element = start
    if (partStyle == part_style.LAST):
        partition_element = end - 1
    if (partStyle == part_style.MED_OF_THREE):
        med = median([arr[start], arr[end - 1], arr[int((end - start) / 2)]])
        if (med == arr[start]):
            partition_element = start
        elif (med == arr[end - 1]):
            partition_element = end - 1
        else:
            partition_element = int((end - start) / 2)
    (pivot_start, pivot_end) = partition(arr, start, end, partition_element)

    a = quicksortImpl(arr, start, pivot_start, partStyle)
    b = quicksortImpl(arr, pivot_end + 1, end, partStyle)
    return end-start-1 + a + b


def quicksort(arr, part_type = part_style.RANDOM):
    return quicksortImpl(arr, 0, len(arr), part_type)


seed()
#some_arr = [randint(1, 20) for e in range(1, 40)]
#print(some_arr)
## partition(some_arr, 0, len(some_arr), 0)
#quicksort(some_arr)
#print(some_arr)



str_in = "QuickSort_Data.txt"
print("reading from " + (str_in))
infile = open(str_in, 'r')
contents = infile.read()
arr = contents.split('\n')
arr = arr[:-1]

arr_int = [int(n) for n in arr]
total_comps = quicksort(arr_int, part_style.FIRST)
print("Total comps FIRST " + str(total_comps))

arr_int = [int(n) for n in arr]
total_comps = quicksort(arr_int, part_style.LAST)
print("Total comps LAST " + str(total_comps))

arr_int = [int(n) for n in arr]
total_comps = quicksort(arr_int, part_style.MED_OF_THREE)
print("Total comps MED OF THREE " + str(total_comps))

outfile = open("sorted.txt", 'w')
for i in arr_int:
    outfile.write(str(i) + '\n')

for i in range(1, len(arr_int)):
    if (arr_int[i] < arr_int[i - 1]):
        print("Bad order! ")
