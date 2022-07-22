# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.
#v = 3.14 r2 h
#sa = 2pir(h+r)

#volume
height = 5
pi = 3.14
radius = 3.14
volume = pi * radius**2 *5
print(volume)

#surface area
surface_area = ((2*pi) * radius) * (height * radius)
print(surface_area)