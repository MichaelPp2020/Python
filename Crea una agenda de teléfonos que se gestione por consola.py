def obtener_agenda():
    contactos = {}
    while True:
        nombre = input(
            "Ingrese un nombre o déjelo vacío para terminar de agregar: ")
        if nombre == "":
            break
        if nombre in contactos:
            print("Nombre ya existente")
        else:
            telefono = input(f"Ingrese el teléfono de {nombre}: ")
            contactos[nombre] = telefono
    return contactos

def busqueda():
    contactos = obtener_agenda()
    consulta= True
    print("opciones:")
    print ("1 Busqueda")
    while consulta:
        opcion = ""
       
        while opcion != ("1"):
            
            opcion = input ("ingrese el valor 1 para consultar  ")
            print ("->")
        if opcion =="1":
            busqueda = input ("Nombre ")
            if busqueda not in contactos:
                print("no se encontro en la Agenda")
            else:
                telf = contactos[busqueda]
                print (busqueda," :", telf)
        
        break
  
def main():
    busqueda()


main()
