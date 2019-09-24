import math
import stdio
import sys

# Read two floats avg and t as command-line arguments.

avg = float(sys.argv[1])
t = float(sys.argv[2])

# Calculate the probability; use math.exp(x) to calculate e^x.

Pt = math.exp(-avg * t)

# Write the value of Pt.

stdio.writeln(Pt)
