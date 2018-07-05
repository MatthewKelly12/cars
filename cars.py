colors = 'red'
print(colors)

cars = set()
cars.add('Ram')
print(cars)

cars.add('Camry')
cars.add('Accord')
cars.add('CRV')
cars.add('Dynasty')
print(cars)

print (len(cars))

dodge = ['Dakota', 'Viper']
print(dodge)


honda = set()
honda.add('Pilot')
honda.add('Civic')
print(honda)

cars.update(honda)
print(honda)

print(cars)

cars.remove("Accord")
print(cars)

junkyard = set()
junkyard.update(['Mustang', 'Camaro'])
print (junkyard)

junkyard.update(['Cavalier', 'Wrangler', 'CRV', 'Pilot'])
print(junkyard)

print(cars.intersection(junkyard))

print(cars.union(junkyard))
print(cars)

inventory = cars.union(junkyard)
print(inventory)

inventory.discard('Wrangler')
print(inventory)

inventory.discard('Pilot')
print(inventory)
