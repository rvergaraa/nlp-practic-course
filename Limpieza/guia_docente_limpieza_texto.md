# Guía Docente: Importancia de la Limpieza de Texto en NLP

**Archivo del Notebook:** `clase_limpieza_texto.ipynb`
**Duración Estimada:** 45 - 60 minutos
**Requisitos Técnicos:** Python local o Google Colab (CPU es suficiente)

---

## 🎯 Objetivos de Aprendizaje
Al finalizar la clase, los estudiantes serán capaces de:
1.  **Identificar** los tipos comunes de "ruido" en datos textuales (HTML, stop words, caracteres especiales).
2.  **Aplicar** técnicas de normalización (lowercasing, eliminación de acentos) y limpieza usando `regex` y `spaCy`.
3.  **Comparar** el impacto del preprocesamiento en el tamaño del vocabulario y la calidad de las features.
4.  **Entender** la diferencia práctica entre Stemming y Lemmatization.

---

## ⏱️ Cronograma de la Clase (Minuto a Minuto)

| Tiempo | Sección | Descripción y Puntos Clave |
| :--- | :--- | :--- |
| **00-10** | **1. El Problema del Texto "Sucio"** | - **Contexto**: Mostrar un tweet o comentario real con emojis, errores y hashtags.<br>- **Discusión**: ¿Por qué es difícil para una máquina entender "HOLA!!!" vs "hola"?<br>- **Concepto**: La maldición de la dimensionalidad (Vocabulario inflado). |
| **10-25** | **2. La Caja de Herramientas** | - **Regex**: Patrones básicos para eliminar URLs y emails.<br>- **Normalización**: `unicodedata` para quitar tildes.<br>- **Stop Words**: Discutir cuándo quitarlas y cuándo no (ej. "No me gusta" -> quitando "no" queda "gusta"). |
| **25-40** | **3. Demo: El Impacto Real** | - Usar `CountVectorizer` en un corpus pequeño.<br>- **Caso A (Sucio)**: Mostrar features duplicadas (`[Correr, correr, Corriendo]`).<br>- **Caso B (Limpio)**: Mostrar features unificadas (`[correr]`).<br>- **Métrica**: Reducción del tamaño del vocabulario (ej. de 1000 a 300 tokens). |
| **40-45** | **4. Pipeline con SpaCy** | - Automatizar todo en una función `clean_text(text)`.<br>- Uso de `doc.lemma_` para reducción morfológica. |
| **45-60** | **5. Ejercicios Prácticos** | - Resolver el notebook `ejercicios_limpieza_texto.ipynb`.<br>- Reto: Limpiar dataset de reviews de Amazon (simulado). |

---

## 🛠️ Solución de Problemas Comunes (Troubleshooting)

1.  **Modelo de SpaCy no encontrado (`es_core_news_sm`)**:
    *   *Causa:* No se ha descargado el modelo.
    *   *Solución:* Ejecutar `!python -m spacy download es_core_news_sm`.

2.  **Problemas con Encoding (caracteres raros)**:
    *   *Causa:* Archivos leídos sin `encoding='utf-8'`.
    *   *Solución:* Siempre forzar UTF-8 al abrir archivos o strings.

3.  **Lemmatization incorrecta ("fuimos" -> "ir" pero "casas" -> "casas")**:
    *   *Explicación:* SpaCy es bueno, pero no perfecto. Depende del contexto (POS Tagging). Si la frase es ambigua, el lema puede fallar.

---

## 💡 Sugerencias Pedagógicas
*   **Analogía**: Compara la limpieza de texto con "lavar las verduras antes de cocinar". Puedes cocinar con tierra (ruido), pero el plato final (modelo) sabrá mal.
*   **Debate**: Pregunta si siempre hay que pasar a minúsculas. (Respuesta: No, en NER "Apple" vs "apple" es crucial).
