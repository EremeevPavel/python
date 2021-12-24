a = 3600
b = 60

c = int(input("Your seconds  : "))

h = c // a
c = c - (h * a)

m = c // b
c = c - (m * b)

print(f"{h}:{m}:{c}")
