# Regenerar las miniaturas que faltan

Con **Regenerar miniaturas** generas de una vez las miniaturas que faltan de las digitalizaciones del almacén, también
las que no se pudieron generar al subirlas. Sirve, por ejemplo, para que los PDF subidos antes de que la aplicación
generara su miniatura dejen de mostrar el icono de su tipo.

## Qué ficheros tienen miniatura

La aplicación genera la miniatura de las imágenes que sabe leer, como JPEG y PNG, la de los PDF, a partir de su
primera página, y la de los vídeos MP4, a partir de uno de sus fotogramas. Para los MP4 hace falta que la instalación
tenga el programa `ffmpeg`, del que se encarga quien administra el servidor. Los demás ficheros se muestran con el icono
de su tipo.

Algunos PDF no tienen miniatura, o les falta parte de ella, salvo que la instalación tenga también el programa Poppler. Son,
por ejemplo, los que llevan una imagen muy grande o imágenes JPEG 2000. Los PDF cifrados, por ejemplo los que piden contraseña
o restringen la copia o la impresión, nunca la tienen.

Quien administra la instalación puede elegir otra página de los PDF u otro momento de los vídeos, o que los de un tipo no
tengan miniatura. El cambio vale para las miniaturas que se generen desde entonces.

Los ficheros de la misma carpeta que se llaman igual salvo la extensión comparten miniatura. Si uno es una imagen, se
genera desde ella. Si ninguno lo es, como un PDF y un vídeo, se queda la del que subiste primero, salvo que de ese no se
haya podido generar.

La regeneración no cambia las miniaturas que ya existen ni las que se asignaron a mano. Un fichero del que no se puede
generar la miniatura, como un PDF dañado o cifrado o un MP4 sin `ffmpeg`, sigue con el icono de su tipo, y la regeneración lo
vuelve a intentar cada vez que la lanzas.

## Lanzar la regeneración

1. Abre **Administración** y, en el apartado **Descripciones de Archivo**, **Regenerar miniaturas**.

    ![La página Regenerar miniaturas, con lo que hace la acción y el botón Regenerar ahora.](../assets/screenshots/es/regenerar-miniaturas/pagina.png){ width="638" }

2. Pulsa **Regenerar ahora** y, en **Se iniciará el proceso**, pulsa **Aceptar**.

La página muestra el avance y, al terminar, el resultado, por ejemplo «Miniaturas generadas: 2. No se han podido generar: 0.
Ya existían: 15.». El trabajo queda también en **Tareas de larga duración**, como **Regenerar miniaturas**.

Si el almacén de digitalizaciones de la instalación es de solo lectura, la página lo avisa y no ofrece el botón.

## Ver qué ficheros no tienen miniatura

Si alguna no se ha podido generar, debajo del resultado salen los ficheros, cada uno con su carpeta, el problema y qué
hacer. Si por ejemplo un PDF está dañado, te pide que lo abras y lo sustituyas por una copia correcta, y si falta un
programa en el servidor, te dice cuál hay que instalar.

![Los ficheros sin miniatura, con su carpeta, el problema y qué hacer, y el botón Descargar el informe.](../assets/screenshots/es/regenerar-miniaturas/informe.png){ width="638" }

La página muestra los cien primeros. Con **Descargar el informe** los tienes todos en un fichero CSV, que se abre con una
hoja de cálculo. Si pasan de cien mil, el informe guarda los primeros y la página lo avisa.

De los ficheros que comparten miniatura sale uno solo, el que tiene preferencia para generarla. El resultado y el informe
son los de la última regeneración, y se pierden al parar la aplicación. Para verlos otra vez, vuelve a lanzarla.

## En una instalación con instituciones

La regeneración se ejecuta en la institución en la que estás. Si tienes el rol de administrador en varias, puedes
lanzarla en todas a la vez. Añade `?tenant=*` a la dirección de la página, comprueba la lista de instituciones que
muestra y lánzala como arriba.

La página solo muestra las cifras y los ficheros de la institución en la que estás, aunque la hayas lanzado en todas. Para
ver los de cada una, entra en ella y abre la misma página.
