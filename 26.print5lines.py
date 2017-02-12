#print5lines.py
infile = open(someFile,"r")
for i in range(5):
    line = infile.readline()
    print(line[:-1])

