import array
import sys
import string

s = "Given an array of integers nums and an integer target."
a = array.array('u', s)

def sort(s):
    if len(s) < 2:
        return s

    chs = string.ascii_lowercase + string.ascii_uppercase
    pivot = s[0]
    # get pivot
    for c in s:
        if c in chs:
            pivot = c.lower()
            break
    else:
        return s

    i, j = 0, len(s) - 1
    while i < j:
        left, right = s[i].lower(), s[j].lower()
        if (left not in chs) or (left < pivot):
            i += 1
            continue
        if (right not in chs) or (right >= pivot):
            j -= 1
            continue



print(sort(a))
