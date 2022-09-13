import random
import time

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

puntaje = random.randint(0, 11)

iniciar_trivia = True
Intentos = 0


print (GREEN+"¡BIENVENID@ A LA TRIVIA LIBRERA!"+RESET)
print (YELLOW+"---------------------------------\n"+RESET)
time.sleep(2)

print (CYAN+"¡En esta trivia pondremos a prueba tus conocimientos sobre libros y lectura en general!")
time.sleep(2)
print ("\n¡Comenzaras con una cantidad de puntos al azar!") 
time.sleep(2)
print ("\nTrata de conseguir la mayor cantidad de puntos que puedas contestando correctamente las preguntas\n"+RESET)
time.sleep(2)
print (RED+"Tienes", puntaje, "puntos\n"+RESET)
time.sleep(2)

while iniciar_trivia == True:
  Intentos += 1
  puntaje = 0

  print("\nIntento número:", Intentos)
  input("Presiona Enter para continuar")
  
  nombre = input (GREEN+"\n¡Bienvenido! coloca aquí tu nombre: "+RESET)
  
  print (YELLOW+"\nHola", nombre, "! Responde las siguientes preguntas escribiendo la letra de la alternativa que creas correcta (a, b, c o d) y presionando 'Enter' para enviar tu respuesta:\n"+RESET)
  
  print (RED+"\n¡EMPECEMOS!\n"+RESET)
  time.sleep(2)
  
  print (BLUE+"¿Quién es el autor de la novela Los Miserables?"+RESET)
  time.sleep(2)
  print (MAGENTA+"a) Honore de Balzac")
  print ("b) Charles Baudelaire")
  print ("c) Victor Hugo")
  print ("d) Gustave Flaubert"+RESET)

  respuesta_1 = input(CYAN+"\nTu respuesta: "+RESET)
  
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_1 == "b":
    print (RED+"Incorrecto! ..."+RESET)
    puntaje = puntaje - 1
  elif respuesta_1 == "d":
    print (RED+"..."+RESET)
    puntaje = puntaje + 1
  elif respuesta_1 == "c":
    print (YELLOW+"¡Así es! Victor Hugo publicó la primera parte de los Miserables en 1862."+RESET)
    puntaje = puntaje + 5
  else:
    print (RED+"Totalmene incorrecto!"+RESET)
    puntaje = puntaje - 5
  
  
  print (BLUE+"\n¿Quién fue la primera mujer en ganar el premio nobel de literatura?"+RESET)
  time.sleep(2)
  print (MAGENTA+"a) Selma Lagerlöf")
  print ("b) Toni Morrison")
  print ("c) Gabriela Mistral")
  print ("d) Alice Munro"+RESET)
  
  respuesta_2 = input(CYAN+"\nTu respuesta: "+RESET)
  
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_2 == "a":
    print (YELLOW+"Muy bien! En efecto, Selma ganó el premio nobel de literatura en el año 1909, convirtiendose así en la primera mujer en conseguirlo."+RESET)
    puntaje = puntaje + 10
  elif respuesta_2 == "b":
    print (RED+"Incorrecto!"+RESET)
    puntaje = puntaje - 5
  elif respuesta_2 == "c":
    print (RED+"Cerca! Mistral fue la primera mujer latina en ganar el nobel, mas no la primera mujer en general ..."+RESET)
    puntaje = puntaje + 5
  else:
    print (RED+"Totalmente incorrecto! ..."+RESET)
    puntaje = puntaje - 10
  
  
  print (BLUE+"\n¿Cuál es el libro más costoso en el mundo?"+RESET)
  time.sleep(2)
  print (MAGENTA+"a) La Biblia de Gutenberg")
  print ("b) Codex Leicester de Leonardo da Vinci")
  print ("c) First Folio de William Shakespeare")
  print ("d) Evangelio de San Cuthbert de Lindisfarne"+RESET)
  
  respuesta_3 = input(CYAN+"\nTu respuesta: "+RESET)
  
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_3 == "a":
    print (RED+"Casi! La edición de Gutenberg de la sagrada Biblia cuesta 20 millones de dolares ..."+RESET)
    puntaje = puntaje + 5
  elif respuesta_3 == "c":
    print (RED+"Error! El Folio de Shakespeare se llego a vender por 10 millones de dolares"+RESET)
    puntaje = puntaje - 5
  elif respuesta_3 == "b":
    print (YELLOW+"Asi es! el CodeX Leicester, el libro donde Da vinci plasmo todas sus mas revolucionarias creaciones fue comprado por Bill Gates en 30 millones de dolares"+RESET)
    puntaje = puntaje * 2
  else:
    print (RED+"Totalmente incorrecto..."+RESET)
    puntaje = puntaje / 2
  
  print ("\n¡Eso es todo", nombre, "la trivia llegó a su fin, alcanzaste", puntaje, "puntos!")

  print(RED+"\n¿Te gustaría volver a intentar la trivia?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()

  if repetir_trivia != "si": 
   print(CYAN+"\nEspero que hayas podido aprender algo nuevo y la hayas pasado muy bien, nos vemos pronto!"+RESET)
   iniciar_trivia = False  