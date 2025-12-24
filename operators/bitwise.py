a = 10
b = 4

print(a & b)   # Bitwise AND
print(a | b)   # Bitwise OR
print(a ^ b)   # Bitwise XOR
print(~a)      # Bitwise NOT
print(a << b)  # Left Shift
print(a >> b)  # Right Shift

# a = 10 → 1010
# b = 4 → 0100
# a & b → 1010 & 0100 = 0000 → 0
# a | b → 1010 | 0100 = 1110 → 14
# a ^ b → 1010 ^ 0100 = 1110 → 14
# ~a → ~1010 = -(10+1) → -11
# a << b → 1010 << 4 = 10100000 → 160
# a >> b → 1010 >> 4 = 0000 → 0