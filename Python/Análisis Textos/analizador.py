# 
def Limpiador (texto):

  #Primero convertimos todo el texto a minúsculas
  texto_limpio= texto.lower()

  #Después eliminamos los signos de puntación comunes

  signos_eliminar= ['.', ',', ';', ':', '!', '?', '¡', '¿', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '/', '\\', '|', '@', '#', '$', '%', '^', '&', '*', '~', '`', '<', '>' ]
  for signo in signos_eliminar:
      texto_limpio= texto_limpio.replace(signo, '')

  # Finalmente, eliminamos los espacios adicionales

  palabras= texto_limpio.split()
  texto_limpio= ' '.join(palabras)

  return texto_limpio
