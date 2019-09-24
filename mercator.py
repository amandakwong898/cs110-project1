import math
import stdio
import sys

# Read two floats (1) latitude in degrees and (2) longitude
# in degrees as command-line arguments and writes the
# corresponding x and y values (Mercator projection),
# separated by a space.

latitude = float(sys.argv[1])
longitude = float(sys.argv[2])

# Use math.radians() to convert degrees to radians.

y0 = math.radians(latitude)

# Use math.log() for natural logarithm.

x = longitude
y = math.log((1 + (math.sin(y0))) / (1 - (math.sin(y0)))) / 2

stdio.write(x)
stdio.write(" ")
stdio.writeln(y)
