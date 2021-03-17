f = open("p1.txt", "r")
f1 = open("p2.txt", "w")
line = f. readlines()
type(line)
for i in range (0, len(line)):
    if(i%2!=0):
        pass
    else:
        f1.write(line[i])

f1.close()

f1 = open("p2.txt", "r")
lines = f1.read()
print(lines)
f1.close()
f.close()