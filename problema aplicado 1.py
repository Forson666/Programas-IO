
# Defino la matriz de costos o de la contribucion de cada decision
# En este caso la fila (posicion dentro de la lista) representa la propuesta
# a escoger y las columnas la planta en la que se da 
# el valor de las casillas es una tupla en donde el primer elemento indica el
# costo de la propuesta y el segundo el beneficio
matrizCostos  = [ [(0,0),(0,0),(0,0)],
                  [(1,5),(2,8),(1,4)],
                  [(2,6),(3,9),(-1,-1)],
                  [(-1,-1),(4,12),(-1,-1)]]


# Defino el numero de etapas
n = 3

# Defino una lista para guardar los costos y decisiones optimas para cada etapa
lista = []

# Defino la funcion que halla (y guarda) de forma recursiva los costos y desiciones optimas
def valorOptimo(etapa, estado):
    if etapa == 0:
        # Si la etapa actual es la ultima, el beneficio optimo es simplemente
        #el beneficio maximo con el dinero actual
        aux0 = [(matrizCostos[i][etapa][1],1,i+1,estado) for i in range(len(matrizCostos)) if matrizCostos[i][etapa][0] != -1 and matrizCostos[i][etapa][0] <= estado]
        aux1 = aux0[len(aux0)-1]
        # Si el valor optimo no esta en la lista ==> lo agrego
        if aux1 not in lista:
            lista.append(aux1)
        
        # Retorno unicamente el valor optimo
        return aux1[0]
    else:
        # El costo optimo para un estado en la etapa n es el valor maximo de la suma entre el costo inmediato
        # de tomar una decision x y el valorOptimo de esa decision x en la etapa n - 1(recursividad)
        aux = [(matrizCostos[i][etapa][1] + valorOptimo(etapa - 1, estado-matrizCostos[i][etapa][0]), etapa + 1, i+1,estado) for i in range(len(matrizCostos)) if matrizCostos[i][etapa][0] != -1 and matrizCostos[i][etapa][0] <= estado]
        
        # Guardo en la lista los valores optimos que no esten
        for x in aux:
            if x not in lista:
                lista.append(x)
        
        # Retorno el costo optimo para el estado actual
        return max([x[0] for x in aux])

# Llamo a la funcion y guardo el valor de la ruta de desiciones que maximiza la eficiencia
costooptimo = valorOptimo(2,5)

# Defino una funcion para imprimir 1 camino optimo  de decision, teniendo un presupuesto num para la planta "etapa"
def camino(num, etapa):
    print(f"Una ruta de decision optima teniendo ${num} millones cuando estoy escogiendo una propuesta de la planta {etapa} es:")
    estado = num
    mensaje = "\t"
    while estado != 0:
        mensaje += "Para la planta " + str(etapa) + ":\n"
        aux0 = max([x[0] for x in lista if x[3] == estado and x[1] == etapa])
        aux = [x[2] for x in lista if x[3] == estado and x[0] == aux0 and x[1] == etapa]
        mensaje += "\t\tpropuesta " + str(aux[0]) + " con un costo de $" + str(matrizCostos[aux[0]-1][etapa-1][0])
        mensaje += " y un beneficio de $" + str(matrizCostos[aux[0]-1][etapa-1][1]) + " millones\n\t"
        estado -= matrizCostos[aux[0]-1][etapa-1][0] 
        etapa -= 1
    print(mensaje)


# Imprimo los datos importantes de cada etapa
for x in range(n):
    # Imprimo la etapa (para este caso la planta) en la que me encuentro
    print(f"Planta {x + 1}")
    
    # Guardo en una variable auxiliar los valores optimos de la etapa
    valoresDeEtapa = [y for y in lista if y[1] == x + 1]
    
    # Guardo los posibles estados iniciales de cada etapa
    estadosIniciales = set([y[3] for y in valoresDeEtapa])
    
    for y in estadosIniciales:
        # Para cada estado inical
        mensaje = "\tCon " + str(y) + ": "
        for z in valoresDeEtapa:
            if z[3] == y:
                # Imprimo el valor optimo de cada decision posible 
                mensaje += "f(" + str(z[2]) + ") = " + str(z[0]) + " "
        w = max([z[0] for z in valoresDeEtapa if z[3] == y])
        
        # Imprimo el valor optimo del estado actual
        mensaje += "f*(" + str(y) + ") = " + str(w) + " x* = "
        for z in valoresDeEtapa:
            if z[3] == y and z[0] == w:
                # Imprimo las decisiones que me dan el valor optimo
                mensaje += str(z[2]) + ","
        mensaje = mensaje[:-1]
        print(mensaje)
print()
# Imprimo el beneficio optimo de las decisiones del problema
print(f"Beneficio optimo = {costooptimo} ")
print()

# Imprimo una ruta de decision optima
camino(5, 3)

# Linea para que no se cierre al ejecutar en consola
input("Presione cualquier tecla para terminar...")
