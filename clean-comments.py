import os
import re
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Definir una función para limpiar los comentarios de películas
def limpiar_comentario(comentario):
    # Convertir a minúsculas
    comentario = comentario.lower()
    
    # Eliminar caracteres especiales y puntuaciones
    comentario = re.sub(r'\d+', '', comentario)
    comentario = comentario.translate(str.maketrans("", "", string.punctuation))
    
    # Tokenizar el comentario
    tokens = word_tokenize(comentario)
    
    # Eliminar stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if not word in stop_words]
    
    # Unir las palabras en una oración limpia
    comentario_limpio = ' '.join(tokens)
    
    return comentario_limpio

# Definir la ruta de la carpeta que contiene los archivos de comentarios
ruta_carpeta = os.getcwd() + '\\aclImdb\\test\\neg'

# Crear un archivo de salida para los comentarios limpios
ruta_archivo_salida = os.getcwd() + '\\exit\\test'
archivo_salida = open(ruta_archivo_salida, 'w', encoding='utf-8')

# Leer todos los archivos de la carpeta
for archivo in os.listdir(ruta_carpeta):
    # Comprobar que el archivo es un archivo de texto
    if archivo.endswith('.txt'):
        # Leer el contenido del archivo
        with open(os.path.join(ruta_carpeta, archivo), 'r', encoding='utf-8') as file:
            comentario = file.read()
        
        # Limpiar el comentario
        comentario_limpio = limpiar_comentario(comentario)
        
        # Escribir el comentario limpio en el archivo de salida
        archivo_salida.write(comentario_limpio + '\n')

# Cerrar el archivo de salida
archivo_salida.close()
