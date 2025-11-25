import analizador
from collections import Counter 

def main():
    print("--- 1. TEXTO ORIGINAL ---")
    print(texto_original)
    print("-" * 30)

    texto_procesado = analizador.limpiador(texto_original)

    frecuencia = Counter(texto_procesado.split())

    print("--- 2. TEXTO LIMPIO ---")
    print(f"'{texto_procesado}'") 
    print("-" * 30)

    print("--- 3. ESTADÍSTICAS ---")
    print(f"Total de palabras: {len(texto_procesado.split())}")
    print("Frecuencia de cada palabra:")

    for palabra, cantidad in frecuencia.items():
        print(f" - {palabra}: {cantidad}")

if __name__ == "__main__":
    main()
