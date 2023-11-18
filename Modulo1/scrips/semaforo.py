





# 1. ingresar el estado del semaforo
# 2. si el semaforo esta en verde, imprimir "puede cruzar"
# 3. si el esemaforo esta en rojo o amarillo, imprimir "no cruzar"

semaforo = input("ingrese el estado del semaforo: ")

if semaforo == "verde":
    print("puedes cruzar")
elif semaforo == "rojo" or semaforo == "amarillo":
    print("No puedes cruzar")
else: #cualquier otra cuasuhistica
    print("comando no reconocido")

#print(semaforo)