import os
import sys
os.system("cls")
#Variables
n1 = 0
m2 = 0

#Funciones
def Sumar():
    
    n1= float(input("Ingresa primer sumando"))
    n2= float(input("Ingresa segundo sumando"))
    suma=n1+n2
    print("El resultado es: ", suma) 
    
def Restar():
   
    n1= float(input("Ingresa el minuendo"))
    n2= float(input("Ingresa el sustraendo"))
    resta=n1-n2
    print("El resultado es: ", resta)

def Multiplicar():
   
    n1= float(input("Ingresa primer coeficiente"))
    n2= float(input("Ingresa segundo coeficiente"))
    producto=n1*n2
    print("El resultado es: ", producto)

def Dividir():
   
    n1= float(input("Ingresa el dividendo"))
    n2= float(input("Ingresa el divisor"))
    division=n1/n2
    print("El resultado es: ", division)

def Potencia():
   
    n1= float(input("Ingresa la base"))
    n2= float(input("Ingresa el exponente"))
    potencia=n1**n2
    print("El resultado es: ", potencia)

def Raiz():
   
    n1= float(input("Ingresa el radicando"))
    n2= float(input("Ingresa el indice"))
    raiz=n1** (1/n2)
    print("El resultado es: ", raiz)

menu = """
1) Sumar
2) Restar
3)Multiplicar
4)Dividir
5)Potencia
6)Raiz
8)Salir
"""

print(" CALCULADORA ")
while True:
    print(menu)
    try:
        opcion = int(input("Seleccione una opcion: "))
        if opcion ==1:
            Sumar()
        elif opcion==2:
            Restar()
        elif opcion==3:
            Multiplicar()
        elif opcion==4:
            Dividir()
        elif opcion==5:
            Potencia()
        elif opcion==6:
            Raiz()
        elif opcion==8:
            sys.exit()                
        else:
            print("Ingresa Opcion valida")      
    except ValueError:
        print("ERROR! Ingresa solo numeros ")   


