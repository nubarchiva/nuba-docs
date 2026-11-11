# Guía de estilo de la documentación de usuario

Cómo se escribe una página de este sitio. Rige para toda página nueva o modificada. La lista de comprobación del final
se repasa antes de proponer el cambio.

## El principio

Una página sirve si responde pronto a la duda con la que se llega a ella. Quien la abre quiere hacer algo en la
aplicación y volver a su trabajo. Cada regla de esta guía sirve a ese principio. Ante un caso que las reglas no cubran, se
elige lo que deja la respuesta antes y con menos texto.

## Una tarea por página

Cada página explica una sola tarea, de principio a fin. Si una página necesita explicar dos tareas, son dos páginas,
enlazadas entre sí.

La portada de un área de la aplicación es la excepción: se titula con el nombre del área, dice para qué sirve, lista
sus tareas y explica lo que necesitan todas antes de empezar. Ejemplo: `user-guide/diffusion-portal/index.md`.

## Extensión máxima: 600 palabras

Una página tiene como mucho 600 palabras, contadas con `wc -w` sobre su fichero. Si no cabe, es que explica más de una
tarea o lo que la aplicación ya dice en pantalla.

## El título es la tarea

El título dice lo que el lector quiere hacer, en infinitivo y con sus palabras, no con las del código ni con el nombre
técnico de la pantalla.

- Correcto: «Seleccionar un bloque», «Montar un carrusel de imágenes».
- Incorrecto: «Panel de propiedades», «Gestión de la publicación».

El título de la página es el mismo que el de su entrada en `nav` de `mkdocs.yml`, o una forma más corta de él.

## El resultado, en la primera frase

La primera frase dice qué consigue el lector o qué hace la aplicación. Después, los pasos. El contexto y los matices
van al final, y solo si cambian lo que el lector va a hacer.

- Correcto: «El editor guarda cada cambio solo: no hay botón de guardar.» (`save-changes.md`).
- Incorrecto: empezar explicando cómo funciona el guardado por dentro.

## Pasos numerados

Lo que el lector hace va en una lista numerada, una acción por paso. Si un paso tiene un efecto visible, se dice en
el mismo paso, justo después de la acción.

- Correcto: «Pulsa **Visual**. El editor muestra la página con su aspecto final.» (`select-block.md`).

Una página con varias formas de hacer la tarea pone cada una en su sección, con su lista. Las alternativas cortas,
como hacerlo con el teclado, van en una frase después de la lista.

## Tuteo, con la voz del producto

Se habla al lector de tú, con la misma voz que los textos de la aplicación: formal con tuteo, en español de España.
La voz la fija la guía de microcopy del producto (`.ai/microcopy-guidelines.md` del workspace de nubarchiva, §1); esta
guía no la repite. Una página y la pantalla que describe suenan igual.

- Correcto: «Los visitantes del portal no ven nada de lo que cambias hasta que publicas.» (`publish.md`).
- Incorrecto: «El usuario deberá pulsar…», «Pulse…».

## Castellano fácil de traducir

La documentación tendrá una versión en inglés. Se escribe para que se traduzca frase a frase sin reescribirla:

- Una idea por frase. Dos verbos principales unidos por «y» suelen ser dos frases.
- Sin incisos entre rayas ni paréntesis largos.
- Sin modismos ni juegos de palabras.
- Una palabra, un sentido en toda la página. Si el lector «pulsa» un botón, no lo «presiona» ni lo «clica» después.

Ejemplo correcto: «Para cambiar un bloque, primero lo seleccionas. Sus opciones se abren en el panel de la derecha.»
(`select-block.md`).

Las reglas generales de redacción están en la guía de idioma del workspace (`.ai/language-guidelines.md`, §2 y §5).

## Botones, menús y campos, como los rotula la aplicación

Todo lo que el lector ve escrito en pantalla se nombra con el texto exacto de la aplicación, con sus mayúsculas:

