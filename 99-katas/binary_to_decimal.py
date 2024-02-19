
def binary_to_decimal(b: str) -> int:
    exponent = 0
    total = 0
    for i in range(len(b)-1, -1, -1):
        if b[i] == '1':
            total += 2 ** exponent
        exponent += 1
    return total


print(binary_to_decimal('10011'))