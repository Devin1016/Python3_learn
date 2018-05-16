# i = 1

# while i <= 10:
#     print(i)
#     i += 1

# line = 0

# while line <= 3:
#     sp = ' ' * line
#     star = '*' * (7 - line * 2)
#     print(sp + star)
#     line += 1

# line -= 1

# while line >= 0:
#     line -= 1
#     sp = ' ' * line
#     star = '*' * (7 - line * 2)
#     print(sp + star)

lines = 7
line = 0
middle = 4

while line < lines:
    if line < middle:
        sta = line
    else:
        sta -= 1

    sp = ' ' * sta
    star = '*' * (lines - sta * 2)
    print(sp + star)

    line += 1
