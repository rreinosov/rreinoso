
personas = []

def mostrar_menu():
    print ('1.guardar datos')
    print ('2.buscar datos')
    print ('3.imprimir certificado')
    print ('4.salir')

def datos():
    nombre = input('ingrese su nombre :')
    
    if len(nombre) <= 8:
        print('su nombre debe tenr minimo 8 caracteres')
   
    nif = input('ingrese su nif :')
    if len(nif) < 0:
        print('su nif debe tener mas de 0 numeros')    
        
    edad = int(input('ingrese su edad '))
    if edad >= 0:
        print(' su edad ')
        
    persona = {
        'nombre': nombre,
        'nif': nif,
        'edad' : edad
        }    
    
    personas.append(persona)   
    
    
    
def buscar():
    nif = input('ingrese el nif de la pernosa  :')
    for persona in personas:
        if persona['nif'] == nif:
            print('\033[91mesta es la informacion de la persona que busca\033[0m ')
            print(f"{persona['nif']}")
            print(f"{persona['nombre']}")
            print(f"{persona['edad']}")
            if persona['nif'] == 'es':
                print('la persona pertenece a la union europea')
            else:
                print('la persona  no pertenece a la union europea')
            return
    print('no existe nadie con ese nif ')
    print('intente denuevo ')  
    
    
def inprimir():
    opc = int(input('ingrese la opcion que desea')) 
    print('1.certificado de nacimiento')
    print('2.estado conyugue')
    print('3.pertenencia union europea')
    
    
    datos()
    if opc == 1:
        print('certificado de nacimiento')
        buscar()  
    elif opc == 2:
        print('estado conyugue')
        buscar()
    elif opc == 3:
        print('pertenencia union europea')
        buscar()           
    else:
        return
            
def menu():
    while True:
        mostrar_menu()
        opc = int(input('ingrese la opcion que desea:'))
        if opc == 1:
            datos()
        elif opc == 2:
            buscar()      
        elif opc == 3:
            (inprimir())
        elif opc == 4:
            break
        else:
            print('opcion invalida , ingrese otra opcion ')
            return 
        
menu()           
        