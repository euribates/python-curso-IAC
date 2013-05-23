=======================================================================
Apéndice 2: "One liners"
=======================================================================

Codificar/decodificar un texto o fichero con base64::
-----------------------------------------------------------------------

Base 64 es un sistema de numeración posicional que usa 64 como base. Esta
es la mayor potencia de dos que puede ser representada usando únicamente los caracteres imprimibles de ASCII puro. Se usa para codificación de correos electrónicos, PGP y otras aplicaciones::

    $ python -m base64 -e <input
    $ echo "hola, mundo" | python -m base64 -e

    $ python -m base64 -d <input
    $ echo "aG9sYSwgbXVuZG8K" | python -m base64 -d

"Cifrar" texto con ROT-13
-----------------------------------------------------------------------

Cifra un texto en ROT-13 (Rotar 13 veces). Este cifrado es demasiado sencillo
para que sea utilizable, excepto para evitar una lectura casual: ROT-13
se ha descrito como el "equivalente en Usenet de una revista que imprime
bocabajo la respuesta a un pasatiempo"::

    $ echo "Hola, Cesar" | python -m encodings.rot_13

Se codifica y descodifica igual::

    $ echo "Ubyn, Prfne" | python -m encodings.rot_13

Validar y reformatear json::
-----------------------------------------------------------------------

A partir de texto json_, lo valida y lo imprime formateado de
forma más agradable para el lector humano::

    $ python -m json.tool <input

Se complementa muy bien con la utilidad curl_, de forma que podemos
obtener json desde una direccion y formatearla con la siguiente línea::

    $ curl <URL> | python -m json.tool

Servidor de correo de pruebas
-----------------------------------------------------------------------

La siguiente línea crea un servidor smtp que imprime los correos que
recibe en la línea estandar (Y  no los envia, claro). Es útil para
desarrollo web y para crear baterias de test que comprueben nuestros
envios de correo.

    python -m smtpd -n -c DebuggingServer localhost:1025

Servidor web
-----------------------------------------------------------------------

Las siguientes líneas arrancan un servidor web, que monstrara los contenidos
del directorio actual, y que permitira descargar los ficheros que se
encuentra en el directorio actual o es sus descendientes.

Para Python 2.x::

    $ python2 -m SimpleHTTPServer [port#]

Para Python 3.x::

    $ python3 -m http.server [--cgi] [port#]

Véase Waitress_ para un ejemplo de servidor web más orientado a
producción en Python.

Compresión y decompresion de archivos con gzip/zip
--------------------------------------------------------------------

Para comprimir o descomprimir ficheros con gzip::

    $ python -m gzip [file] # comprimir
    $ python -m gzip -d [file] # descomprimir

Para gestionar archivadores .ZIP::

    $ python -m zipfile -l <file> # listar contenidos
    $ python -m zipfile -t <file> # test
    $ python -m zipfile -e <file> <dir> # extraer
    $ python -m zipfile -c <file> sources... # crear

Cliente sencillo ftp
-----------------------------------------------------------------------

Permite recuperar rapidamente un archivo desde un servidor FTP, usando
un usuario anónimo (o, si está definido, leyendo usuario y
password del fichero ``.netrc``)::

    $ python -m ftplib host -p <ruta al fichero>

Extraer el texto de un fichero en HTML
-----------------------------------------------------------------------

    $ python -m htmllib <archivo>

Listar el contenido de un buzón POP3
-----------------------------------------------------------------------

    $ python -m poplib <server> <username> <password>


MIME type/extension database
-----------------------------------------------------------------------

Consultar la base de datos de tipos MIME. Para ver el tipo MIME que le correspondería a un fichero, basándonos en su extensión::

    $ python -m mimetypes file.ext

Para ver las extensiones aosciadas con un determinado tipo MIME::

    $ python -m mimetypes -e mime/type

Abrir un navegador
-----------------------------------------------------------------------

Para abrir una página web en un navegador::

    $ python -m webbrowser -n <url>

Para abrir una página web en un navegador, pero en una nueva pestaña
si el navegador::

    $ python -m webbrowser -t <url> # new tab

Antigravedad
-----------------------------------------------------------------------

    $ python -m antigravity


Navegador Documentacion python
----------------------------------------------------------------------

Para abrilo en modo consola (parecido a man)::

    $ python -m pydoc <topic>

Para abrilo en modo gráfico::

    $ python -m pydoc -g

Para abrirlo como un servidor web en un puerto determinado::

    $ python -m pydoc -p <port> # star

Comparar directorios:
-----------------------------------------------------------------------

Comparar el contenido de dos directorios::

    python -m filecmp dir1 dir2

Si queremos que incluya recursivamente todos los directorios::

    python -m filecmp -r dir1 dir2


Varios
-----------------------------------------------------------------------

Imprime un calendario (como cal) pero puede sacar html y tienen unas cuantas
opciones de formato::

    $python -m calendar

Para ver las opciones::

    $ python -m calendar --help



Formatear párrafos de un fichero de texto::

    python -m formatter [file]

Mostrar la plataforma actual (como ``uname`` pero más sencillo):

    $ python -m platform


.. _Waitress: https://github.com/Pylons/waitress
.. _json: http://en.wikipedia.org/wiki/JSON
.. _curl: http://en.wikipedia.org/wiki/CURL