# Ejercicio 1
resultado=max(5,10,3,8)
print(resultado)
# Ejercicio 2
resultado=round(3.14159,2)
print(resultado)
# Ejercicio 3
resultado=min(5,10,3,8)
print(resultado)
#Practica
nombre='kerym reyes'
edad='26'
longitud=len(nombre)
print('Mi nombre es',nombre,'y mi edad es',edad,'la longitud del mensaje es',longitud)
#Practica2
valor = 27
if valor > 26:
    print('el numero es mayor que mi edad')
    if valor % 2 ==0:
        print('el numero es par')
    else:
        print('el numero es impar')
else:
    print('el numero no es mayor que la edad')
#imprimir varias variebles en una linea
nombre='Kerym Reyes'
edad=26
print('Mi nombre es:',nombre,'y tengo',edad,'años.')
valorHora=17.5
totalHoras=8
sueldoDiario=valorHora*totalHoras
print('Nombre Empleado:',nombre,'El precio por hora trabajada:',valorHora,'Y el sueldo diario es:',sueldoDiario)
#F-String
print(f'Nombre Empleado:{nombre} El precio por hora trabajada:{valorHora} Y el sueldo diario es:{sueldoDiario}')
#imprimir por tipo de variable(%)
#print('Mi nombre es %tipodevariable y tengo %tipovariable2 años.\n\n'%(nombre,edad))
print('Mi nombre es %s y tengo %d años.\n\n'%(nombre,edad))
nombre='kerym'
edad=26
peso=160
print('Mi nombre es %s y tengo %d años y peso %d.\n\n'%(nombre,peso,edad))
nombre='kerym'
precioHora=17.5
horasTrabajadas=44
print('Mi nombre es %s ,cobro: %d por hora y trabaje %.2f\n\n'%(nombre,horasTrabajadas,precioHora))
#tabulacion en la impresion y salto de linea
print('Nombre: \n\t Kerym \n Edad: \n\t26')
mensaje='TeneMos qUe HAcer tareA'
mensajeMinuscula=mensaje.lower()
mensajeMayuscula=mensaje.upper()
print(mensajeMinuscula)  
print(mensajeMayuscula)
nombreEmpleado1='Kerym Vladimir Reyes Velasquez'
nombreEmpleado2='kerym vladimir reyes velasquez'
nombreEmpleado1==nombreEmpleado2
nombreEmpleado1.lower()==nombreEmpleado2.lower()
print(nombreEmpleado1.lower())
print(nombreEmpleado2.lower())
x=str(3)
y=int(3)
z=float(3)
print(x,y,z)
print('\n\n')
#Aplicacion de conocimientos TAREA
print('APLICACION DE CONOCIMIENTOS - TAREA\n')
nombres='Kerym Vladimir'
primerApellido='Reyes'
segundoApellido='Velasquez'
edad=26
Nacionalidad='Salvadoreña'
sexo='Hombre'
print(f'Mis nombres son: {nombres}\nMi primer apellido es: {primerApellido}\nMi segundo apellido es: {segundoApellido}\nMi edad es: {edad}\nSoy de nacionalidad: {Nacionalidad}\nMi sexo es: {sexo} ')
