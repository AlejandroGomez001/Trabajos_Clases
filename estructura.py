from typing import MutableSequence


num=28
nombre="ana"
print(num,type(num))
print(nombre,type(nombre))

def mensaje(msg):
    print(msg)
      
mensaje("Mi primer programa en Python") 
mensaje("Mi segundo programa en Python") 

class Sintaxis:
    instancia=0
    
    
    def __init__(self,dato="llamando al constructor2"):
        self.frase=dato
        Sintaxis.instancia = Sintaxis.instancia+1
    def usoVariable(self):
        edad,-peso=50,70.5 
        nombres= 'Alejandro Gomez'
        Tipo_sexo = 'M'
        civil = True
        usuario=('eisonale','1234','eisonale@gmail.com')
        # usuario[0] = "Alejandro"
        # print(usuario[2],nombre[7])
        # listas=[] 
        materias=[]
        materias=['Progamacion web', 'PHD','POO']
        aux=materias[1]
        materias[1]="Python"
        materias.append("Go")
        # print(materias,aux,materias[1])
        #  diccionario = {} colecciones de objeto clave:valor tipo json
        docente = {}
        docente = {'nombre': 'Alejandro', 'edad': 50, 'activo': True}
        edad = docente ['edad']
        docente['edad']=51
        docente['carrera']='IS'
        print(docente,edad,docente['edad'])
        # print(usuario,usuario[0],usuario[0:2],usuario[-1])
        # print(nombres,nombres[0],nombres[0:2],nombres[-1])
        print(materias,materias[0],materias[0:2],materias[-1])
      
    # # presentacion con format
    # print(""Mi nombre es {}, tengo {}
    #        años "".format(nombres,edad))
# print("Sintaxis antes de instancia es:{}".format(Sintaxis.instancia))    
ejer1 = Sintaxis()  #Instania la clase sintaxis y crea el objeto ejer1(copia de la clase)
# print("Sintaxis de ejer1 es:{}".format(Sintaxis.instancia))
# ejer2 = Sintaxis()
# print(ejer1.frase) 
# print("Sintanxis de ejer2 es :{}".formt(Sintaxis.instancia))
# print("Sintaxis nuevamente de ejer1 es: {}".format(Sintaxis.instancia))
# print(ejer2.frase)