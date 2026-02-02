# The "basic" type float

nb=123.56 # fixed notation

nb=.7
print(nb, type(nb))

nb=8.
print(nb, type(nb))

nb=123.56E+45 # scientific notation
print(nb, type(nb))
nb=.34E-5 # scientific notation
print(nb, type(nb))
nb=123.56e+45 # scientific notation
print(nb, type(nb))

nb=123.5676543
print(f"{nb:.2f}")

# Operator: + - * / % ** //

print(234.56E+145 ** 3) # OverflowError max capacity of float is exceeded





