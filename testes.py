def separacao_cartas(inventario):
    curingas_base = ['Joker', 'Space Joker', 'Blueprint', 'Chicot']   
    arcanos_base = ['Tolo', 'Hierofante', 'Justiça', 'Força']
    
    curingas_presentes = []
    arcanos_presentes = []
    for item in inventario:
        if item in curingas_base:
            curingas_presentes.append(item)
        elif item in arcanos_base:
            arcanos_presentes.append(item)

    return curingas_presentes, arcanos_presentes

lista_cartas = ['Blueprint', 'Joker', 'Space Joker', 'Tolo', 'Força']
curingas, arcanos = separacao_cartas(lista_cartas)

lista_de_curingas = ", ".join(curingas)
lista_de_arcanos = ", ".join(arcanos)
print(f"Curingas: {lista_de_curingas}")
print(f"Arcanos: {lista_de_arcanos}")
