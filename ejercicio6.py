# como definimos un objeto ? => es instanciar a una clase que implementa todo eso (tienen propiedades) en Python
#EXISTEN CLASES DINAMICAS Y ESTATICAS

# class Dino : 
#     encendido = True #PROPIEDAD
    
#     def encender (self):   #METODOS (funciones)
#         pass     

# d = Dino()
# print(d.encendido)

# CUANDO INSTANCIAMOS UNA CLASE. UTILIZAMOS UN CONSTRUCTOR , UTILIZANDO FUNCION RESERVADA INIT
#                                 PUEDE EXISTIR UN DESTRUCTOR, FUNCION RESERVADA DEL

class Dino : 
    def __init__(self,nombre) :
        print("Estoy en el constructor" , nombre)
    
    def encender (self):   #METODOS (funciones)
        pass     

d = Dino("ale")


# EXISTEN CLASES ABSTRACTAS Y NO ABSTRACTAS

#RELACIONES IS A  => HERENCIA
#RELACIONES HAS A => "CONTIENE" COMPOSICION  "CLASES COMPUESTAS"

############################################# 

#EJERCICIO 1

#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

  # Color

  # Ruedas

  # Puertas

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

  # Velocidad

  #Cilindrada

# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

#EJERCICIO 2

# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
# Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

