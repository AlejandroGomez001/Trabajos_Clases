class Condicion:
    
    def __init__(self,num1=5,num2=4):
        self.numero1=num1
        self.numero2=num2
        numero=self.numero1+self.numero2
        self.numero3=numero
        
    def usoIf(self):
        if self.numero1== self.numero2:
            print("numero1={}=numero2={}:son iguales".format(self.numero1,self.numero2))
        elif self.numero1 == self.numero3:
            print("numero1 y numero2 son iguales")
        else:
            print("numeros diferentes")
            print("fin if")

print("instancia de la clase")
cond1= Condicion(10,20)
cond2= Condicion()
print(cond2.numero3)
cond1.usoIf()
cond2.usoIf()
print("Gracias por su visita")