# Guía Docente Detallada: Expresiones Regulares (Script paso a paso)

Este documento es un guión para el instructor. Contiene las explicaciones exactas, analogías y preguntas para mantener la clase dinámica.

**Archivo del Notebook:** `clase_regex.ipynb`
**Duración:** 90 - 110 minutos

---

## 0. Introducción (Minutos 0-5)
**Objetivo**: Vender la idea. Que entiendan por qué Regex es un súpoder.

*   **🗣️ Script de Apertura**:
    > "Bienvenidos todos. Hoy vamos a aprender a usar la 'navaja suiza' del procesamiento de texto: las Expresiones Regulares o Regex."
    > "¿Alguna vez han tenido que extraer todos los correos de un documento de 500 páginas? ¿O validar si un RUT/DNI está bien escrito? Si intentan hacer esto con `if` y `for` en Python, terminarán con 50 líneas de código y muchos dolores de cabeza. Con Regex, es una sola línea."
    > "Advertencia: La sintaxis parece críptica al principio, como si un gato caminara sobre el teclado. ¡No se asusten! Hoy vamos a descifrarla."

---

## 1. Fundamentos: Sets y Clases (Minutos 5-15)
**Notebook**: Sección 1.

*   **Acción**: Ejecutar la celda de importación y la función `mostrar_matches`.
*   **🗣️ Explicación**:
    > "Empecemos por lo básico. Regex es un lenguaje de patrones. Si escribo la palabra 'casa', buscará literalmente c-a-s-a."
    > "Pero la magia está en la generalización.
    > *   `\d`: Es cualquier dígito (0-9). Piensen en 'd' de 'dígito'.
    > *   `\w`: Es cualquier caracter de palabra (Letras, números, guión bajo). Piensen en 'w' de 'word'.
    > *   `\s`: Es espacio. Piensen en 's' de 'space'."
*   **💻 Demo**: Muestra el ejemplo buscando `\d{3}` (tres dígitos seguidos).
*   **❓ Pregunta a la clase**:
    > "¿Si quiero buscar una vocal, qué uso? `\w` me traería consonantes también..."
    > *(Respuesta esperada: Usar corchetes `[aeiou]`)*.
    > "Exacto. Los corchetes `[]` definen un SET. Significa 'Cualquiera de estos caracteres'."

---

## 2. Greedy vs Lazy (Minutos 15-30)
**Notebook**: Sección 2. **CRÍTICO**: Este es el concepto donde más fallan los principiantes.

*   **🗣️ Explicación**:
    > "Ahora hablemos de cuantificadores. `*` significa 'cero o más veces'. `+` significa 'una o más veces'."
    > "Pero cuidado: Regex es **CODICIOSO** (Greedy) por naturaleza."
*   **Analogía**:
    > "Imaginen que Regex es como Pac-Man. Si le dices 'come todo lo que puedas hasta encontrar un cierre', se comerá todo hasta el ÚLTIMO cierre que vea en la línea."
*   **💻 Demo**: Ejecutar el ejemplo de HTML `<div>...</div>`.
    > "Miren el resultado de `<.*>`. Se comió todo el string hasta el final."
    > "¿Cómo le decimos que pare en cuanto encuentre el *primer* cierre?"
*   **El Truco**:
    > "Agregamos un signo de interrogación `?` después del cuantificador. `.*?`. Esto lo vuelve **PEREZOSO** (Lazy). Significa: 'Coincide lo mínimo indispensable'."
    > "Esto salvará sus vidas cuando parsens HTML o JSON."

---

## 3. Grupos Nombrados (Minutos 30-50)
**Notebook**: Sección 3.

*   **🗣️ Explicación**:
    > "Hasta ahora solo buscamos. ¿Y si queremos extraer? Para eso son los paréntesis `()`."
    > "El problema clásico: `m.group(1)`, `m.group(2)`... Es confuso. Si cambias la regex, rompes los índices."
*   **Mejor Práctica**:
    > "Usen **Grupos Nombrados**: `(?P<nombre>patron)`. Es un poco más largo de escribir, pero hace que su código sea legible."
*   **💻 Demo**: Ejemplo de la fecha `ISO 8601`.
    > "Vean cómo extraemos `anio`, `mes` y `dia` directamente en un diccionario. Esto es oro para Data Science."

---

## 4. Lookarounds (Minutos 50-70)
**Notebook**: Sección 4. (Nivel Avanzado)

*   **🗣️ Explicación**:
    > "Llegamos a la magia negra. Los **Lookarounds**."
    > "A veces quieres buscar algo, pero solo si tiene algo específico al lado... ¡pero no quieres incluir ese algo en el resultado!"
*   **Analogía**:
    > "Es como mirar por la mirilla de la puerta. Ves quién está, confirmas que es seguro, pero NO abres la puerta (no consumes caracteres)."
*   **Tipos**:
    > 1.  `(?=...)` **Positive Lookahead**: Mira adelante. 'Dime si lo siguiente es X'.
    > 2.  `(?<=...)` **Positive Lookbehind**: Mira atrás. 'Dime si lo anterior era X'.
*   **💻 Demo**: El ejemplo de los precios.
    > "Queremos solo el número, pero solo si tiene el signo `$` antes. `(?<=\$)\d+`."
    > "Fíjense que el `$` no aparece en el match, solo sirvió de condición."

---

## 5. Taller: Log Parsing (Minutos 70-100)
**Notebook**: Sección 5.

*   **Actividad**:
    > "Muy bien, basta de teoría. Tenemos un log de servidor real. Es un desastre de texto."
    > "Vamos a construir la Regex gigante juntos, paso a paso."
*   ** Paso a Paso en vivo**:
    1.  "Primero, capturemos la IP. `(?P<ip>\d+\.\d+\.\d+\.\d+)`"
    2.  "Luego viene un guión y espacio. `\s-\s`"
    3.  "Ahora la fecha entre corchetes... Cuidado!! ¿Greedy o Lazy? ¡Lazy! `\[(?P<fecha>.*?)\]`"
    4.  "Y el método HTTP..."
*   **Tip de Experto**:
    > "En Python, usen `re.VERBOSE`. Les permite escribir la regex en múltiples líneas y poner comentarios. Si escriben una regex de 100 caracteres en una sola línea, la odiarán mañana."
*   **Resultado**: Mostrar el DataFrame de Pandas creado mágicamente desde el texto plano.

---

## 6. Cierre (Minutos 100-110)
*   **Resumen**:
    > "Hemos visto desde `.` hasta Lookarounds. Tienen herramientas para el 99% de los casos."
*   **Entrega de Ejercicios**:
    > "Para la próxima, tienen 4 misiones en el notebook de ejercicios. Empiezan fácil (fechas) pero el Nivel 4 requiere Lookarounds. ¡Suerte!"
