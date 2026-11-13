# Guía de estilo de la documentación de usuario

Cómo se escribe una página de este sitio, nueva o modificada. Antes de proponer el cambio se repasa la lista de
comprobación del final.

## El principio

Una página sirve si responde pronto a la duda con la que se llega a ella. Quien la abre usa aplicaciones web a diario:
sabe rellenar un formulario, moverse por un menú y pulsar un botón. Quiere hacer algo en la aplicación y volver a su
trabajo. La página explica lo propio de nubarchiva, lo que no se ve en la pantalla y lo que tiene consecuencias. Ante
un caso que las reglas no cubran, se elige lo que deja la respuesta antes y con menos texto.

- Correcto: «**Continuar a la vista pública** muestra la página, pero cierra tu sesión de gestión.» (`publish.md`).
- Incorrecto: una tabla de lo que abre cada entrada del menú.

## Una tarea por página

Cada página explica una sola tarea, de principio a fin. Si necesita explicar dos, son dos páginas, enlazadas entre sí.

La portada de un área de la aplicación es la excepción: se titula con el nombre del área, dice para qué sirve, lista
sus tareas y explica lo que necesitan todas antes de empezar. Ejemplo: `user-guide/diffusion-portal/index.md`.

## Extensión máxima: 600 palabras

Una página tiene como mucho 600 palabras, contadas con `wc -w`. Si no cabe, es que explica más de una tarea o lo que
la aplicación ya dice en pantalla.

## El título es la tarea

El título dice lo que el lector quiere hacer, en infinitivo y con sus palabras, no con las del código ni con el nombre
técnico de la pantalla.

- Correcto: «Seleccionar un bloque», «Montar un carrusel de imágenes» (`select-block.md`, `carousel.md`).
- Incorrecto: «Panel de propiedades», «Gestión de la publicación».

La entrada de la página en `nav` de `mkdocs.yml` es su título o una forma más corta de él.

- Correcto: «Montar un carrusel» en `nav` para la página «Montar un carrusel de imágenes» (`carousel.md`).

## El resultado, en la primera frase

La primera frase dice qué consigue el lector o qué hace la aplicación. Después, los pasos. El contexto y los matices
van al final, y solo si cambian lo que el lector va a hacer.

- Correcto: «El editor guarda cada cambio solo: no hay botón de guardar.» (`save-changes.md`).
- Incorrecto: empezar explicando cómo funciona el guardado por dentro.

## Pasos numerados

Las acciones propias de la tarea van en una lista numerada, en su orden. Rellenar un formulario o aceptar una
ventana no es un paso. Después de la acción se dice solo lo que la pantalla no muestra o lo que tiene consecuencias.

- Correcto: «Arriba, pulsa **Móvil**, **Tableta** o **Escritorio**. La página se dibuja con el ancho de ese
  dispositivo: 375, 768 o 1280 píxeles.» (`publish.md`).
- Incorrecto: tres pasos para escribir el usuario, escribir la contraseña y pulsar **Entrar**.

Si la tarea se hace de varias formas, cada una va en su sección, con su lista. Una alternativa corta, como el
teclado, va en una frase tras la lista.

## Tuteo, con la voz del producto

Se habla al lector de tú, con la voz de los textos de la aplicación: formal con tuteo, en español de España.
El registro es el cuidado que espera quien trabaja en un archivo o una biblioteca, sin coloquialismos, y la cercanía
la da el tú; para matizar se usan el condicional con «si» y las construcciones con «se». Para el equipo, la fuente de
esta voz es la guía de microcopy del producto (`microcopy-guidelines.md` del workspace de nubarchiva, §1).

- Correcto: «Los visitantes del portal no ven nada de lo que cambias hasta que publicas.» (`publish.md`).
- Correcto: «Si recargas la página, el cambio sigue ahí.» (`save-changes.md`).
- Correcto: «Otros cambios, como añadir un bloque, se guardan igual aunque no muestren el aviso.»
  (`save-changes.md`).
- Incorrecto: «El usuario deberá pulsar…», «Pulse…».

## Castellano fácil de traducir

Habrá versión en inglés, así que se escribe para que se traduzca frase a frase sin reescribirla:

- Una idea por frase. Dos verbos principales unidos por «y» suelen ser dos frases.
- Sin incisos entre rayas ni paréntesis largos.
- Sin modismos ni juegos de palabras.
- Una palabra, un sentido en toda la página. Si el lector «pulsa» un botón, no lo «presiona» ni lo «clica» después.

Ejemplo correcto: «Para cambiar un bloque, primero lo seleccionas. Sus opciones se abren en el panel de la derecha.»
(`select-block.md`).

