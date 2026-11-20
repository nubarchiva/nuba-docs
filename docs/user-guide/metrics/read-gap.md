# Saber por qué falta un periodo

Cuando un periodo de la historia no tiene datos, la tabla dice por qué. Los periodos seguidos sin datos por el mismo
motivo van juntos en una fila.

1. En la ficha de la medida, despliega **Ver los datos** ([Ver la historia de una medida](read-history.md)).
2. Busca las filas que tienen un texto en lugar de valores. La primera columna da el tramo, por ejemplo «20/11/2026
   01:21 a 01:29».

En la gráfica, un periodo sin datos es un hueco que la línea no cruza. Si pasas el puntero por él, los valores salen
como «—».

## Qué dice cada motivo

«No consta nada de este nodo en este periodo: no estaba midiendo o no pudo escribir en la base de datos.» El nodo no
dejó constancia de ese periodo. La historia no distingue las dos causas. Para ver si un nodo mide ahora, abre el
**Estado** ([Comprobar si cada nodo mide y guarda](node-status.md)).

«Detalle no guardado: no cambió desde el último valor guardado» sale en una medida que se guarda solo si cambia. En la
gráfica, una medida de tipo indicador no deja hueco en esos periodos: mantiene su último valor guardado.

«Detalle no guardado: no cumplió la condición de guardado» sale cuando la política guarda el detalle solo si se cumple
una condición, como pasar de un valor, y en ese periodo no se cumplió.

«Sin actividad de esta serie» quiere decir que en ese periodo la serie no tuvo nada que contar.

«No se guarda» sale cuando la política no guarda la medida o la serie ([Ver qué política de almacenamiento
rige](read-policy.md)).

«Se midió y no se guardó porque el nodo estaba cargado» quiere decir que el nodo midió el periodo cuando usaba muchas
conexiones a la base de datos. Mientras dura esa carga no escribe la historia, y lo que midió en ese periodo no llegó a
guardarse.

Si un motivo termina con «(o un límite de series la dejó sin guardar en este nodo)», hay otra causa posible. El nodo
tiene un tope de series que guarda, y esa serie pudo quedar fuera de él.

## Si la política ha cambiado

Los motivos se explican con las reglas que rigen hoy. Si el intervalo empieza antes del último cambio de la política
de esta instalación, una línea lo avisa con «El motivo de los periodos se explica con las reglas del producto y del
cliente que rigen hoy.».
