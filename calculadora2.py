# julian andres calambas ordonez
def sumar(n1,n2):
    try:
        r=n1+n2
        print('el resultado de la SUMA es: ' + str(r))
    except:
        print("No ingresate valores validos para realizar la operacion")

def restar(n1,n2):
    try:
        r=n1-n2
        print('el resultado de la RESTA es: ' + str(r))
    except:
        print("No ingresate valores validos para realizar la operacion")


def multiplicar(n1,n2):
    try:
        r=n1*n2
        print('el resultado de la MULTIPLICACION es: ' +  str(r))
    except:
        print("No ingresate valores validos para realizar la operacion")

def dividir(n1,n2):
    try:
        if n2>0:
            r=n1/n2
            print('el resultado de la DIVICION es: ' + str(r))
        else:
            print('ningun numero es divisible por CERO \n en este caso el segundo numero tiene que ser mayor que CERO')
    except:
        print("No ingresate valores validos para realizar la operacion")
    



def operaciones():

  try:
    n= int(input("Elige la operacion a realizar : \n 1. Sumar \n 2. Restar \n 3. multiplicar \n 4. dividir \n 5. salir \n Ingrese la opcion. "))

    while n==1 or n==2 or n==3 or n==4:
      try:

          n1= int(input("ingresa el primer numero "))
          n2= int(input("ingresa el segundo numero "))

          if n==1:
              valor=sumar(n1,n2)
          if n==2:
              Valor=restar(n1,n2)
          if n==3:
              valor=multiplicar(n1,n2)
          if n==4:
              valor=dividir(n1,n2)

          n= int(input("Elige la operacion a realizar : \n 1. Sumar \n 2. Restar \n 3. multiplicar \n 4. dividir \n 5. salir \n Ingrese la opcion. "))  
          if n==5:
              break

      except ValueError:
          print("El valor ingresado no fue valido ...")
          break
            

  except ValueError:
    print("Debes ingresar una opcion Correcta...")
  else:
    print("Opcion no disponible")




calculadora=operaciones();