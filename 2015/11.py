"""--- Day 11: Corporate Policy ---"""

def containsStraight(p):
  for i in range(len(p) - 2):
    if ord(p[i]) + 2 == ord(p[i+1]) + 1 == ord(p[i+2]):
      return True # break early
  return False

def containsIllegals(p):
  illegals = ["i", "o", "l"]

  for i in illegals:
    if i in p:
      return True
  return False

def containsDouble(p):
  count = 0
  i = 0
  while i < len(p) -1:
    if p[i] == p[i+1]:
      count += 1
      i += 2 # skip next
    else:
      i += 1
  return count > 1

def checkPass(password):
  return containsStraight(password) and containsDouble(password) and not containsIllegals(password)

def incr(s):
  if s == '':
    return 'a'
  if s[-1] < 'z':
    return s[0:-1] + chr(ord(s[-1])+1)
  return incr(s[:-1]) + 'a'

def day_11 (instructions):
  password = incr(instructions)

  while not checkPass(password):
    password = incr(password)
  return password

with open("input/11.txt") as f:
  for line in f:
    a = day_11(line.replace("\n", ""))
    b = day_11(incr(a))
    print(a)
    print(b)
