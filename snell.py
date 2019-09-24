import math
import stdio
import sys

# Read three floats theta1, n1, and n2 as command-line arguments.

theta1 = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

# Calulate and write the value of the
# angle of refraction theta2 in degrees.
# Use math.radians() and math.degrees().

theta2 = math.degrees(math.asin(n1 / n2 * math.sin(math.radians(theta1))))

# Print theta2.

stdio.writeln(theta2)
