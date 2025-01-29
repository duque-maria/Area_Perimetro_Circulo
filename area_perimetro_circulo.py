import math

print("############################")
print("Area perímetro del circulo")
print("############################")
      

# input
r = input("Digite el valor del radio: ")
r = int(r)

# Processing
p = 2*math.pi*r
a = math.pi*r*r

# Output
print("#############################")
print("el área es : " + str(a))
print("el perímetro es : " + str(p))
print("#############################")