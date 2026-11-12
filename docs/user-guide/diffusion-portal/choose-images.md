---
status: published
---

# Elegir las imágenes de un bloque

Cada campo de imagen de un bloque, como **Imagen** o **Imagen de fondo**, se rellena desde el diálogo **Elegir
imagen**. El diálogo tiene una pestaña por origen de la imagen:

- **Digitalizaciones**: las copias digitales asociadas a las descripciones del archivo.
- **Imágenes del portal**: un espacio aparte para el material propio de la web, como cabeceras, logotipos o
  adaptaciones de una imagen para la difusión.
- **Dirección web**: la dirección de una imagen publicada en otro sitio.

Tú decides dónde guardas cada imagen. Un consejo: lo que preparas solo para el portal, como un recorte o una versión
retocada, va mejor en **Imágenes del portal**, para no mezclarlo con los originales del archivo.

## Elegir una imagen

1. En las opciones del bloque, busca el campo de imagen. Si está vacío, muestra el botón **Elegir imagen…**.
2. Pulsa **Elegir imagen…**. Se abre el diálogo **Elegir imagen**.
3. Pulsa la pestaña del origen: **Digitalizaciones** o **Imágenes del portal**. La pestaña muestra sus carpetas a la
   izquierda y su contenido a la derecha.
4. Entra en la carpeta de la imagen. Con **Vista de lista** ves cada imagen en miniatura junto a su nombre; con
   **Vista de mosaico**, más grande.
5. Marca el botón redondo de la imagen. Abajo aparece «Seleccionado:» con su nombre.
6. Pulsa **Vincular**. El diálogo se cierra y el campo muestra la imagen en miniatura.

Si pulsas el nombre de una imagen, se abre en grande. Desde ahí, **Vincular este** la elige directamente.

En las opciones de un bloque, el cambio se guarda solo, como cualquier otro. En el formulario de un elemento, se guarda
al pulsar **Guardar elemento** ([Guardar un elemento](save-changes.md#guardar-un-elemento)).

Con el campo vacío, el diálogo se abre en la última pestaña que usaste mientras dura tu sesión. Con una imagen ya
elegida, se abre en la pestaña de su origen.

## Cambiar o quitar la imagen

Con una imagen elegida, el campo muestra dos botones:

- **Cambiar** abre el diálogo para elegir otra.
- **Quitar** deja el campo vacío.

Si el bloque necesita la imagen, al quitarla no se guarda y sale un mensaje que te pide revisar el campo
([Cuando un cambio no se guarda](save-changes.md#cuando-un-cambio-no-se-guarda)).

## Subir una imagen desde el diálogo

Las pestañas **Imágenes del portal** y **Digitalizaciones** permiten subir imágenes de tu equipo sin salir del
editor. Si tu instalación no permite añadir digitalizaciones desde el portal, la pestaña **Digitalizaciones** no
ofrece subir.

1. En el diálogo, pulsa la pestaña y entra en la carpeta donde quieres guardar la imagen.
2. Pulsa **Subir**. Aparece la zona «Arrastra aquí los ficheros o las carpetas, o selecciónalos abajo.».
3. Pulsa **Subir ficheros** y elige una imagen, o arrástrala a esa zona.
4. La imagen se guarda en la carpeta en que estás y queda elegida: el diálogo se cierra y el campo la muestra.

Si la arrastras sobre una carpeta de la lista, se guarda en esa carpeta.

Cada vez se sube una sola imagen o una carpeta. Si eliges varias imágenes sueltas a la vez, no se guarda ninguna y la
pestaña lo dice con el nombre de cada una. Solo se admiten imágenes en formato jpg, jpeg, png, webp o gif. Con otro fichero,
la pestaña lo dice, por ejemplo «documento.txt: extensión no permitida (permitidas: jpg, jpeg, png, webp, gif).», y
no se guarda.

Si en la carpeta ya hay una imagen con el mismo nombre, la nueva no la sustituye. La pestaña lo avisa, por ejemplo
«Ya hay un fichero llamado «escudo.png» en la carpeta. Elígelo en la lista o cámbiale el nombre y vuelve a
subirlo.».

### Subir una carpeta entera

1. Pulsa **Subir** y después **Subir carpeta**, y elige una carpeta de tu equipo.
2. Sus imágenes se guardan en una carpeta con el mismo nombre, dentro de la carpeta en que estás.
3. No se elige ninguna: el campo no cambia y la lista muestra la carpeta nueva. Entra en ella y elige la imagen.

Los avisos de cada fichero que no se ha guardado siguen a la vista hasta que termina la subida.

## Usar una dirección web

1. En el diálogo, pulsa la pestaña **Dirección web**.
2. Escribe la dirección de la imagen en el campo **Dirección web de la imagen**.
3. Pulsa **Usar esta dirección**. El diálogo se cierra y el campo muestra la imagen.

Una imagen de otra web se ve mientras esa web la mantenga en la misma dirección. Si la cambia o la borra, deja de
verse en tu página. Por eso es mejor guardar las imágenes en **Imágenes del portal** o en **Digitalizaciones**.

## Qué se guarda en el campo

Al elegir una imagen de **Digitalizaciones** o de **Imágenes del portal**, el campo guarda una referencia a esa
imagen, por ejemplo `media://escudo.png` o `digitization://fondo/vista-plaza.jpg`. No se copia nada: la página usa
la imagen del almacén.

La referencia solo la entiende el portal. No es una dirección para abrir en el navegador ni para compartir fuera de
él.

Una digitalización se puede elegir también escribiendo su referencia:

1. Pulsa **Administración** en el menú superior y, después, **Gestión de digitalizaciones**.
2. En la fila de la digitalización, pulsa **Más acciones** y después **Copiar referencia para el portal**. Sale el
   aviso «Referencia copiada». La acción la ven las cuentas con permiso de administración del portal.
3. En el editor, abre el diálogo de la imagen, pulsa la pestaña **Dirección web**, pega la referencia y pulsa
   **Usar esta dirección**.

La próxima vez que abras el diálogo de ese campo, se abre en la pestaña **Digitalizaciones**.

## Enlazar a una descripción del archivo

Un campo de enlace, como **Enlace**, no tiene diálogo: admite solo una dirección, que escribes en el campo. Para que
lleve a una descripción del archivo, usa su referencia:

1. Busca la descripción con **Búsqueda**, en el menú superior.
2. En su fila de resultados o en su ficha, pulsa **Copiar referencia para el portal**.
3. En el editor, pega la referencia en el campo de enlace, por ejemplo `opac://item/E783`, y sal del campo. Aparece
   «Guardado».

En la página publicada, el enlace lleva a la ficha de esa descripción.

## Subir imágenes desde la administración

Las imágenes del portal también se suben y se organizan fuera del editor:

1. Pulsa **Administración** en el menú superior y, en el apartado **General**, pulsa **Imágenes del portal**.
2. Pulsa **Subir**. En la ventana **Subir ficheros**, pulsa **Subir ficheros** y elige las imágenes de tu equipo, o
   pulsa **Subir carpeta** y elige una carpeta.
3. Las imágenes aparecen en la lista. Las de una carpeta, en una carpeta con su nombre. Cierra la ventana.

## Ver las imágenes en la lista de elementos

En los bloques con varios elementos, como el [carrusel](carousel.md), la pestaña **Elementos** lista los elementos con
la miniatura de su imagen. Un elemento sin título se muestra como «Elemento» seguido de su posición y «(sin
título)», por ejemplo «Elemento 2 (sin título)».
