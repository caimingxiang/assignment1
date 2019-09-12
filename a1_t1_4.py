def f_to_k(f):
    k = (f + 459.67) * 5/9
    return k

f = 60.0
k = f_to_k(f)
print("Fahrenheit of " + str(f) + " is " + str(k) + " in Kelvin.")
