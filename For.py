class For:
    def __init__(self):
        pass
    
    
    def usoFor(self):
        # ciclo repetitivo de incrementos o decrementos se ejecuta por verdadero
        nombre = "Alejandro"
        datos=["Alejandro",19,True]
        # pos      0        1   2
        numeros=(2,5,6,4,1)
        docente= {'nombre':'Alejandro','edad': 19,'fac':'faci'}
        listaNotas = [(30,40),(20,40),(50,40)]
        listaAlumnos = [{"nombre":"Erick","final":60}],{"nombre":"Maria","final":50}
        
        
        # j=0 
        # while j<5:
        #     print('while',j)
        #     j=j+1
        
        # for i in range(5):
        #     print('for',i,end="")
        # print()
        # for i in range(1,5):
        #     print('for',i,end="")
        # print()
        # for i in range(1,11,1):
        #     print('for',i,end="")
        # print()
        # for i in range(13,2,-2):
        #     print('for',i,end="")
                
        # lon = len(numeros)
        # for pos in range (lon):
            #   if pos%2 ==0{}:
        #     print(pos.numeros[pos])
         
          
        # for elem in datos:
        #     print(elem,end="")
        # for elem in nombre:
        #     print(elem,end="")
        # lon = len(datos)
        # for pos in range (lon):
        #     print(pos,datos[pos])  
             
        # for pos,valor in enumerate(datos):
        #     print(pos,valor)   
        # for clave,valor in docente.item():
        #     print(clave,valor,end="")
        
        # for notas in listaNotas:
        #     print("for externo",notas)
        #     for nota in notas:
        #         print(nota,end="")
        #     print("Saliendo del for interno")
        
        # print(listaNotas)    
        # for notas in listaNotas:
        #     acum=0
        #     for nota in notas:
        #         acum=acum+nota 
        #     print(nota,end="")
        #     print(acum/len(notas),end="") 
        print("\nDiccionario de alumnos")
        print(listaAlumnos)
        for alumnos in listaAlumnos.items():
            print(alumnos)
            for clave,valor in alumnos.items():
                print(clave,";",valor,end=" ")
            print()      
bucle = For()
bucle.usoFor()