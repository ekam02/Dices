from dices import Dices

dices = None

while True:
    cant = int(input('¿Cuántos datos va a lanzar?: '))
    if cant > 0:
        dices = Dices(cant)
        break
    print('Intenta ingresar un entero positivo')

print(dices)
