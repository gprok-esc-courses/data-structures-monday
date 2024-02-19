# Calculate the hash value of any integer
# as a hash value in the range 0-9
def hash_int(n: int) -> int:
    return n % 10

# Calculate the hash value of any string
# as a hash value in the range 0-99
def hash_str(s: str) -> int:
    total = 0
    for c in s:
        total += ord(c)
    return total % 10


print(hash_int(1027))
print(hash_int(1027))

print(hash_str('John'))