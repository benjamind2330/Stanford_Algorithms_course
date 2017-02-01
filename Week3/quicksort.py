from random import randint, seed, randrange


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
def quicksortImpl(arr, start, end):

    if (len(arr) <= 1 or end - start <= 1):
        return

    partition_element = randint(start, end - 1)
    (pivot_start, pivot_end) = partition(arr, start, end, partition_element)

    quicksortImpl(arr, start, pivot_start)
    quicksortImpl(arr, pivot_end + 1, end)


def quicksort(arr):
    quicksortImpl(arr, 0, len(arr))


seed()
some_arr = [randint(1, 20) for e in range(1, 40)]
print(some_arr)
# partition(some_arr, 0, len(some_arr), 0)
quicksort(some_arr)
print(some_arr)
