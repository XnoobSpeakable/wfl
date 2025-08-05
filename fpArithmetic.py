# Fixed Point Arithmetic Library version α0.0.1 (broken)

def parse(input):
    return input.split(".")

def unparse(input):
    return input[0] + "." + input[1]

def add(a, b):
    ap = parse(a)
    bp = parse(b)
    sizea = len(ap[1])
    sizeb = len(bp[1])
    if sizea > sizeb:
        bp[1] += "0" * (sizea - sizeb)
    elif sizeb > sizea:
        ap[1] += "0" * (sizeb - sizea)

    azero = 0
    bzero = 0
    for i in ap[1]:
        if i != "0":
            break
        azero += 1
    for j in bp[1]:
        if j != "0":
            break
        bzero += 1

    zeroes = max(azero, bzero)

    fraction = "0" * zeroes + str(int(ap[1]) + int(bp[1]))
    integer = int(ap[0]) + int(bp[0])

    if len(fraction) > sizea:
        fraction = fraction[1:]
        integer += 1
    integer = str(integer)
    return unparse([integer, fraction])
    

while True:
    x = input("Enter two fixed point numbers to add (format: x.y): ")
    y = input("Enter another fixed point number to add (format: x.y): ")
    print("Result:", add(x, y))