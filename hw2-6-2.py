# Author MEE 9/26/21

rp = input("What's the radius of the cylinder?: ")
hp = input("What's the height of the cylinder?: ")

h = int(hp)
r = int(rp)

sa = 2 * 3.14 * r * h + 2 * 3.14 * (r ** 2)
v = 3.14 * (r **2) * h

print("Surface Area:",sa,"Volume:",v)