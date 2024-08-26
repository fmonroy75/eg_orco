from personaje import Personaje
import random


nombre = input("""
¡Bienvenido a Gran Fantasía!

Cual es tu nombre:                      
    """)

persona = Personaje(nombre)

print(persona.estado)

print("¡Alertaaaa!, ¡Ha aparecido un Orco!")

orco = Personaje("orco")

probabilidad_de_ganar = persona.mostrar_probabilidad(orco)
