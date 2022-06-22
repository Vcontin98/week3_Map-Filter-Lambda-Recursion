places = [('Nassau', 32), ('Boston', 12), ('Los Angeles', 44), ('Miami', 29)]

# HINT: KEEP IN MIND PEMDAS. USE THE CELCIUS - FAHRENHEIT CONVERSION
# F = C * 9/5 + 32

Fahrenheit = list(map(lambda x: f"{x[0]} {(9/5)*x[1]+32}", places))
print (Fahrenheit)