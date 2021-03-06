import random

#Colección de individuos
individuos={}  

#Para calcular la distancia entre dos números
def distancia(num1,num2):   
        d=num1-num2
        return abs(d) 

 #Generamos la poblacion inicial. cada individuo se le asocia un número aleatorio entre el rango ingresado 
def poblacionInicial():  
	for individuo in range(numIndividuos): 
		individuos[individuo]=random.uniform(limiteInferior, limiteSuperior)  

#Seleccionamos el individuo donde el número mas se acerco al objetivo y muestra los datos del individuo escogido 
def seleccion():  
        global numeroSeleccionado
        numeroSeleccionado=0
        individuoSeleccionado=0  
        distanciaMinima=1000000000000000000000000
        for individuo in individuos: 
                dis=distancia(individuos[individuo], numeroObjetivo) 
                if dis<distanciaMinima:
                        distanciaMinima=dis
                        individuoSeleccionado=individuo
                        numeroSeleccionado=individuos[individuo] 
        print("Individuo:", individuoSeleccionado, "Número del individuo:", individuos[individuoSeleccionado], "Distancia:", distanciaMinima)

#A cada uno de los individuos se le asigna un número aleatorio nuevo y en este caso va a estar oscilando cerca del número seleccionado
#la magnitud de la oscilacion la determina el usuario   
def mutacion():  
        for individuo in individuos: 
                if not individuo==0: 
                	individuos[individuo]=random.uniform(numeroSeleccionado-rangoMutacion,numeroSeleccionado+rangoMutacion)
                else:
                	individuos[individuo]=numeroSeleccionado
  
 
#Se solicitan las variables 
numIndividuos=int(input("Por favor ingrese la cantidad de individuos por generación: "))
iteraciones=int(input("Por favor ingrese el número de iteraciones: "))
numeroObjetivo=float(input("Por favor ingrese el numero objetivo: "))
rangoMutacion=float(input("Por favor ingrese el rango de mutacion: "))
limiteInferior=float(input("Por favor ingrese el límite inferior donde oscilaran los valores iniciales de cada individuo: "))
limiteSuperior=float(input("Por favor ingrese el límite superios donde oscilaran los valores iniciales de cada individuo: "))
 
#Generar la poblacion inicial, Iterar y ejecuta las funciones 
poblacionInicial() 
for generacion in range(iteraciones):
        print("Iteración", generacion)
        seleccion()
        if numeroSeleccionado==numeroObjetivo: #revisa si se alcanzo el numero objetivo. Si es asi lo avisa y rompe el bucle.
                print("Se alcanzo el número objetivo")
                break 
        mutacion()
 
print("Resultado:", numeroSeleccionado)
