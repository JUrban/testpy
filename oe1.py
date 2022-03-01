def f(x):
  x1 = 9
  for i1 in range (1,(x + 3) + 1):
    x1 = x1 // 2 if x1 % 2 <= 0 else 3*x1 + 1
  return x1

for x in range(16):
  print (f(x))
