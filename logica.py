class Ejercicios:
    def __init__(self):
        pass
    
    def parImpar(self,numero):
        if numero % 2 == 0:
            print("{} es Par".format(numero))
        else:
            print("{} es Impar",format(numero))
    
    def perfecto(self, numero):
        acu=0
        for i in range % 1 == 0:
            acu=acu+i
        if numero == acu:
            print("[] es Perfecto".format(numero))
        else:
            print("[] ni es Perfecto",format(numero))
    
    def perfecto2(self, numero):
        acu=0
        for i in range % 1 == 0:
            acu=acu+i
        return acu
                    
ejer = Ejercicios()
# num = int(input("Ingrese un numero: "))
# print("llamada 1")
# resp = ejer.perfecto2(num)
# if num == resp:
#     print("{} es Perfecto".format(num))
# else:
#     print("{} no es Perfecto".format(num))
# input()
lista = [3,5,6,8,28]
print("Llamada 2")
perfectos= []
for num in lista:
  if ejer.perfecto(num) == num:
      perfectos.append(num)
print(perfectos)
# input()
# print("Llamada 3")
# ejer.parImpar(23)