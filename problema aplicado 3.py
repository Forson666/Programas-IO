from fractions import Fraction # importo la libreria fractions para expresar decimales commo fracciones

# Defino el numero de etapas del problema (decisiones)
n = 3

# Defino una lista para guardar los costos y decisiones optimas para cada etapa
lista = []

# Defino la funcion del costo de inicio de produccion
def K(x):
    if(x == 0):
        return 0
    else:
        return 3

# Defino la funcion que halla (y guarda) de forma recursiva los costos (probabilidades) y desiciones optimas
def valorOptimo(etapa, estado):
    if etapa == n + 1:
        # Si la etapa actual es la ultima, el valor es 0 si estado (numero de productos por obtener) = 0 y 16 si el estado == 1
        if estado == 0:
            return 0
        else:
            return 16
    else:
        # EL valor optimo para un estado en la etapa n es el valor minimo de la suma del costo de empezar la produccion
        # mas el costo de los productos mas la probabilidad de fracaso por el valor optimo de la siguiente etapa
        aux = [(K(0) + 0 + ((1/2)**0)*valorOptimo(etapa + 1, 1), etapa, 0,estado)]
        x = 1
        while True:
            aux.append((K(x) + x + ((1/2)**x)*valorOptimo(etapa + 1, 1), etapa, x,estado))
            if aux[len(aux) - 1][0] > aux[len(aux) - 2][0] and x >= 3:
                break
            else:
                x += 1
        
        # Guardo en la lista los valores optimos que no esten
        for x in aux:
            if x not in lista:
                lista.append(x)
        
        # Retorno el costo optimo para el estado actual
        return min([x[0] for x in aux])

# Llamo a la funcion y guardo la probabilidad maxima
pOptima = valorOptimo(1,1)

# Imprimo los datos importantes de cada etapa
for x in range(1,n+1):
    # Imprimo la etapa en la que me encuentro
    print(f"n = {x}")
    
    # Guardo en una variable auxiliar los valores optimos de la etapa
    valoresDeEtapa = [y for y in lista if y[1] == x]
    
    # Guardo los posibles estados iniciales de cada etapa
    estadosIniciales = set([y[3] for y in valoresDeEtapa])
    
    for y in estadosIniciales:
        # Para cada estado inical
        mensaje = "\tCon " + str(y) + ": "
        for z in valoresDeEtapa:
            if z[3] == y:
                # Imprimo el valor optimo de cada decision posible 
                mensaje += "f(" + str(z[2]) + ") = " + str(Fraction(z[0]).limit_denominator()) + " "
        w = min([z[0] for z in valoresDeEtapa if z[3] == y])
        
        # Imprimo el valor optimo del estado actual
        mensaje += "f*(" + str(y) + ") = " + str(Fraction(w).limit_denominator()) + " x* = "
        for z in valoresDeEtapa:
            if z[3] == y and z[0] == w:
                # Imprimo las decisiones que me dan el valor optimo
                mensaje += str(z[2]) + ","
        mensaje = mensaje[:-1]
        print(mensaje)

print()
# Imprimo la probabilidad optima de las decisiones del problema
print(f"costo de la politica optima = {Fraction(pOptima).limit_denominator() * 100} ")
print()

# Linea para que no se cierre al ejecutar en consola
input("Presione cualquier tecla para terminar...")
