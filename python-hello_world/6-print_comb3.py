for i in range(10):
    for j in range(i + 1, 10):
        print("{i}{j}".format(i=i, j=j), end=', '  if i < 8 or j < 9 else '\n')