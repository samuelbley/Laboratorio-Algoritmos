a = 0
b = 0
c = 0

for i in range(10):
    op = input("A/B/C: ")

    if op == "A":
        a = a + 1
    if op == "B":
        b = b + 1
    if op == "C":
        c = c + 1

print("A:", a)
print("B:", b)
print("C:", c)

print("A %:", (a/10)*100)
print("B %:", (b/10)*100)
print("C %:", (c/10)*100)