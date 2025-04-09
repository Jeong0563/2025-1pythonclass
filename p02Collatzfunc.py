def collatz(i):
    ncount = 0
    while i > 1:
        if i % 2 == 0:
            i = i / 2
        elif i % 2 != 0:
            i = 3 * i + 1
        ncount += 1
    return ncount