
import json
import os

def create_markdown_cell(source_lines):
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in source_lines]
    }

def create_code_cell(source_lines):
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source_lines]
    }

exercises_cells = [
    create_markdown_cell([
        "## Ejercicios Adicionales: Práctica Detallada",
        "",
        "Vamos a profundizar antes de pasar a la vectorización. Realiza los siguientes mini-ejercicios."
    ]),
    create_code_cell([
        "texto_ejercicio = \"\"\"",
        "El procesamiento de lenguaje natural (NLP) es una rama de la inteligencia artificial.",
        "Ayuda a las computadoras a entender, interpretar y manipular el lenguaje humano.",
        "¿Podrá la IA escribir novelas completas algún día?",
        "\"\"\"",
        "",
        "doc_ejercicio = nlp(texto_ejercicio)",
        "print(texto_ejercicio)"
    ]),
    create_code_cell([
        "# Ejercicio A: Contar Tokens Reales",
        "# Cuenta cuántos tokens hay en el texto EXCLUYENDO puntuación y espacios en blanco.",
        "# Pista: Usa token.is_punct y token.is_space",
        "",
        "def contar_tokens_reales(doc):",
        "    contador = 0",
        "    # TODO: Tu código aquí",
        "    return contador",
        "",
        "print(f\"Tokens reales: {contar_tokens_reales(doc_ejercicio)}\")"
    ]),
    create_code_cell([
        "# Ejercicio B: Extraer Sustantivos",
        "# Devuelve una lista con todos los sustantivos (NOUN) del texto.",
        "# Pista: Usa token.pos_",
        "",
        "def extraer_sustantivos(doc):",
        "    sustantivos = []",
        "    # TODO: Tu código aquí",
        "    return sustantivos",
        "",
        "print(f\"Sustantivos: {extraer_sustantivos(doc_ejercicio)}\")"
    ]),
    create_code_cell([
        "# Ejercicio C: Extraer Verbos (Lemas)",
        "# Devuelve una lista con los LEMAS de todos los verbos (VERB y AUX) del texto.",
        "",
        "def extraer_verbos(doc):",
        "    verbos_lemas = []",
        "    # TODO: Tu código aquí",
        "    return verbos_lemas",
        "",
        "print(f\"Verbos (Lemas): {extraer_verbos(doc_ejercicio)}\")"
    ]),
    create_code_cell([
        "# Ejercicio D: Pipeline de Limpieza Avanzado",
        "# 1. Tokenizar",
        "# 2. Filtrar Stop Words, Puntuación y Espacios",
        "# 3. Devolver lista de LEMAS en minúsculas",
        "",
        "def limpiar_texto_avanzado(texto):",
        "    doc = nlp(texto)",
        "    tokens_limpios = []",
        "    # TODO: Tu código aquí",
        "    return tokens_limpios",
        "",
        "print(f\"Texto Limpio: {limpiar_texto_avanzado(texto_ejercicio)}\")"
    ])
]

solutions_cells = [
    create_markdown_cell([
        "## Ejercicios Adicionales: Práctica Detallada (Solución)"
    ]),
    create_code_cell([
        "texto_ejercicio = \"\"\"",
        "El procesamiento de lenguaje natural (NLP) es una rama de la inteligencia artificial.",
        "Ayuda a las computadoras a entender, interpretar y manipular el lenguaje humano.",
        "¿Podrá la IA escribir novelas completas algún día?",
        "\"\"\"",
        "",
        "doc_ejercicio = nlp(texto_ejercicio)"
    ]),
    create_code_cell([
        "# Ejercicio A: Contar Tokens Reales",
        "def contar_tokens_reales(doc):",
        "    contador = 0",
        "    for token in doc:",
        "        if not token.is_punct and not token.is_space:",
        "            contador += 1",
        "    return contador",
        "",
        "print(f\"Tokens reales: {contar_tokens_reales(doc_ejercicio)}\")"
    ]),
    create_code_cell([
        "# Ejercicio B: Extraer Sustantivos",
        "def extraer_sustantivos(doc):",
        "    sustantivos = [token.text for token in doc if token.pos_ == \"NOUN\"]",
        "    return sustantivos",
        "",
        "print(f\"Sustantivos: {extraer_sustantivos(doc_ejercicio)}\")"
    ]),
    create_code_cell([
        "# Ejercicio C: Extraer Verbos (Lemas)",
        "def extraer_verbos(doc):",
        "    verbos = [token.lemma_ for token in doc if token.pos_ in [\"VERB\", \"AUX\"]]",
        "    return verbos",
        "",
        "print(f\"Verbos (Lemas): {extraer_verbos(doc_ejercicio)}\")"
    ]),
    create_code_cell([
        "# Ejercicio D: Pipeline de Limpieza Avanzado",
        "def limpiar_texto_avanzado(texto):",
        "    doc_local = nlp(texto)",
        "    tokens_limpios = [",
        "        token.lemma_.lower() ",
        "        for token in doc_local ",
        "        if not token.is_stop and not token.is_punct and not token.is_space",
        "    ]",
        "    return tokens_limpios",
        "",
        "print(f\"Texto Limpio: {limpiar_texto_avanzado(texto_ejercicio)}\")"
    ])
]

def patch_notebook(filepath, new_cells, insert_before_marker):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    insert_index = -1
    for i, cell in enumerate(nb['cells']):
        # Look for the marker in markdown cells
        if cell['cell_type'] == 'markdown':
            source_text = "".join(cell['source'])
            if insert_before_marker in source_text:
                insert_index = i
                break
    
    if insert_index != -1:
        print(f"Found marker '{insert_before_marker}' at index {insert_index} in {filepath}")
        # Insert cells
        nb['cells'][insert_index:insert_index] = new_cells
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1) # Original file uses 1 space indent based on previous view_file
        print(f"Successfully patched {filepath}")
    else:
        print(f"Error: Could not find marker '{insert_before_marker}' in {filepath}")

# Patch Exercises Notebook
patch_notebook('clase_nlp_ejercicios.ipynb', exercises_cells, "## Ejercicio 1: Limpieza")

# Patch Solutions Notebook
# Note: In soluciones, the marker might be different or same. Checking content...
# It is "## Ejercicio 1: Limpieza y Vectorización (Solución)"
patch_notebook('clase_nlp_soluciones.ipynb', solutions_cells, "## Ejercicio 1: Limpieza")
