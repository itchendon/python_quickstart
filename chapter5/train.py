peach = 1
while True:
    d1 = peach // 2 - 1
    d2 = d1 // 2 - 1
    d3 = d2 // 2 - 1
    if d3 == 1:
        print(peach)
        break
    peach += 1
