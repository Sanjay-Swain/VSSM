a = open("lel.txt", 'rt+')
s = "lol"
a.seek(0,2)
print(a.tell())
s = a.read()
print(len(s))