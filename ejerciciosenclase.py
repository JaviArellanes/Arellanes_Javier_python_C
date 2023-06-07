numero = int(input('Escriba un número positivo: '))
if numero < 0:
    print('Escribe un número positivo!')
print(f'Has escrito el número: {numero}')


print("Este programa mezcla dos colores.")
print("  r. Rojo      a. Azul")
primera = input("  Elija un color (r o a): ")
if primera == "r":
    print("  a. Azul      v. Verde")
    segunda = input("  Elija otro color (a o v): ")
    if segunda == "a":
        print("La mezcla de Rojo y Azul produce Magenta.")
    else:
        print("La mezcla Rojo y Verde produce Amarillo.")
else:
    print("  v. Verde    r. Rojo")
    segunda = input("  Elija otro color (v o r): ")
    if segunda == "v":
        print("La mezcla Azul y Verde produce Cian.")
    else:
        print("La mezcla Azul y Rojo produce Magenta.")
print("Hasta la proxima")





#lista  a tupla
lista = [1, 2, 3]
print(type(lista))
tupla = tuple(lista)
print(type(tupla)) #<class 'tuple'>
print(tupla)       #(1, 2, 3)

l = [1, 1, 1, 3, 5]
print(l.count(1)) #3
nombre="maria"
print(nombre.count("a"))

l = [7, 7, 7, 3, 5]
print(l.index(5)) #4
  