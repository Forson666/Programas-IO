
# Defino la matriz de costos de cada unidad de reserva para cada subsistema
matrizCostos  = [100,300,200]

# Defino la matriz de probabilidades de exito de cada subsistema
# Donde las filas representan el numero de unidades de reserva y las columnas los subsistemas - 1
# Por ejemplo la probabilidad que el subsistema 2 funcione correctamente con 2 unidades de reserva
# es matrizProbabilidades[2][1] = 0.95
matrizProbabilidades = [[0.85,0.6,0.7],
                        [0.9,0.85,0.9],
                        [0.95,0.95,0.98]]

# Defino el numero de etapas del problema (decisiones)
n = 3

# Defino una lista para guardar los costos y decisiones optimas para cada etapa
lista = []

# Defino la funcion que halla (y guarda) de forma recursiva los costos y desiciones optimas
def valorOptimo(etapa, estado):
    if etapa == n - 1:
        # Si la etapa actual es la ultima, la probabilidad optima es simplemente 
        # La probabilidad de agregar todas las unidades posibles con un presupuesto $"estado"
        aux1 = [(matrizProbabilidades[x][etapa], etapa + 1, x, estado) for x in range(3) if x*matrizCostos[etapa] <= estado]
        
        # Guardo en la lista los valores optimos que no esten
        for x in aux1:
            if x not in lista:
                lista.append(x)
        
        # Retorno unicamente el valor optimo
        return max([x[0] for x in aux1])
    else:
        # El valor optimo para un estado en la etapa n es el valor maximo de la multiplicacion entre el costo inmediato
        # de tomar una decision x y el valorOptimo de esa decision x en la etapa n + 1(recursividad)
        
        # Guardo en una lista auxiliar los valores optimos de la etapa
        aux = [(matrizProbabilidades[x][etapa]*valorOptimo(etapa + 1, estado-(x*matrizCostos[etapa])), etapa + 1, x, estado) for x in range(3) if x*matrizCostos[etapa] <= estado]
        
        # Guardo en la lista los valores optimos que no esten
        for x in aux:
            if x not in lista:
                lista.append(x)
        
        # Retorno el valor optimo para la etapa actual
        return max([x[0] for x in aux])

# Llamo a la funcion y guardo el valor de la ruta de desiciones que maximiza la probabilidad de exito
costooptimo = valorOptimo(0,600)

# Defino una funcion para imprimir 1 camino optimo  de decision, teniendo un presupuesto num en el subsistema "etapa"
def camino(num, etapa):
    enunciado = "Una ruta de decision optima teniendo $" + str(num) + " cuando estoy escogiendo el numero de unidades de reserva"
    enunciado += " para el subsistema " + str(etapa) + " es:"
    print(enunciado)
    estado = num
    mensaje = "\t"
    while estado != 0:
        mensaje += "Para el subsistema " + str(etapa) + ":\n"
        aux0 = max([x[0] for x in lista if x[3] == estado and x[1] == etapa])
        aux = [x[2] for x in lista if x[3] == estado and x[0] == aux0 and x[1] == etapa]
        mensaje += "\t\t" + str(aux[0]) + " unidad(es) de reserva con un costo de $" + str(aux[0]*matrizCostos[etapa-1])
        mensaje += " y una probabilidad de exito de " + str(matrizProbabilidades[aux[0]][etapa-1]) + "\n\t"
        estado -= aux[0]*matrizCostos[etapa-1]
        etapa += 1
    print(mensaje)

print("Si se dispone de $600, obtenemos:")
print()

# Imprimo los datos importantes de cada etapa
for x in range(n):
    # Imprimo la etapa (para este caso el subsistema) en la que me encuentro
    print(f"subsistema {x + 1}")
    
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

# Imprimo la probabilidad optima de que el sistema funcione bien
print(f"Probabilidad optima = {costooptimo} ")
print()

# Imprimo una ruta de decision optima
camino(600, 1)

# Linea para que no se cierre al ejecutar en consola
input("Presione cualquier tecla para terminar...")
