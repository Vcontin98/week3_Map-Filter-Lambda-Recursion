places = [' ', 'Argentina', '  ', 'San Diego', '', '   ', '', 'Boston', 'New York']
# = [Argentina, San Diego, Boston, New York]

# HINT: LOOK FOR A STRING METHOD THAT REMOVES WHITESPACE




places = filter(str.strip, places)
print(list(places))