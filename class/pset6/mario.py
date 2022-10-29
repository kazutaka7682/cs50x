import cs50

height = cs50.get_int("Height: ")
while height > 8 or height < 1:
    height = cs50.get_int("Height: ")
for i in range(1, height + 1):
    print(" "*(height - i) + "#"*i)
