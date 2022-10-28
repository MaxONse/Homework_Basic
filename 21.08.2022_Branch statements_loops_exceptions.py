distance = float(input("Enter distance in meters:"))
convert = input("Which do convert: miles, foot, inches or yards?")
miles = 1609
inches = 0.0254
yards = 0.9144
foot = 0.3048
m = distance / miles
i = distance / inches
y = distance / yards
f = distance / foot
if convert == 'miles':
    print("in miles it will be:", m, "mile")
elif convert == 'inches':
    print("in inches it will be:", i, "inch")
elif convert == 'yards':
    print("in yards it will be:", y, "yard")
elif convert == 'foot':
    print("in foots it will be:", f, "foot")
else:
    print("error type input")