from collections import namedtuple


planeta = namedtuple('planeta',['nombre', 'numero'])

mercurio = planeta('Mercurio', 1)
venus = planeta('Venus', 2)
tierra = planeta('tierra', 3)
marte = planeta('Marte', 4)


print(mercurio.nombre)
print(mercurio.numero)
print(venus[0])
print(venus[1])

print("Campos de la dupla: {}",format(tierra._fields))
