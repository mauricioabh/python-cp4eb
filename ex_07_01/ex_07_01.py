fh = open('mbox-short.txt')

for lx in fh:
    print(lx.upper().rstrip())