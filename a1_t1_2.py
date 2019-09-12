def c_to_k(c):
    k = c + 273.15
    return k

c = 20.0
k = c_to_k(c)
print("Celsius of " + str(c) + " is " + str(k) + " in Kelvin.")
