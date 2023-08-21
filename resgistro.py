import library.registro_alumnos as al


while True:
    registro = al.registrar_alumnos()
    al.mostrar_mayores_edad(registro)

    repetir = input("¿Desea repetir el programa? (s/n): ")
    if repetir.lower() != 's':
        break


