notas=[8.5, 8.5, 9, 10]

total=0

for nota in notas:
    total=total+nota

print(f"Promedio: {total/len(notas)}")