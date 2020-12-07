def bubbles_sort(arr):
    """
    :param arr: [2, 8, 26, -30, -10, 27, 13, -20, -30]
    :return: -30 -30 -20 -10 2 8 13 26 27
    """
    for i in range(len(arr) -1):
        need_replace = False
        max_elem = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < max_elem:
                need_replace = True
                max_elem = arr[j]
                max_pos = j
        if need_replace:
            tmp = arr[i]
            arr[i] = max_elem
            arr[max_pos] = tmp
    return arr

