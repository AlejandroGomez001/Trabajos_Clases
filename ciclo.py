class Ciclo:
    def __init__(self,numero=5):
        self.numero=numero
        self.numero2=0
        
    def usoWhile(self):
        car = input("ingrese vocal")
        car = car.lower()
        while car not in('a','e','i','o','u'):
            car1 = input("ingrese vocal").lower()
        print("Felicitacion su vocal es:{}".format(car))
    
ciclo1 = Ciclo()
ciclo1.usoWhile()
print("fin de uso ciclo")