import stdio
import sys

# Read integers n1, n2, and float p as command-line arguments.

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])

# Given probability (q).

q = 1 - p

# Calculate and write the values of P1 and P2, separated by
# a space.

P1 = (1 - (p/q) ** n2) / (1 - (p/q) ** (n1 + n2))

P2 = (1 - (q/p) ** n1) / (1 - (q/p) ** (n1 + n2))

stdio.write(P1)
stdio.write(" ")
stdio.writeln(P2)
