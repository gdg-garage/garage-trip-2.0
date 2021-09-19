def xxx(haystack, needle):
    low = 0
    high = len(haystack) - 1

    while low <= high:
        middle = low + (high - low) // 2

        if haystack[middle] == needle:
            return middle
        elif haystack[middle] < needle:
            low = middle + 1
        else:
            high = middle - 1
    return -1

