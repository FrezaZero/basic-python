#not
print("===Not===")
a=True
b=not a
print("data a =", a)
print("data b =", b)

#or
print("===Or===")
a = False
b = False
c = a or b
print(a, "or", b, "=", c)

a = False
b = True
c = a or b
print(a, "or", b, "=", c)

a = True
b = False
c = a or b
print(a, "or", b, "=", c)

a = True
b = True
c = a or b
print(a, "or", b, "=", c)

#and
print("===and===")

a = False
b = False
c = a and b
print(a, "and", b, "=", c)

a = False
b = True
c = a and b
print(a, "and", b, "=", c)

a = True
b = False
c = a and b
print(a, "and", b, "=", c)

a = True
b = True
c = a and b
print(a, "and", b, "=", c)

#xor = akan Ture jika salah satu value True, sisanya False
print("===XOR===")
a = False
b = False
c = a ^ b
print(a, "xor", b, "=", c)

a = False
b = True
c = a ^ b
print(a, "xor", b, "=", c)

a = True
b = False
c = a ^ b
print(a, "xor", b, "=", c)

a = True
b = True
c = a ^ b
print(a, "xor", b, "=", c)
