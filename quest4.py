a = int(input("Your number: "))

b = 0

while a > 0:
    c = a % 10
    if c >= b:
        b = c
    a //= 10
print(b)
