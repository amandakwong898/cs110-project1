import random
import stdio
import sys

# Read an integer n as command-line argument.

n = int(sys.argv[1])

# Use the function random.randomint() with suitable arguments to
# simulate two n-sided die rolls.

# Write the sum of the numbers rolled.

val = random.randint(n, n + n)

stdio.writeln(val)
