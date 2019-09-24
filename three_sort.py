import stdio
import sys

# Read three integers x, y, and z as command-line arguments.

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

# Find the smallest value m and largest value M using min()
# max() functions.

m = min(x, y, z)
M = max(x, y, z)

# Find the middle value as an arithmetic combination of x, y, z, m, and M.

mid = (x + y + z) - (m + M)

# Write the numbers in ascending order.

stdio.write(m)
stdio.write(" ")
stdio.write(mid)
stdio.write(" ")
stdio.writeln(M)
