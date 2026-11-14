---
status: published
---

# Montar un carrusel de imágenes

El bloque **Carrusel de cabecera** muestra varias imágenes a todo el ancho de la página, una tras otra. Suele ir en la
cabecera.

Las imágenes se eligen, o se suben desde tu equipo, en el diálogo de cada elemento
([Elegir las imágenes de un bloque](choose-images.md)).

## Añadir el carrusel y sus imágenes

1. Abre la página en el editor ([Antes de empezar](index.md#antes-de-empezar)).
2. Pulsa **Añadir bloque** y elige **Carrusel de cabecera**. Llega con un ejemplo: el título «Lo más destacado» y
   tres imágenes, cada una con su título. Sus opciones se abren a la derecha.
3. Pasa a la pestaña **Elementos** y pulsa el primer elemento de la lista.
4. En **Imagen**, pulsa **Cambiar** y elige tu imagen en el diálogo
   ([Cambiar o quitar la imagen](choose-images.md#cambiar-o-quitar-la-imagen)).
5. Repite los pasos 3 y 4 con cada elemento del ejemplo. Para quitar uno que no necesitas, pulsa **Eliminar** en su
   fila.

Cada elemento se guarda con **Guardar elemento** ([Guardar un elemento](save-changes.md#guardar-un-elemento)). Su
**Título** se muestra como pie de la imagen: cambia el del ejemplo por el tuyo o déjalo vacío, y la imagen saldrá sin
pie. Su **Enlace** es la dirección a la que lleva la imagen al pulsarla. La imagen es obligatoria: sin ella, el
elemento no se guarda
([La imagen de un elemento es obligatoria](save-changes.md#la-imagen-de-un-elemento-es-obligatoria)).

Para añadir otra imagen, pulsa **Añadir elemento**. En la lista, un elemento sin título se llama «Elemento 1 (sin
título)», con su posición. Con **Subir** y **Bajar** cambias el orden.

Si ya tienes las imágenes en **Digitalizaciones** o en **Imágenes del portal**, puedes añadirlas todas de una vez: en
**Elementos**, pulsa **Añadir varias imágenes** y marca las que quieras
([Elegir varias imágenes a la vez](choose-images.md#elegir-varias-imagenes-a-la-vez)). Cada una pasa a ser un elemento
guardado, sin título.

## Ajustar cómo se comporta

En la pestaña **Opciones**, arriba está el **Título**: el encabezado que se muestra sobre el carrusel. El del ejemplo
es «Lo más destacado». Sin título, no se muestra ninguno.

Lo demás está en grupos plegados. Pulsa el nombre de un grupo para abrirlo
([Ver y cambiar las demás opciones de un bloque](block-options.md)).

| Grupo | Opción | Qué hace | Si no la cambias |
|---|---|---|---|
| **Paso de las imágenes** | **Pasar las imágenes solas** | Pasa de una imagen a la siguiente sin que el visitante haga nada. | Activada |
| **Paso de las imágenes** | **Tiempo entre imágenes (milisegundos)** | Tiempo que se ve cada imagen: 5000 son 5 segundos. El mínimo es 1000. | 5000 |
| **Paso de las imágenes** | **Detener al pasar el ratón** | Detiene el paso de las imágenes mientras el ratón está sobre el carrusel. | Activada |
| **Controles** | **Mostrar puntos de posición** | Muestra un punto por imagen para saltar a cualquiera. | Activada |
| **Controles** | **Mostrar flechas** | Muestra las flechas de anterior y siguiente. | Activada |

Con una sola imagen, el carrusel no pasa de imagen ni muestra flechas ni puntos, aunque estén activados.

## Cambiar la altura

Todas las imágenes del carrusel tienen la misma altura: 400 píxeles si no la cambias. Las que no tienen esa
proporción se recortan para llenar el espacio.

Para cambiarlo:

1. En **Opciones**, pulsa el grupo **Otros ajustes**.
2. En **Estilo personalizado**, pulsa **Añadir ajuste**. Se añade una fila con **Ajuste** y **Valor del ajuste**.

| Ajuste | Valor del ajuste | Qué hace |
|---|---|---|
| `slideHeight` | La altura, por ejemplo `300px` | Cambia la altura de las imágenes. |
| `imgObjectFit` | `contain` | Muestra cada imagen entera, sin recortes. Con `cover`, el valor por defecto, la imagen llena el espacio y se recorta. |

Cada ajuste va en su fila.

Para quitar un ajuste, pulsa el botón a la derecha de su fila. Al dejar el ratón sobre él, dice **Quitar este
ajuste**.

## Comprobar el resultado

1. Pulsa **Vista previa**. El carrusel pasa de una imagen a otra con el tiempo elegido.
2. Cuando esté a tu gusto, pulsa **Publicar**.
