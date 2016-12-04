# --- Day 3: Squares With Three Sides ---

import re

with open("input/03.txt", "r") as input:
  instructions = input.read().split("\n")
  valid_1 = valid_2 = 0

  a = []
  b = []
  c = []

  for instruction in instructions:
    sides = re.findall(" [0-9]+", instruction)
    if len(sides) == 3:
      sides = map(lambda x: int(x), sides)

      # this is for part 2
      a.append(sides[0])
      b.append(sides[1])
      c.append(sides[2])

      # solve part 1
      sides.sort()
      if sides[0] + sides[1] > sides[2]:
        valid_1 += 1

  print "Part 1:",valid_1

  i = 0
  while ( i < len(a)):
    # row a
    sides = a[i:i+3]
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
      valid_2 += 1

    # row b
    sides = b[i:i+3]
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
      valid_2 += 1

    # row c
    sides = c[i:i+3]
    sides.sort()
    if sides[0] + sides[1] > sides[2]:
      valid_2 += 1

    i += 3

  print "Part 2:",valid_2