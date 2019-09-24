import stdio
import sys

# Get m month (int) from the command line.
m = int(sys.argv[1])

# Get d day (int) from the command line.
d = int(sys.argv[2])

# Get y year (int) from the command line.
y = int(sys.argv[3])

# Calculate and write the value of day of the week D.

y0 = y - (14 - m) // 12
x0 = y0 + y0 // 4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
d = (d + x0 + 31 * m0 // 12) % 7

# Use // (floored division) for / and % for mod.

stdio.writeln(d)
