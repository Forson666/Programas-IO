import math # importo la biblioteca math para redondear numeros

# Defino la matriz de costos de cada componente
matrizCostos  = [[100,200,100,200],
                 [200,400,300,300],
                 [300,500,400,400]]

# Defino la matriz de probabilidades de exito de cada componente
# Donde las filas representan el numero de unidades de reserva y las columnas los componentes - 1
# Por ejemplo la probabilidad que el componente 2 funcione correctamente con 2 unidades de reserva
# es matrizProbabilidades[2][1] = 0.8
matrizProbabilidades = [[0.5,0.6,0.7,0.5],
                        [0.6,0.7,0.8,0.7],
                        [0.8,0.8,0.9,0.9]]

# Defino el numero de etapas del problema (decisiones)
n = 4

# Defino una lista para guardar los costos y decisiones optimas para cada etapa
lista = []

# Defino la funcion que halla (y guarda) de forma recursiva los costos y desiciones optimas
def valorOptimo(etapa, estado):
    if etapa == n - 1:
        # Si la etapa actual es la ultima, la probabilidad optima es simplemente 
        # La probabilidad de agregar todas las unidades posibles con un presupuesto $"estado"
            
        aux1 = [(matrizProbabilidades[x][etapa], etapa + 1, x+1, estado) for x in range(3) if matrizCostos[x][etapa] <= estado]
        
        # Guardo en la lista los valores optimos que no esten
        for x in aux1:
            if x not in lista:
                lista.append(x)
        
        # Retorno unicamente el valor optimo
        aux2 = [x[0] for x in aux1]
        if(aux2 != []):
            return max(aux2)
        else:
            return -1
        
    else:
        # El valor optimo para un estado en la etapa n es el valor maximo de la multiplicacion entre el costo inmediato
        # de tomar una decision x y el valorOptimo de esa decision x en la etapa n + 1(recursividad)
        
        # Guardo en una lista auxiliar los valores optimos de la etapa
        
        aux = [(matrizProbabilidades[x][etapa]*valorOptimo(etapa + 1, estado-matrizCostos[x][etapa]), etapa + 1, x+1, estado) for x in range(3) if matrizCostos[x][etapa] <= estado]
        
        # Guardo en la lista los valores optimos que no esten
        for x in aux:
            if x not in lista and x[0] > 0:
                lista.append(x)
        
        # Retorno el valor optimo para la etapa actual
        aux3 = [x[0] for x in aux]
        if(aux3 != []):
            return max(aux3)
        else:
            return -1

# Llamo a la funcion y guardo el valor de la ruta de desiciones que maximiza la probabilidad de exito
costooptimo = valorOptimo(0,1000)

# Defino una funcion para imprimir 1 camino optimo  de decision, teniendo un presupuesto num en el subsistema "etapa"
def camino(num, etapa):
    enunciado = "Una ruta de decision optima teniendo $" + str(num) + " cuando estoy escogiendo el numero de unidades paralelas"
    enunciado += " para el componente " + str(etapa) + " es:"
    print(enunciado)
    estado = num
    mensaje = "\t"
    while estado != 0:
        mensaje += "Para el componente " + str(etapa) + ":\n"
        aux0 = max([x[0] for x in lista if x[3] == estado and x[1] == etapa])
        aux = [x[2] for x in lista if x[3] == estado and x[0] == aux0 and x[1] == etapa]
        mensaje += "\t\t" + str(aux[0]) + " unidad(es) paralelas con un costo de $" + str(matrizCostos[aux[0] - 1][etapa-1])
        mensaje += " y una probabilidad de exito de " + str(matrizProbabilidades[aux[0]-1][etapa-1]) + "\n\t"
        estado -= matrizCostos[aux[0]-1][etapa-1]
        etapa += 1
    print(mensaje)

print("Si se dispone de $1000, obtenemos:")
print()

# Imprimo los datos importantes de cada etapa
for x in range(n):
    # Imprimo la etapa (para este caso el subsistema) en la que me encuentro
    print(f"componente {x + 1}")
    
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
                mensaje += "f(" + str(z[2]) + ") = " + str(round(z[0]*10000) / 10000) + " "
        w = max([z[0] for z in valoresDeEtapa if z[3] == y])
        
        # Imprimo el valor optimo del estado actual
        mensaje += "f*(" + str(y) + ") = " + str(round(w*10000) / 10000) + " x* = "
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
camino(1000, 1)

# Linea para que no se cierre al ejecutar en consola
input("Presione cualquier tecla para terminar...")
