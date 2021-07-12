#Variable que representa una lista
countries = ['Mexico','Estados Unidos','Nigeria','Brasil','Argentina']
print(type(countries))
print(countries)
print(countries[1])
print(countries[0:3])
countries[1] = 'Japón'
countries[3] = 'España'
print(countries)
print(countries[-1])
print(len(countries))
countries[4] = 4
print(countries)
print(type(countries[4]))

#Variable que representa una Lista con un Constructor
states = list(('Nuevo Leon', 'Zacatecas','Durango','CDMX')) #list Constructor
print(states)
print(type(states))