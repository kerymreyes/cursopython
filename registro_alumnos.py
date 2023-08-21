def registrar_alumnos():
    registro_alumnos = {}

    num_alumnos = int(input("Ingrese la cantidad de alumnos a registrar: "))

    for i in range(num_alumnos):
        nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
        edad = int(input(f"Ingrese la edad de {nombre}: "))
        registro_alumnos[nombre] = edad

    return registro_alumnos

def mostrar_mayores_edad(registro):
    print("Alumnos mayores de 18 años:")
    for nombre, edad in registro.items():
        if edad > 18:
            print(f"{nombre} - {edad} años")



    
