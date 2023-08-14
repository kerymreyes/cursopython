#REPASO
#EJERCICIO1
nombreUsuario='Noelia Tatiana Guadalupe Reyes Lopez'
print(f'!Hola, {nombreUsuario}! Bienvenido a nuestro Programa.')
print('!Hola, %s! Bienvenido a nuestro programa.'%(nombreUsuario))
print('!Hola',nombreUsuario,'Bienvenido a nuestro programa')
#EJERCICIO2
valorBase=12
valorAltura=6
areaTriangulo=valorBase*valorAltura/2
print('El area del triangulo es: %.2f'%(areaTriangulo))
#EJERCICIO3
nombreUsuario = 'Kerym Reyes'
edadUsuario = '26'
ciudadResidencia = 'Soyapango'
print(f'{nombreUsuario}, {edadUsuario}, {ciudadResidencia}')
#TIPOS DE DATOS
x=1 #int
y=1.465281 #float
z=2j #complex
print(type(x),type(y),type(z))
#FLOAT
ejemploFloat1=1.1
ejemploFloat2=25.2278
ejemploFloat3=854.672
ejemploFloat4=0
print(type(ejemploFloat1), type(ejemploFloat2), type(ejemploFloat3), type(ejemploFloat4))
X=35E3
y=12e4
z=1.2e4
print(x,y,z)
print(type(x),type(y),type(z))
#COMPLEX
x=3+5j
y=-5j
z=-3+0j
print(type(x),type(y),type(z))
#PRACTICA EN CLASE
print(type(3)) #int
print(type(3.14)) #float
print(type(1+8j)) #complex
print(type('Helow World!')) #str
print(type([1,2,3])) #list
print(type({1:'one', 2:'two', 3:'three'})) #dictionary
print(type({1,2,3})) #set
print(type((1,2,3))) #tuple
#float, list:calcular el promedio de notas de un alumno
notas=[7.0, 6.0, 9, 10.00, 5.6, 9.4, 5.6]
promedio=sum(notas)/len(notas)
print('El promedio de notas es:', promedio)
#bool:validar un campo
usuarioRegistrado= False
if usuarioRegistrado:
    print('Bienvenido al curso')
else:
    print('El usuario no esta en el curso')
#list:tipo str
nombre=['cristian','dennis','edwin','herny','roberto']
print(f'Lista de nombres: {nombre}')
#tuple:Dias de la semana y otra con valores
diasSemana=('L','M','W','J','V')
numeros=(1,2,3,4,5)
print(diasSemana)
print(type(diasSemana))
print(numeros)
print(type(numeros))
#dict: Nombres y Contactos
dictContacts={
    'cristian': 12354645,
    'dennis':6549846,
    'edwin':65432185,
    'herny':98746321,
    'roberto':2135874
}
print(type(dictContacts))
x=1
y=2.8
z=5j
print(type(x),type(y),type(z))
convertX=float(x)
convertY=complex(y)
print(type(convertX),type(convertY))
#forma1
edadUsuario1= input('Ingrese la edad del usuario:')
print(type(edadUsuario))
edadUsuario1=int(edadUsuario1) #Hace la conversion de str -> int
print(type(edadUsuario1))
print('La edad es:',edadUsuario1)
#Forma2
edadUsuario1=int(input('Ingrese la edad del usuario:'))
print(type(edadUsuario1))
print('La edad es:',edadUsuario1)
#Cadena de str -> int
cadena='46531987'
cadena=int(cadena)
#Cadena de str -> float
cadena='3.75'
strFloat=float(cadena)
print(type(cadena), type(strFloat))
print(cadena+cadena+cadena)
print(strFloat+strFloat)
#entero int -> cadena
entero=45
type(entero)
cadenaInt=str(entero)
print(type(cadenaInt))
#Flotante float -> cadena
flotante=4.69
cadenaFlotante=str(flotante)
print(type(cadenaFlotante))
#Lista a cadena
lista=[1,2,3,4,5]
cadenaLst=str(lista)
print(type(cadenaLst))
print(cadenaLst)
#Cadena a lista
cadena='[1,2,3,4,5,6]'
lista=eval(cadena)
print(type(lista))
print(lista)
#Cortar cadenas
a='Hello World:Hola Mundo'
b='Noche de tacos de birria'
print(len(a),len(b))
print(a[2:20])
print(b[4:20])
print(a[:9])
print(a[7:])
print(a[-5:-2])
#EJERCICIOS
#1
mensaje='Bienvenido a Python'
print(mensaje)
#2
poema="""Recuerde el alma dormida
Avive el seso y despierte
Contemplando
Cómo se pasa la vida,
Cómo se viene la muerte,
Tan callando,
Cuán presto se va el placer,
Cómo, después de acordado
Da dolor,
Cómo, a nuestro parecer,
Cualquier tiempo pasado
Fue mejor."""
print(poema)
#3
cadena='Programacion en python'
subcadena= cadena[-6:]
print(subcadena)
subcadena2=cadena[16:22]
print(subcadena2)
#4
cadena='abcdefghij'
print(cadena[2:6])
#5
cadena='Python es genial'
subCadena=cadena[-9:]
print(subCadena)






