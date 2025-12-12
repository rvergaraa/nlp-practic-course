# Guía Docente: Embeddings, Búsqueda Semántica y LLMs Locales

**Archivo del Notebook:** `clase_embeddings_llm_local.ipynb`
**Duración Estimada:** 60 - 75 minutos
**Requisitos Técnicos:** Google Colab con **T4 GPU** (Gratuito)

---

## 🎯 Objetivos de Aprendizaje
Al finalizar la clase, los estudiantes serán capaces de:
1.  **Diferenciar** conceptual y prácticamente entre una vectorización clásica (Bag of Words) y Embeddings semánticos.
2.  **Visualizar** cómo los modelos de lenguaje agrupan conceptos semánticos similares en un espacio vectorial.
3.  **Implementar** un motor de búsqueda semántica simple utilizando `SentenceTransformers`.
4.  **Desplegar** un LLM local (TinyLlama) utilizando técnicas de cuantización (4-bit) para optimizar recursos.
5.  **Integrar** búsqueda y generación en un sistema RAG (Retrieval-Augmented Generation) básico.

---

## ⏱️ Cronograma de la Clase (Minuto a Minuto)

| Tiempo | Sección | Descripción y Puntos Clave |
| :--- | :--- | :--- |
| **00-05** | **0. Setup** | - Verificar que el entorno sea **T4 GPU** (`!nvidia-smi`).<br>- Explicar brevemente las librerías: `transformers` (huggingface), `sentence-transformers` (embeddings), `bitsandbytes` (optimización). |
| **05-20** | **1. Embeddings vs BoW** | - **Teoría**: BoW cuenta palabras, Embeddings capturan significado.<br>- **Demo**: Mostrar que `CountVectorizer` no ve relación entre "Perro" y "Canino", pero los Embeddings sí.<br>- **Multilingüismo**: Destacar cómo el modelo 'paraphrase-multilingual' conecta "Dog" con "Perro". |
| **20-30** | **2. Visualización (PCA)** | - Explicar que los embeddings tienen muchas dimensiones (ej. 384).<br>- Usar PCA para bajar a 2D.<br>- **Actividad visual**: Ver en el gráfico cómo 'gato/perro' se separan de 'coche/moto'. |
| **30-45** | **3. Búsqueda Semántica** | - Concepto de **Chunking**: Dividir textos largos para no saturar el modelo. <br>- Indexar un texto de juguete (sobre IA/HuggingFace).<br>- Hacer una *query* y mostrar el resultado más relevante (`util.semantic_search`). |
| **45-60** | **4. LLMs Locales** | - Cargar `TinyLlama-1.1B`.<br>- **Concepto Clave**: Cuantización (4-bit). Explicar que esto permite correr modelos pesados en GPUs modestas.<br>- Generar un texto simple. |
| **60-70** | **5. RAG (Integración)** | - Unir las piezas: Usar el chunk recuperado en la sección 3 como contexto para el prompt del LLM.<br>- Mostrar cómo el LLM responde mejor cuando tiene "información fresca". |
| **70-75** | **6. Ejercicios ("Your Turn")** | - Dar tiempo a los alumnos para resolver los retos.<br>- **Reto 1**: Probar nuevas palabras para ver similitud.<br>- **Reto 2**: Cambiar la "sys prompt" del LLM (ej. modo Pirata). |

---

## 🛠️ Solución de Problemas Comunes (Troubleshooting)

1.  **Error de Memoria (CUDA OOM)**:
    *   *Causa:* El estudiante ejecutó celdas muy rápido o cargó modelos grandes sin reiniciar.
    *   *Solución:* `Entorno de ejecución > Reiniciar sesión` y correr todo de nuevo asegurando que se usa la configuración `bnb_config` (4-bit).

2.  **Lentitud en descargas**:
    *   La primera vez que se ejecuta `!pip install` y `model.encode`, descarga varios cientos de MB. Es normal que tome 2-3 minutos iniciales.

3.  **El gráfico PCA se ve amontonado**:
    *   Depende de la aleatoriedad de PCA y los ejemplos. Sugiere a los estudiantes agregar palabras muy distintas (ej. "Pizza", "Saturno") para ver mejor la separación.

---

## 💡 Sugerencias Pedagógicas
*   En la sección de **Embeddings**, pregúntales: *"¿Qué pasaría si usamos una palabra que tiene dos significados, como 'Banco' (dinero vs asiento)?"*. (Respuesta: Los embeddings contextuales como BERT suelen manejarlo bien, pero modelos simples de oraciones a veces promedian el significado).
*   En la sección **RAG**, haz énfasis en que **esta es la base de aplicaciones modernas** como los chatbots de soporte técnico o asistentes legales.
