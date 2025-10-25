"""
selection_algorithms.py
Assignment 6: Medians and Order Statistics
"""

import random
import time
import statistics

# Randomized Quickselect

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def randomized_select(arr, low, high, k):
    """
    Returns the k-th smallest element (0-indexed)
    Expected time complexity: O(n)
    """
    if low == high:
        return arr[low]
    pivot_index = randomized_partition(arr, low, high)
    rank = pivot_index - low
    if k == rank:
        return arr[pivot_index]
    elif k < rank:
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, high, k - rank - 1)


# Deterministic Median of Medians

def deterministic_select(arr, k):
    """
    Deterministic selection using Median of Medians.
    Worst-case O(n) time complexity.
    """
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Step 1: Divide arr into groups of 5 and find medians
    medians = [sorted(arr[i:i + 5])[len(arr[i:i + 5]) // 2]
               for i in range(0, len(arr), 5)]

    # Step 2: Recursively find the median of medians
    pivot = deterministic_select(medians, len(medians) // 2)

    # Step 3: Partition around pivot
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    # Step 4: Recurse in appropriate partition
    if k < len(lows):
        return deterministic_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return deterministic_select(highs, k - len(lows) - len(pivots))


# Empirical Performance Test

def compare_selection_algorithms():
    sizes = [1000, 5000, 10000, 20000]
    print(f"{'n':<8}{'Quickselect(s)':<18}{'Deterministic(s)':<18}")
    for n in sizes:
        data = [random.randint(1, 10**6) for _ in range(n)]
        k = n // 2

        start = time.time()
        randomized_select(data.copy(), 0, n - 1, k)
        quick_t = time.time() - start

        start = time.time()
        deterministic_select(data.copy(), k)
        det_t = time.time() - start

        print(f"{n:<8}{quick_t:<18.6f}{det_t:<18.6f}")


if __name__ == "__main__":
    compare_selection_algorithms()
