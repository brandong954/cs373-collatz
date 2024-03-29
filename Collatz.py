#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

cache = {}

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    assert i > 0
    assert j > 0
    if i > j :
        temp = i
        i = j
        j = temp
    maxCycle = 0
    for num in range(i, j + 1) :
        n = num
        if num in cache :
            c = cache[num]
        else :
            c = 1
            while n > 1 :
                if (n % 2) == 0 :
                    n = (n // 2)
                else :
                    n = (3 * n) + 1   
                c += 1
            assert c > 0
            cache[num] = c
        maxCycle = max(maxCycle, c)
    assert maxCycle > 0
    return maxCycle
        

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
