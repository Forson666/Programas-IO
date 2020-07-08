from fractions import Fraction # importo la libreria fractions para expresar decimales commo fracciones

# Defino la probabilidad de exito
pExito = 2/3

# Defino la probabilidad de fracaso
pFracaso = 1/3

# Defino el numero de etapas del problema (decisiones)
n = 3

# Defino una lista para guardar los costos y decisiones optimas para cada etapa
lista = []

# Defino la funcion que halla (y guarda) de forma recursiva los costos (probabilidades) y desiciones optimas
def valorOptimo(etapa, estado):
    if etapa == n + 1:
        # Si la etapa actual es la ultima, la probabilidad es 0 si estado (numero de fichas) < 5 y 1 si el estado >= 5
        if estado < 5:
            return 0
        else:
            return 1
    else:
        # La probabilidad optima para un estado en la etapa n es el valor maximo de la suma entre la probabilidad de fracaso
        # al tomar una decision x por el valorOptimo teniendo estado-x a partir de ese punto y  la probabilidad de exito
        # al tomar es misma decision x por el valorOptimo teniendo estado + x fichas a partir de ese punto
        aux = [(pFracaso*valorOptimo(etapa + 1, estado-x) + pExito*valorOptimo(etapa + 1, estado+x), etapa, x,estado) for x in range(estado+1)]
        
        # Guardo en la lista los valores optimos que no esten
        for x in aux:
            if x not in lista:
                lista.append(x)
        
        # Retorno el costo optimo para el estado actual
        return max([x[0] for x in aux])

# Llamo a la funcion y guardo la probabilidad maxima
pOptima = valorOptimo(1,3)

# Imprimo los datos importantes de cada etapa
for x in range(1,n+1):
    # Imprimo la etapa en la que me encuentro
    print(f"Jugada {x}")
    
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
        w = max([z[0] for z in valoresDeEtapa if z[3] == y])
        
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
print(f"Probabilidad maxima de la politica optima = {Fraction(pOptima).limit_denominator()} ")
print()

# Linea para que no se cierre al ejecutar en consola
input("Presione cualquier tecla para terminar...")