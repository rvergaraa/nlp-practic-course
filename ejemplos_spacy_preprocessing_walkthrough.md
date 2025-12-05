# Guía de Clase: Preprocesamiento con SpaCy

Esta guía sirve como apoyo paso a paso para dictar la clase práctica utilizando el script `ejemplos_spacy_preprocessing.py`.

## 1. Preparación Previa
Asegúrate de tener el entorno listo antes de proyectar.

### Terminal
```bash
# 1. Crear entorno (si no existe)
python -m venv .venv

# 2. Activar entorno
# Windows:
.\.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 3. Instalar librerías
pip install spacy

# 4. Descargar modelo en español
python -m spacy download es_core_news_sm
```

## 2. Desarrollo de la Clase (Paso a Paso)

Abre el archivo `ejemplos_spacy_preprocessing.py` y ejecútalo paso por paso o comenta/descomenta secciones.

### Introducción
*   **Objetivo**: Mostrar cómo una máquina "lee" texto crudo y lo convierte en algo estructurado.
*   **Analogía**: Aprender un idioma implica entender vocabulario (tokens), gramática (POS) y raíces (lemas).

### Paso 1: Carga del Modelo
> "SpaCy necesita un 'cerebro' pre-entrenado para entender el idioma."

```python
nlp = spacy.load("es_core_news_sm")
```
*   **Nota**: `sm` significa "small" (pequeño). Es rápido y bueno para estas tareas básicas.
*   **Error común**: Olvidar descargarlo previamente (`ModuleNotFoundError`).

### Paso 2: Tokenización
> "Lo primero es cortar el texto en pedacitos."

*   **Concepto**: Separar palabras y signos de puntuación.
*   **Mostrar en código**:
    ```python
    tokens = [token.text for token in doc]
    ```
*   **Destacar**: SpaCy es inteligente, separa "tú" de "," automáticamente.

### Paso 3: Lematización
> "Para la máquina, 'corriendo', 'correré' y 'corrió' son palabras distintas. Queremos que entienda que es la misma acción."

*   **Concepto**: Reducir a la forma base (infinitivo para verbos, singular para sustantivos).
*   **Mostrar en código**: `token.lemma_`
*   **Ejemplo**: `corriendo` -> `correr`.

### Paso 4: POS Tagging (Etiquetado Gramatical)
> "¿Qué rol cumple cada palabra en la oración?"

*   **Concepto**: Sustantivo, Verbo, Adjetivo, etc.
*   **Mostrar en código**: `token.pos_`
*   **Utilidad**: Filtrar solo sustantivos para saber de qué se habla en un texto.
*   **Demo**: Mostrar `spacy.explain(token.pos_)` para ver qué significa la etiqueta (ej: `PROPN` = Nombre Propio).

### Paso 5: Stop Words (Palabras Vacías)
> "Palabras que sobran para el análisis de contenido."

*   **Concepto**: "El", "de", "y", "a". Son muy frecuentes pero aportan poco significado semántico único.
*   **Mostrar en código**: `token.is_stop`
*   **Visualización**: Mostrar cuánto se reduce el texto al quitarlas.

### Paso 6: Ejercicio Combinado (El Pipeline de Limpieza)
> "Juntemos todo en una función real."

Esta es la función que usarán en sus proyectos.
1.  **Entrada**: Texto sucio.
2.  **Proceso**:
    *   Tokenizar (automático al crear `doc`).
    *   Filtrar Stop Words (`!token.is_stop`).
    *   Filtrar Puntuación (`!token.is_punct`).
    *   Extraer Lemas (`token.lemma_`).
    *   Normalizar (minúsculas `.lower()`).
3.  **Salida**: Lista limpia de palabras clave.

## 3. Demo en Vivo
1.  Ejecuta el script completo: `python ejemplos_spacy_preprocessing.py`
2.  Muestra la salida en la terminal.
3.  Modifica la variable `texto_ejemplo` con una frase sugerida por los alumnos para probar en tiempo real.
    *   *Ejemplo sugerido*: "Los estudiantes de la universidad están aprendiendo NLP hoy."
