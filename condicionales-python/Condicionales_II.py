# USo de if, elif, y else:

print("Controlador de personal segun su edad")
print("")
print("Ingrese su edad antes de continuar: ")
edad=input()

def control(edad):
    if(edad<18):
        print("Usted es menor de edad, NO puede pasar. Regrese otro dia.")
    elif(edad>50):
        print("Usted puede pasar GRATIS, disfrute el acto. ")    
    else:
        print("Usted puede pasar, despues de pagar el boleto de entrada. ")
    
print(control(edad))