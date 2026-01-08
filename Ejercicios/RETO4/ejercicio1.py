notas=[10, 9.8, 9.5, 4, 8]

posiciones=[0,1,2,3,4]
#a todos los que tengan una nota mayor o igual a 9.5, les va a poner 10
for nota in notas:
    print(nota)
    if nota>=9.5:
        nota=10

for indice in [0,1,2,3,4]:
    nota=notas[indice]
    print(nota)
    if nota>=9.5:
        notas[indice]=10

tamanio=len(notas)
for indice in range(tamanio):
    nota=notas[indice]
    print(nota)
    if nota>=9.5:
        notas[indice]=10

print(notas)
