def double(n):
  return n * 2

doublesGenerator = (double(i) for i in range(1, 6))

print([*range(1, 6)])

# * is the unpacking operator (spread)
print([*doublesGenerator])