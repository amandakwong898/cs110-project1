import stdio
import sys

# Read two floats t and v as command-line arguments.

t = float(sys.argv[1])
v = float(sys.argv[2])

# Calculate and write the value of wind chill w.

v = v ** 0.16

w = 35.74 + (0.6215 * t) + (((0.4275 * t) - 35.75) * v)

stdio.writeln(w)
