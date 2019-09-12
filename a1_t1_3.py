def f_to_c(f):
    c = (f - 32) * 5/9
    return c

f = 68.0
c = f_to_c(f)
print("Fahrenheit of " + str(f) + " is " + str(c) + " in Celsius.")
