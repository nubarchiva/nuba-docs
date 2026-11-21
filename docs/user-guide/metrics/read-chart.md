# Leer la gráfica de una medida

La gráfica de la historia dibuja lo que se guardó de una medida en el intervalo elegido. Puedes leer el valor de cada
instante, ampliar un tramo y ocultar una línea.

La gráfica es lo primero de la **Historia** de la ficha ([Ver la historia de una medida](read-history.md)).

## Cómo se dibuja cada medida

Con una sola línea, el dibujo depende del tipo de la medida, que la ficha dice junto a su nombre técnico:

- Un indicador, como «Hilos vivos de la JVM», se dibuja como su media, con una banda del mínimo al máximo. La
  leyenda lleva **Mínimo**, **Máximo** y **Media**.
- Un contador se dibuja en barras, con el total de cada periodo. La leyenda lleva **Total del periodo**.
- Una duración se dibuja en dos gráficas, una encima de otra. Arriba van **Máximo** y **Media**, y abajo, el
  **Recuento** en barras.

Con varias líneas, por ejemplo una por serie o una por nodo, cada línea se dibuja con el valor que eliges en
**Estadístico**, y la leyenda la nombra por sus etiquetas, como `class=identified`.

## Leer, ampliar y ocultar

1. Pasa el puntero por la gráfica. Debajo, la leyenda da el **Instante** y el valor de cada línea en él. Donde no hay
   datos, el valor sale como «—».
2. Para ampliar un tramo, arrastra sobre la gráfica de un extremo a otro del tramo. Con dos gráficas, las dos se
   amplían a la vez.
3. Para volver al intervalo entero, pulsa **Ver todo el intervalo**, que sale solo con un tramo ampliado. También
   puedes hacer doble clic sobre la gráfica.
4. Para ocultar una línea, pulsa su nombre en la leyenda. Vuelve a pulsarlo para que aparezca otra vez.

Ampliar un tramo no cambia el intervalo de la historia, ni la tabla de **Ver los datos**, ni lo que descargas. Para
ver otro intervalo, elígelo en **Cuándo**.

Si un periodo no tiene datos, la gráfica deja un hueco ([Saber por qué falta un periodo](read-gap.md)).
