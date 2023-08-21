import library.calculadora as cal

n1 = float(input("Ingresar primer número: ") )
n2 = float(input("Ingresar segundo número: ") )

while True:
    print("""
    Elige la operacion a realizar:
    
    1 Sumar los dos números
    2 Restar los dos números
    3 Multiplicar los dos números
    4 Dividir los dos números
    5 Apagar calculadora
    """)
    opcion = int(input("Elige la operacion: ") )     
    if opcion == 1:
        print(" ")
        print('El Resultado de la Suma es:',cal.suma(n1,n2))
    elif opcion == 2:
        print(" ")
        print('El Resultado de la Resta es:',cal.resta(n1,n2))
    elif opcion == 3:
        print(" ")
        print('El Resultado de la Multiplicacion es:',cal.multiplicacion(n1,n2))
    elif opcion == 4:
        print(" ")
        print('El Resultado de la Division es:',cal.division(n1,n2))
    elif opcion == 5:
        print('!Hasta Pronto!')
        break
    else:
      print("Dato Invalido")