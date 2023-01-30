def primos_numeros():
    n = int(input("ingrese numero  entero positivo: "))
    if n > 0:
        for i in range(2,n+1):
            creciente = 2 #desde el numero dos hasta el numero i (divisible)#
            esPrimo = True

            while esPrimo and creciente <i:
                if i% creciente == 0:
                    esPrimo= False

                else:
                    creciente+=1

            if esPrimo:
                print(i,"Es primo")
            i+=1
    else:
        print("el numero ingresado no es positivo")

def main():
    primos_numeros()

main()