Las reglas generales de redacción están en la guía de idioma del workspace (`language-guidelines.md`, §2 y §5).

## Botones, menús y campos, como los rotula la aplicación

Lo que el lector ve escrito en pantalla se nombra con el texto exacto de la aplicación, con sus mayúsculas:

- Botones, menús, pestañas y campos, en negrita: **Publicar**, **Vista previa**, **Más acciones**.
- Los avisos y mensajes, entre comillas angulares y completos: «¡Publicado! Los visitantes ya ven tus cambios.»
  (`publish.md`).
- Para llegar a una pantalla, su ruta en un solo paso: «En **Administración**, apartado **General**, pulsa **Portal
  de Difusión**.». Incorrecto: dos pasos, uno por menú.

El texto exacto se comprueba en el código de la aplicación o en su pantalla, nunca de memoria. Si la aplicación
cambia un rótulo, la página cambia con ella.

Las teclas van en texto normal: Tab, Intro.

## Página de producto, sin cliente

La página de producto describe la tarea tal como la ofrece nubarchiva, sin instituciones reales:

- No nombra clientes, instituciones reales ni su configuración.
- Nombra como posibilidades las capacidades de personalización de la tarea: «se puede configurar para…».
- Habla de una sola institución: «la web pública de tu archivo» (`user-guide/diffusion-portal/index.md`). No menciona el
  trabajo con varias instituciones, ni como capacidad: va en la documentación del cliente que lo usa. Incorrecto:
  «nubarchiva se puede configurar en modo multi-institución».

La página de un cliente explica cómo tiene configuradas esas personalizaciones y sus desarrollos propios, y remite a
la página de producto para lo común.

## Capturas e imágenes de la aplicación

- Toda captura de la aplicación la genera la orden de capturas (`nuba-capture` del módulo `docs-capture` de `nuba-qa`)
  y está en su manifiesto. Una captura hecha a mano no se sube.
- Su letra se lee sin esfuerzo a la anchura con que el sitio la muestra, con la escala de la orden. La imagen no se
  recorta ni se escala a mano: se cambia el paso de la orden y se vuelve a ejecutar.
  - Correcto: cambiar el paso `portal.save-changes` si no se lee el aviso «Guardado».
  - Incorrecto: el menú superior entero en una franja de 1038 × 89 píxeles, de letra diminuta en el sitio.
- Una captura va solo donde ayuda a localizar algo en la pantalla o a reconocer el resultado.
- La captura acompaña al paso que muestra, nunca lo sustituye: la página se entiende sin ver las imágenes.
- Cada imagen lleva un texto alternativo que dice lo que muestra.

## Oscaria, el mundo de los ejemplos

Ejemplos y capturas usan un mismo mundo inventado: Oscaria, un municipio que no existe, y su Archivo
Municipal, la única institución que aparece.

- Oscaria está en los datos: nombres de fondos, series, fechas, personas. La página nunca cuenta historias de Oscaria
  ni la presenta.
- Sus datos concretos están solo en `docs-capture` de `nuba-qa`. La página los usa tal cual y esta guía no los copia.
- Ningún ejemplo usa una institución, un municipio o una persona reales.

## Imágenes del contenido de ejemplo

Las imágenes de los documentos de ejemplo:

- muestran objetos de archivo, como documentos, mapas o fotografías antiguas, y no lugares reconocibles;
- son de dominio público o CC0, sin ninguna otra licencia;
- llevan su procedencia (origen, autor y licencia) registrada junto al fichero, en `docs-capture`.

## La cabecera de la página

Una página no lleva el campo `status` en su cabecera. Lo que está publicado lo decide la rama: `main` contiene lo que
ya está en una versión etiquetada ([README](README.md#cuándo-se-publica-una-página)).

## Lista de comprobación

1. Una sola tarea.
2. 600 palabras o menos con `wc -w`.
3. El título dice la tarea, en infinitivo y con las palabras del lector.
4. La primera frase dice el resultado.
5. Ningún paso enseña a rellenar un formulario, aceptar una ventana ni moverse por un menú.
6. Tuteo, con la voz de la aplicación.
7. Una idea por frase, sin incisos entre rayas ni modismos.
8. Cada rótulo y aviso coincide letra a letra con la aplicación.
9. No nombra clientes, instituciones reales ni el trabajo con varias instituciones; las personalizaciones, como
   capacidades.
10. Cada captura sale de la orden sin retoques, se lee en el sitio y ayuda a localizar algo o a ver el resultado.
11. Ejemplos con los datos de Oscaria de `docs-capture`, sin relato, e imágenes de dominio público o CC0 con su
    procedencia registrada.
12. La cabecera no lleva `status` y la página está en `nav` de `mkdocs.yml`.
