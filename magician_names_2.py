def make_great(magician_names):
    n=0
    for magician in magician_names:
        magician_names[n]= "great"+ " " + magician_names[n]
        n=n+1
    n=n-1
    return magician_names

magician_names = ['peter','ronke', 'sam', 'bodurin']
magician_names = make_great(magician_names)
print(magician_names)