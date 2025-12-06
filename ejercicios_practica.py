import spacy

# Cargar modelo (asegúrate de haberlo descargado: python -m spacy download es_core_news_sm)
try:
    nlp = spacy.load("es_core_news_sm")
except OSError:
    print("Error: Modelo no encontrado. Ejecuta: python -m spacy download es_core_news_sm")
    exit()

texto_ejercicio = """
El procesamiento de lenguaje natural (NLP) es una rama de la inteligencia artificial.
Ayuda a las computadoras a entender, interpretar y manipular el lenguaje humano.
¿Podrá la IA escribir novelas completas algún día?
"""

print(f"Texto original:\n{texto_ejercicio}\n")
doc = nlp(texto_ejercicio)

# --- Ejercicio 1: Contar Tokens Reales ---
def contar_tokens_reales(doc):
    """
    Cuenta cuántos tokens hay en el texto EXCLUYENDO puntuación y espacios en blanco.
    Pista: Usa las propiedades token.is_punct y token.is_space.
    """
    contador = 0
    # TODO: Tu código aquí
    # for token in doc:
    #     if ...:
    #         contador += 1
    return contador

print(f"Ejercicio 1 - Tokens reales: {contar_tokens_reales(doc)} (Esperado: ~30)")


# --- Ejercicio 2: Extraer Sustantivos ---
def extraer_sustantivos(doc):
    """
    Devuelve una lista con todos los sustantivos (NOUN) del texto.
    Pista: Usa token.pos_
    """
    sustantivos = []
    # TODO: Tu código aquí
    return sustantivos

print(f"Ejercicio 2 - Sustantivos: {extraer_sustantivos(doc)}")


# --- Ejercicio 3: Extraer Verbos ---
def extraer_verbos(doc):
    """
    Devuelve una lista con los LEMAS de todos los verbos (VERB y AUX) del texto.
    """
    verbos = []
    # TODO: Tu código aquí
    return verbos

print(f"Ejercicio 3 - Verbos (Lemas): {extraer_verbos(doc)}")


# --- Ejercicio 4: Pipeline de Limpieza Avanzado ---
def limpiar_texto_avanzado(texto):
    """
    1. Tokenizar el texto.
    2. Filtrar Stop Words.
    3. Filtrar Puntuación.
    4. Devolver una lista con los LEMAS de las palabras restantes en minúsculas.
    """
    doc_local = nlp(texto)
    tokens_limpios = []
    # TODO: Tu código aquí
    return tokens_limpios

print(f"Ejercicio 4 - Texto Limpio: {limpiar_texto_avanzado(texto_ejercicio)}")
