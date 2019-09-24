import stdio
import sys

# Read three floats m1, m2, and r as command-line arguments.

m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])

# Gravitational constant (given).

G = 6.674e-11

# Calculate and write the value of gravitational force F.

# F = ((m1 * m2) / r ** 2) * G

F = G * m1 * m2 / (r ** 2)

stdio.writeln(F)
