
# Defino la matriz de costos o de la contribucion de cada decision
# En este caso la fila (posicion dentro de la lista) representa el numero de brigadas
# a asignar y las columnas el pais al que se asignaran las brigadas
# el valor de las casillas es el indicador de eficiencia que se obtiene al asignar
# "fila" brigadas al pais "columna + 1"
matrizCostos  = [ [0,0,0],
				  [45,20,50],
				  [70,45,70],
				  [90,75,80],
				  [105,110,100],
				  [120,150,130]]


# Defino el numero de etapas del problema (decisiones)
n = 3

# Defino una lista para guardar los costos y decisiones optimas para cada etapa
lista = []

# Defino la funcion que halla (y guarda) de forma recursiva los costos y desiciones optimas
def valorOptimo(etapa, estado):
    if etapa == n - 1:
        # Si la etapa actual es la ultima, el costo optimo es simplemente el costo entre el
        # estado actual y el estado final
        aux1 = (matrizCostos[estado][etapa], n, estado,estado)
        # Si el valor optimo no esta en la lista ==> lo agrego
        if aux1 not in lista:
            lista.append(aux1)
        
        # Retorno unicamente el valor optimo
        return matrizCostos[estado][etapa]
    else:
        # El costo optimo para un estado en la etapa n es el valor maximo de la suma entre el costo inmediato
        # de tomar una decision x y el valorOptimo de esa decision x en la etapa n + 1(recursividad)
        aux = [(matrizCostos[x][etapa] + valorOptimo(etapa + 1, estado-x), etapa + 1, x,estado) for x in range(estado+1)]
        
        # Guardo en la lista los valores optimos que no esten
        for x in aux:
            if x not in lista:
                lista.append(x)
        
        # Retorno el costo optimo para el estado actual
        return max([x[0] for x in aux])

# Llamo a la funcion y guardo el valor de la ruta de desiciones que maximiza la eficiencia
costooptimo = valorOptimo(0,5)

# Defino una funcion para imprimir 1 camino optimo  de decision, teniendo un num de brigadas en una etapa
def camino(num, etapa):
    print(f"Una ruta de decision optima teniendo {num} brigadas cuando estoy asignando al pais {etapa} es:")
    estado = num
    pais = etapa
    mensaje = "\t"
    while estado != 0:
        mensaje += "Para el pais " + str(etapa) + ":\n"
        aux0 = max([x[0] for x in lista if x[3] == estado and x[1] == etapa])
        aux = [x[2] for x in lista if x[3] == estado and x[0] == aux0 and x[1] == etapa]
        mensaje += "\t" + str(aux[0]) + "\n\t"
        estado -= aux[0]
        etapa += 1
    print(mensaje)


# Imprimo los datos importantes de cada etapa
for x in range(n):
    # Imprimo la etapa (para este caso el pais) en la que me encuentro
    print(f"Pais {x + 1}")
    
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
# Imprimo el costo optimo de las decisiones del problema
print(f"Costo optimo = {costooptimo} ")
print()
# Imprimo una ruta de decision optima
camino(5, 1)

# Linea para que no se cierre al ejecutar en consola
input("Presione cualquier tecla para terminar...")