
import spacy

def main():
    print("--- Configuración Inicial ---")
    # 1. Cargar el modelo
    try:
        nlp = spacy.load("es_core_news_sm")
        print("Modelo 'es_core_news_sm' cargado correctamente.")
    except OSError:
        print("Error: No se encontró el modelo. Ejecuta: python -m spacy download es_core_news_sm")
        return

    texto_ejemplo = "Los gatos están corriendo rápidamente por el jardín del vecino."
    print(f"\nTexto de ejemplo: '{texto_ejemplo}'")

    doc = nlp(texto_ejemplo)

    print("\n--- 1. Tokenización ---")
    print("La tokenización divide el texto en unidades individuales.")
    tokens = [token.text for token in doc]
    print(f"Tokens: {tokens}")

    print("\n--- 2. Lematización ---")
    print("La lematización reduce las palabras a su forma base (lema).")
    for token in doc:
        print(f"Token: {token.text:<12} -> Lema: {token.lemma_}")

    print("\n--- 3. POS Tagging (Etiquetado Gramatical) ---")
    print("Identifica la categoría gramatical de cada palabra.")
    for token in doc:
        print(f"Token: {token.text:<12} -> POS: {token.pos_:<6} ({spacy.explain(token.pos_)})")

    print("\n--- 4. Stop Words (Palabras Vacías) ---")
    print("Palabras comunes que a menudo se filtran.")
    # Obtener lista de stop words del modelo
    stop_words_list = nlp.Defaults.stop_words
    print(f"Ejemplo de stop words en español: {list(stop_words_list)[:5]}...")
    
    tokens_filtrados = [token.text for token in doc if not token.is_stop]
    print(f"Texto sin stop words: {tokens_filtrados}")

    print("\n--- 5. Ejercicio Combinado ---")
    print("Función que limpia texto: tokeniza, elimina stop words/puntuación y lematiza.")
    
    def limpiar_texto(texto):
        doc = nlp(texto)
        tokens_limpios = [
            token.lemma_.lower() 
            for token in doc 
            if not token.is_stop and not token.is_punct
        ]
        return tokens_limpios

    resultado = limpiar_texto(texto_ejemplo)
    print(f"Original: {texto_ejemplo}")
    print(f"Procesado: {resultado}")

if __name__ == "__main__":
    main()
