
#Cree un programa en python que solicite la cantidad de temperaturas que desea ingresar, 
#después cree una lista para almacenar cada una de las temperaturas que indicó el usuario que ingresaría, 
#luego solicite al usuario cada una de las temperaturas que se deberán ingresar en la lista.
#Con los valores previamente ingresados a la lista se desea calcular su media y determinar entre 
#todas ellas cuantas son superiores o iguales a esa media.

suma = 0
media = 0
C = 0

N = int(input("Ingrese el número de temperaturas: "))

temperaturas = []

for i in range(1, N + 1):
    temp = float(input("Ingrese las temperaturas: "))
    temperaturas.append(temp)
    suma += temp

media = suma / N

for temp in temperaturas:
    if temp >= media:
        C += 1
    
print(f"La media es {media}")
print(f"El total de temperaturas >= a la media es", C)


