

def hanoi_towers(n, source, destination, auxilliary):
    if n > 0:
        hanoi_towers(n-1, source, auxilliary, destination)
        print("Move", n, "from:", source, "to:", destination)
        hanoi_towers(n-1, auxilliary, destination, source)


hanoi_towers(4, 'A', 'C', 'B')