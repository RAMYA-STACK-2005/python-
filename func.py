def ASCII(x):
    if type(x) == str:
        return ord(x)
    return (x)
l=["A",-20,"a",94,66]
x=sorted(l, key=ASCII)
print(x)