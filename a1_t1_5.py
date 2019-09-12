def k_to_c(k):
    c = k - 273.15
    return c

k = 300.0
c = k_to_c(k)
print("Kelvin of " + str(k) + " is " + str(c) + " in Celsius.")
