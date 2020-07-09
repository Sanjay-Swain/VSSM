f = open("./testfile2.txt", "r+")

size = f.seek(0, 2)
if size < 4*2:
    padding = ((4*2) - (size % (4 * 2))) % (4*2)
    padded = [True, padding]
    while 0 < padding:
        f.write(" ")
        padding -= 1
f.seek(0)
temp = [None, None]
temp[0] = f.read(4)
temp[1] = f.read(4)
next_temp = f.tell()
f.seek(f.tell() - 7)
pointer = f.tell()
print([f.tell(), pointer])
lol = False
while True:
    if (temp[0] != "\x00") and (temp[0] != ""):  # idk why, but i had to apparently
        f.write(temp[0])
        f.flush()
        f.seek(next_temp)
        temp[0] = f.read(4)
        next_temp += 4
        pointer += 4
        f.seek(pointer)
        temp[0], temp[1] = temp[1], temp[0]
    else:
        break
if padded[0] is True:
    size = f.seek(0,2)
    f.truncate(size - padded[1])