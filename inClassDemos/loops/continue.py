for x in range(33):
    if (x % 3) == 0:
        print("This is the 3rd number I am being skipped... sort of")
        continue # <-- skip to the next block
    print(x)

#  Output skips every 3rd number - 1 2 4 5 7 8 10