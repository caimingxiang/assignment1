def k_to_f(k):
    f = k * 9/5 - 459.67
    return f

k = 300.0
f = k_to_f(k)
print("Kelvin of " + str(k) + " is " + str(f) + " in Fahrenheit.")
