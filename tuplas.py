usuario = ('eisonale','1234','eisonale@gmail.com')
materias = ['Python','PHP','POO’,’Go']
docente = {'nombre':'Eison','edad':19,'fac':'faci'}
print(usuario[0],materias[1],docente['nombre'])
print(usuario[0:2],docente.keys(),docente.values())
materias.append('Programacion Movil')
docente['sexo'], docente['edad']='M', 19
print(materias,docente)
tupla,lista,diccionario=(),[],{}
for valor in usuario: print(valor)
for i, c in enumerate(materias): print(i,':',c)
for c, v in docente.items(): print(c,':',v)