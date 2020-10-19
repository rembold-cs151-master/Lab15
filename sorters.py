"""
Library of several different sorting algorithms
"""


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        first = array[:mid]
        last = array[mid:]
        merge_sort(first)
        merge_sort(last)
        merge_arrays(array, first, last)

def merge_arrays(array, first, last):
    n_f = len(first)
    n_l = len(last)
    i_f = 0
    i_l = 0
    for i in range(len(array)):
        if (i_l == n_l) or (i_f < n_f and first[i_f] < last[i_l]):
            array[i] = first[i_f]
            i_f += 1
        else:
            array[i] = last[i_l]
            i_l += 1


def selection_sort(array):
    for lh in range(len(array)):
        rh = lh
        for i in range(lh + 1, len(array)):
            if array[i] < array[rh]:
                rh = i
        array[lh], array[rh] = array[rh], array[lh]


def bubble_sort(array):
    for end in range(len(array), -1, -1):
        for i in range(end - 1):
            if array[i + 1] < array[i]:
                array[i], array[i + 1] = array[i + 1], array[i]
