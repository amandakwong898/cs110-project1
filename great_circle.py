import math
import stdio
import sys

# Read four floats x1, y1, x2, and y2 as command-line arguments.

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])

x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

sinx1 = math.sin(math.radians(x1))
sinx2 = math.sin(math.radians(x2))

cosx1 = math.cos(math.radians(x1))
cosx2 = math.cos(math.radians(x2))

y = math.cos(math.radians(y1 - y2))

# Calculate and write the value of great-circle distance d.

d = (math.acos((sinx1 * sinx2) + (cosx1 * cosx2 * y)))

stdio.writeln(math.degrees(d) * 111)
