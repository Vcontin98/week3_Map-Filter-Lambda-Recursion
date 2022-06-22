# .sort(key=)
# sorted(key=)

authors = ["Connor Milliken", "Victor aNisimov", "Andrew P. Garfield", "David HassELHOFF", "Oprah wInfrey"]

# HINT: YOU'LL NEED TO CONVERT EACH PERSON'S NAME (A STRING) INTO A LIST IN ORDER TO GRAB THE LAST NAME BY
# THE INDEX
#~!@#$%&*()_+ = 1
# 123457890 = 50
# abcd = 70
# DERK = 90


authors.sort(key=lambda name: name.split(" ")[-1].lower())

print(authors)
