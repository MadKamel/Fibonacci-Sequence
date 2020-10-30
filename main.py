print()
x = 0
y = 1
z = 1
for i in range(15):
  print(str(x))
  z = y
  y = x
  x = x+z
