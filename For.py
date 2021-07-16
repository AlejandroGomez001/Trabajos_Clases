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
        listaNotas = [(30,40),(20,40,50),(50,40)]
        listaAlumnos = [{"nombre":"Erick","final":70}],{"nombre":"Maria","final":60}
        
        
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
        # listaAlumnos=[{"mombre":"Jose","final":60},{"mombre":"Erick","final":70},{"nombre":"Maria","final":60},{"nombre":"Danny","final":90}] 
        # print("\nDiccionario de alumnos")
        # print(listaAlumnos)
        # acum=0
        
        # for alumnos in listaAlumnos.items():
        #     print(alumnos,len(alumnos))
            
        #     for clave,valor in alumnos.items():
        #         print(clave,";",valor,end=" ")
        #         if clave == 'final':
        #             acum=acum-valor
                    
        #     print()   
        # print("Promedio",acum/len(listaAlumnos))   
        listaNotas = [(30,40,10,20),(20,40,50),(50,40,10),(10,20)]
        acum,cont=0,0
        for notas in listaNotas:
            print(notas)
            acumparcial=0
            for nota in notas:
                acumparcial +=nota
            cont=cont+len(notas)
            acum=acum+acumparcial
            print("TotalParcial:{} PromParcial:{}".format(acumparcial,acumparcial/len(notas)))
        print("TotalParcial:{} PromParcial:{}".format(acum,acum/cont))
        print(acum/cont)
            
bucle = For()
bucle.usoFor()