def make_great(magician_names, new_magician_names):
    while magician_names:
        move = "great" +" " + magician_names.pop()
        new_magician_names.append(move.title())
    return new_magician_names
  
magician_names = ['peter','ronke', 'sam', 'bodurin'] 
new_magician_names = []

magician_namesf=make_great(magician_names, new_magician_names)
print(magician_namesf)
print(magician_names)