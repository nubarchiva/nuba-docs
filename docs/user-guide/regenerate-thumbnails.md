# Regenerar las miniaturas que faltan

Con **Regenerar miniaturas** generas de una vez las miniaturas que faltan de las digitalizaciones del almacén, también
las que no se pudieron generar al subirlas. Sirve, por ejemplo, para que los PDF subidos antes de que la aplicación
generara su miniatura dejen de mostrar el icono de su tipo.

## Qué ficheros tienen miniatura

La aplicación genera la miniatura de las imágenes que sabe leer, como JPEG y PNG, la de los PDF, a partir de su
primera página, y la de los vídeos MP4, a partir de uno de sus fotogramas. Para los MP4 hace falta que la instalación
tenga el programa `ffmpeg`, del que se encarga quien administra el servidor. Los demás ficheros se muestran con el icono
de su tipo.

Los ficheros de la misma carpeta que se llaman igual salvo la extensión comparten miniatura. Si uno es una imagen, se
genera desde ella. Si ninguno lo es, como un PDF y un vídeo, se queda la del que subiste primero, salvo que de ese no se
haya podido generar.

La regeneración no cambia las miniaturas que ya existen ni las que se asignaron a mano. Un fichero del que no se puede
generar la miniatura, como un PDF dañado o un MP4 sin `ffmpeg`, sigue con el icono de su tipo, y la regeneración lo
vuelve a intentar cada vez que la lanzas.

## Lanzar la regeneración

1. Abre **Administración** y, en el grupo **Sistema**, **Regenerar miniaturas**.

    ![La página Regenerar miniaturas, con lo que hace la acción y el botón Regenerar ahora.](../assets/screenshots/es/regenerar-miniaturas/pagina.png){ width="638" }

2. Pulsa **Regenerar ahora** y, en **Se iniciará el proceso**, pulsa **Aceptar**.

La página muestra el avance y, al terminar, el resultado, por ejemplo «Miniaturas generadas: 2. No se han podido generar: 0.
Ya existían: 15.». El trabajo queda también en **Tareas de larga duración**, como **Regenerar miniaturas**.

Si el almacén de digitalizaciones de la instalación es de solo lectura, la página lo avisa y no ofrece el botón.

## En una instalación con instituciones

La regeneración se ejecuta en la institución en la que estás. Si tienes el rol de administrador en varias, puedes
lanzarla en todas a la vez. Añade `?tenant=*` a la dirección de la página, comprueba la lista de instituciones que
muestra y lánzala como arriba.
