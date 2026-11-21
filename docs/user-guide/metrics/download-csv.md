# Descargar los datos de una medida

**Descargar CSV** baja en un fichero lo que muestra la historia de una medida, para abrirlo en una hoja de cálculo o
en otro programa.

1. En la ficha de la medida, elige el intervalo, los nodos, la resolución y las series que quieras ([Ver la historia
   de una medida](read-history.md)).
2. Pulsa **Descargar CSV**, bajo la gráfica. No hace falta desplegar **Ver los datos**.

El fichero se llama como el nombre técnico de la medida, por ejemplo `nuba.jvm.threads.live.csv`.

## Qué lleva el fichero

El fichero es CSV según el RFC 4180, en UTF-8, con la coma como separador y el punto como separador decimal. Las horas
van en formato ISO 8601, en la hora universal (UTC), así que pueden no coincidir con las que ves en la pantalla.

Cada fila es un periodo guardado o un tramo de periodos sin datos. La columna `row` vale `summary` en un periodo
guardado y `gap` en un tramo sin datos. En un tramo sin datos, `reason` lleva el código de su motivo y los valores van
vacíos ([Saber por qué falta un periodo](read-gap.md)).

Las demás columnas dicen de qué es cada fila y sus valores:

- `node_id`, el nodo, vacío con los nodos sumados;
- `resolution`, `period_start` y `period_minutes`, la resolución, el comienzo del periodo y sus minutos;
- `metric`, `tags`, `kind` y `base_unit`, la medida, las etiquetas de la serie, el tipo y la unidad;
- `sample_count`, `total`, `min`, `max`, `mean` y `last`, los valores del periodo;
- `episode`, si el periodo empieza, sigue o cierra un episodio.
