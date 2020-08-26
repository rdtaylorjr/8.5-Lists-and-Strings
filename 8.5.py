fname = input("Enter file name: ")
count = 0
if len(fname) < 1:
    fname = "mbox-short.txt"
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
