# program to create dictionary

cars = {
    "name": "Toyota",
    "date": "2019",
    "color": "black"
}
print(cars)
print(cars.keys())
print(cars.values())
print(cars.items())

for x in cars:
    print(cars[x])

for x in cars.values():
    print(x)

for x in cars.keys():
    print(x)

for x, y in cars.items():
    print(x,y)