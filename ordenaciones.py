class Ordenar:
    def __init__(self,lista):
        self.lista=lista
        
    def recorrerElemento(self):
        for ele in self.lista:
            print(ele)
    
    def recorrerPosicion(self):
        for pos, ele in enumerate(self.lista):
            print(pos,ele)
     
    def recorrerRange(self):
        for pos, ele in range((self.lista)):
            print(pos,self.lista[pos]) 
            
    def buscar(self,buscado): 
        emc = False 
        for pos, ele in enumerate(self.lista):
            if ele == buscado:
                enc=True 
                break
        if enc == True:
            return pos 
        else: return-1
        
    def ordenarAsc(self):
        for pos in range(0,len(self.lista)):
            for sig in range(pos +1,len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                 aux = self.lista[pos]
                 self.lista[pos]= self.lista[sig]
                 self.lista[sig]=aux
      
            
    def ordenarDes(self):
        for pos, ele in enumerate(self.lista):
            for sig in range(pos +1,len(self.lista)):
                
                
                if ele < self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]= aux

    def primer(self):
        return self.lista[0] 
    
    def primerEliminado(self):
        primer = self.lista[0]
        auxlista = []
        for pos in range(1,len(self.lista)):
            auxlista.append(self.lista[pos])
        self.lista=auxlista
        return primer
    
    def primerEliminado2(self):
        primer = self.lista[0]
        self.lista=self.lista[1:]
        return primer
    
    def ultimo(self):
        return self.lista[-1]
    
    def ultimoEliminado(self):
        primer = self.lista[-1]
        auxlista = []
        for pos in range(0,len(self.lista)-1):
            auxlista.append(self.lista[pos])
        self.lista=auxlista
        return primer
    
    def ultimoEliminado(self):
        ultimo = self.lista[-1]
        self.lista=self.lista[0:-1]
        return ultimo

    def insertar(self,num):
        self.ordenarAsc()
        auxlista=[]
        for pos, ele in enumerate(self.lista):
            if num < ele:
                auxlista.append(num)
                break
            
        self.lista=self.lista[0:pos]+auxlista+self.lista[pos:]
    
    def insertar2(self,num):
        self.ordenarAsc()
        auxlista=[]
        for pos, ele in enumerate(self.lista):
            if num < ele:
                break
        for i in range(pos):
            auxlista.append(self.lista[i])
        auxlista.append(num)
        for j in range(pos, len(self.lista)):
            auxlista.append(self.lista[j])  
        self.lista=auxlista    
           
        # self.lista=self.lista[0:pos]+auxlista+self.lista[pos:]
    
    def insertarOrden(self,num):      
        self.lista.append(num)
        self.ordenarAsc()
    
    def eliminar(self,num):
        enc=False
        for pos, ele in enumerate(self.lista):
            if num == ele:
                enc:True
                break                 
        if enc: self.lista=self.lista[0:pos]+self.lista[pos+1:]
        return enc
        
lista = [2,3,8,10] 
ord1= Ordenar(lista)
# print(ord1.primerEliminado())
# print(ord1.lista) 
if ord1.eliminar(5)== True : print("El numero se elimino de la lista",ord1.lista)       
else: print("El numero no se encuentra en la lista")

# print("Primer",ord1.primer())
# print("Segundo",ord1.primer())
# print("Normal", ord1.lista)
# ord1.ordenarAsc()
# print("Asc",ord1.lista)
# ord1.ordenarDes()
# print("Des",ord1.lista)               
# ord1.recorrerElemento()
# ord1.recorrerPosicion()          
# ord1.recorrerRange()
# print(ord1.buscar(3))
#buscado=9
#resp = ord1.buscar(buscado)
# if resp !=-1:
#     print("El Numero={} se encuentra en la Posicion:({} de la lista:{})",format(buscado,resp,ord1.lista))
# else:
#     print("El Numero={} no se encuentra en la lista:{}".format(buscado,ord1.lista))
lista = [2,4,8,5,10]

x= lista[2]
lista1 = lista[1:]
lista2 = lista[:-1]
for pos in range(len(lista)-1):
    print("Primer for",pos,lista[pos])
    for j in range(pos+1,len(lista)):
        print("Segundo for",j,lista[j])
    input("preiosione una tecla para continuar..")    