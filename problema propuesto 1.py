
# Defino los nombres o identificadores de los estados
identificadores = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V"]

# Defino la matriz de costos o de la contribucion de cada decision
# Si el costo es -1 nos indica que los estados no estan conectados
# O en el caso del problema de la diligencia el -1 en la posicion [0][0] nos indica 
# que no se puede ir de el estado A hacia A 
matrizCostos  = [[-1,-1,20,15,30,50,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,12,16,41,35,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,13,11,10,21,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,22,10,15,5,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,14,11,12,13,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,21,18,9,30,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,8,7,12,10,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,6,14,13,7,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,12,21,8,4,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,12,11,13,12,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,18,10,11,13,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,9,15,8,21,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,14,12,7,8,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,12,10,15,11,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,4,7,12,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,8,3,9,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,9,15,12,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,8,6,13,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,8],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,7],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
                 
# Defino el estado del que parto (la posicion en la matriz de costos)
inicio = 0
inicio1 = 1

# Defino el estado al que quiero llegar (la posicion en la matriz de costos)
fin = 21

# Defino el numero de etapas del problema (decisiones)
n = 6

# Defino una lista para guardar los costos y decisiones optimas para cada etapa
lista = []

# Defino la funcion que halla (y guarda) de forma recursiva los costos y desiciones optimas
def valorOptimo(etapa, estado):
    if etapa == n:
        # Si la etapa actual es la ultima, el costo optimo es simplemente el costo entre el
        # estado actual y el estado final
        aux1 = (matrizCostos[estado][fin],identificadores[fin], n, identificadores[estado])
        # Si el valor optimo no esta en la lista ==> lo agrego
        if aux1 not in lista:
            lista.append(aux1)
        
        # Retorno unicamente el valor optimo
        return matrizCostos[estado][fin]
    else:
        # El costo optimo para un estado en la etapa n es el valor minimo de la suma entre el costo inmediato
        # de tomar una decision x y el valorOptimo de esa decision x en la etapa n + 1(recursividad)
        aux = [(matrizCostos[estado][x] + valorOptimo(etapa + 1, x), identificadores[x], etapa,
                identificadores[estado]) for x in range(fin +  1) if matrizCostos[estado][x] != -1]
        
        # Guardo en la lista los valores optimos que no esten
        for x in aux:
            if x not in lista:
                lista.append(x)
        
        # Retorno el costo optimo para el estado actual
        return min([x[0] for x in aux])

# Llamo a la funcion y guardo el valor de la ruta mas corta
costooptimo1 = valorOptimo(1,inicio1)
costooptimo = valorOptimo(1,inicio)


# Defino una funcion para imprimir 1 camino optimo desde un estado inicial a uno final
def camino(inicial, final):
    print(f"Una ruta de decision optima entre {identificadores[inicial]} y {identificadores[final]} es:")
    estado = inicial
    mensaje = "\t"
    while estado != final:
        mensaje += identificadores[estado]
        aux0 = min([x[0] for x in lista if x[3] == identificadores[estado]])
        aux = [x[1] for x in lista if x[3] == identificadores[estado] and x[0] == aux0]
        estado = identificadores.index(aux[0])
        mensaje += "->"
    mensaje += identificadores[final]
    print(mensaje)

# Imprimo los datos importantes de cada etapa
for x in range(n):
    # Imprimo la etapa en la que me encuentro
    print(f"Etapa {x + 1}")
    
    # Guardo en una variable auxiliar los valores optimos de la etapa
    valoresDeEtapa = [y for y in lista if y[2] == x + 1]
    
    # Guardo los posibles estados iniciales de cada etapa
    estadosIniciales = set([y[3] for y in valoresDeEtapa])
    
    for y in estadosIniciales:
        # Para cada estado inical
        mensaje = "\tpara " + y + ": "
        for z in valoresDeEtapa:
            if z[3] == y:
                # Imprimo el valor optimo de cada decision posible 
                mensaje += "f(" + z[1] + ") = " + str(z[0]) + " "
        w = min([z[0] for z in valoresDeEtapa if z[3] == y])
        
        # Imprimo el valor optimo del estado actual
        mensaje += "f*(" + y + ") = " + str(w) + " x* = "
        for z in valoresDeEtapa:
            if z[3] == y and z[0] == w:
                # Imprimo las decisiones que me dan el valor optimo
                mensaje += z[1] + ","
        mensaje = mensaje[:-1]
        print(mensaje)
print()
# Imprimo el costo optimo de las decisiones del problema
print(f"Con un costo optimo de = {costooptimo} ")
print()
# Imprimo una ruta de decision optima
camino(inicio, fin)
print()
# Imprimo el costo optimo de las decisiones del problema
print(f"Con un costo optimo de = {costooptimo1} ")
print()
# Imprimo una ruta de decision optima
camino(inicio1, fin)

# Linea para que no se cierre al ejecutar en consola
input("Presione cualquier tecla para terminar...")
