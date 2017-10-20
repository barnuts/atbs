#Simply Impossible

def collatz_sequence(x):
    seq = []
    x = (int(input()))
    if (x != 1):
        print("Number can't be 1")
    while x > 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3 * x + 1
        seq.append(x)
    return seq

             
print(collatz_sequence(5))

