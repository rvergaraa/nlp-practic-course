import spacy

# Cargar modelo
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
    """
    contador = 0
    for token in doc:
        if not token.is_punct and not token.is_space:
            contador += 1
    return contador

resultado_1 = contar_tokens_reales(doc)
print(f"Ejercicio 1 - Tokens reales: {resultado_1}")


# --- Ejercicio 2: Extraer Sustantivos ---
def extraer_sustantivos(doc):
    """
    Devuelve una lista con todos los sustantivos (NOUN) del texto.
    """
    sustantivos = [token.text for token in doc if token.pos_ == "NOUN"]
    return sustantivos

resultado_2 = extraer_sustantivos(doc)
print(f"Ejercicio 2 - Sustantivos: {resultado_2}")


# --- Ejercicio 3: Extraer Verbos ---
def extraer_verbos(doc):
    """
    Devuelve una lista con los LEMAS de todos los verbos (VERB y AUX) del texto.
    """
    # Incluimos VERB (acciones) y AUX (verbos auxiliares como 'ser', 'estar', 'haber')
    verbos = [token.lemma_ for token in doc if token.pos_ in ["VERB", "AUX"]]
    return verbos

resultado_3 = extraer_verbos(doc)
print(f"Ejercicio 3 - Verbos (Lemas): {resultado_3}")


# --- Ejercicio 4: Pipeline de Limpieza Avanzado ---
def limpiar_texto_avanzado(texto):
    """
    1. Tokenizar el texto.
    2. Filtrar Stop Words.
    3. Filtrar Puntuación.
    4. Devolver una lista con los LEMAS de las palabras restantes en minúsculas.
    """
    doc_local = nlp(texto)
    tokens_limpios = [
        token.lemma_.lower() 
        for token in doc_local 
        if not token.is_stop and not token.is_punct and not token.is_space
    ]
    return tokens_limpios

resultado_4 = limpiar_texto_avanzado(texto_ejercicio)
print(f"Ejercicio 4 - Texto Limpio: {resultado_4}")
