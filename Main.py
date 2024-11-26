from areacalc import calcarea
from printlib import printarea


# Prompt user for three bases
base1 = float(input("Enter the first base: "))
base2 = float(input("Enter the second base: "))
height = float(input("Enter the height: "))

# Areacalc call
area = calc(base1, base2, height)
print(area)