- Botones, menús, pestañas y campos, en negrita: **Publicar**, **Vista previa**, **Más acciones**.
- Los avisos y mensajes, entre comillas angulares y completos: «¡Publicado! Los visitantes ya ven tus cambios.».
- Para llegar a una pantalla, un paso por cada menú o apartado que se pulsa, con su rótulo en negrita: «…
  pulsa **Administración** en el menú superior.» y «En el apartado **General**, pulsa **Portal de Difusión**.»
  (`user-guide/diffusion-portal/index.md`, sección «Antes de empezar»).

Ejemplo de rótulos y avisos: `publish.md`, sección «Publicar». El texto exacto se comprueba en el código de la
aplicación o en su pantalla, nunca de memoria. Si la aplicación cambia un rótulo, la página cambia con ella.

Las teclas van en texto normal: Tab, Intro.

## Página de producto, sin cliente

La página de producto describe la tarea tal como la ofrece nubarchiva, sin ninguna institución real:

- No nombra clientes, instituciones reales ni su configuración.
- Nombra las capacidades de personalización que tiene la tarea, como posibilidades: «se puede configurar para…».

La página de un cliente explica cómo tiene configuradas esas personalizaciones y sus desarrollos propios, y remite a
la página de producto para lo común.

## Capturas e imágenes de la aplicación

- Toda captura de la aplicación la genera la orden de capturas (`nuba-capture` del módulo `docs-capture` de `nuba-qa`)
  y está en su manifiesto. Una captura hecha a mano no se sube.
- Se pone una captura solo donde ayuda a localizar algo en la pantalla o a reconocer el resultado. Lo que la frase ya
  deja claro no lleva captura.
- La captura acompaña al paso que muestra, nunca lo sustituye: la página se entiende sin ver las imágenes.
- Cada imagen lleva un texto alternativo que dice lo que muestra.

## Oscaria, el mundo de los ejemplos

Todos los ejemplos y capturas usan el mismo mundo inventado: Oscaria, un municipio que no existe, y su Archivo
Municipal, la única institución que aparece.

- Oscaria está en los datos: nombres de fondos, series, fechas, personas. La página nunca cuenta una historia sobre
  Oscaria ni la presenta.
- Los datos concretos de Oscaria están en `docs-capture` de `nuba-qa`, que es su única fuente. La página los usa tal
  como están allí y esta guía no los copia.
- Ningún ejemplo usa una institución, un municipio o una persona reales.

## Imágenes del contenido de ejemplo

Las imágenes que aparecen como documentos del archivo de ejemplo:

- muestran objetos de archivo, como documentos, mapas o fotografías antiguas, y no lugares reconocibles;
- son de dominio público o CC0, sin ninguna otra licencia;
- llevan su procedencia (origen, autor y licencia) registrada junto al fichero, en `docs-capture`.

## La cabecera de la página

Una página no lleva el campo `status` en su cabecera. Lo que está publicado lo decide la rama: `main` contiene lo que
ya está en una versión etiquetada ([README](README.md#cuándo-se-publica-una-página)).

## Lista de comprobación

1. La página explica una sola tarea.
2. `wc -w` sobre la página da 600 o menos.
3. El título dice la tarea, en infinitivo y con las palabras del lector.
4. La primera frase dice el resultado.
5. Las acciones van en pasos numerados, una por paso.
6. Se habla de tú, con la voz de los textos de la aplicación.
7. Cada frase lleva una idea, sin incisos entre rayas ni modismos.
8. Cada botón, menú, campo y aviso coincide letra a letra con la aplicación.
9. La página no nombra ningún cliente ni institución real; las personalizaciones se nombran como capacidades.
10. Cada captura la genera la orden de capturas y ayuda a localizar algo o a ver el resultado.
11. Los ejemplos usan los datos de Oscaria de `docs-capture`, sin relato, y sus imágenes son de dominio público o
    CC0 con su procedencia registrada.
12. La cabecera no lleva `status` y la página está en `nav` de `mkdocs.yml`.
