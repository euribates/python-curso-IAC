=======================================================================
Día 3.- Python y Librerías externas
=======================================================================

Librerías externas
=======================================================================

iPython
-----------------------------------------------------------------------

iPython es un interprete interactivo de Python, similar al interprete
que viene instalado por defecto, pero con capacidades ampliadas y
mejoradas, pensando especialmente en la comunidad científica. La idea
es conseguir un entorno para cálculos y operaciones que nos
permitan explorar ideas, investigar posibilidades y modificar modelos
de forma interactiva. Para ello, iPython se basa en dos componentes:

 * Un entorno de Python interactivo mejorado
 * Una arquitectura para soportar computación paralela interactiva

Las caracteristicas más detacadas de iPython son las siguientes:

Autonumeración
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

iPython va numerando sucesivamente tanto las entradas y las salidas,
al estilo de herramientas como Matlab_ o Octave_. Esta numeración
facilita el poder luego referirnos a nuestros pasos previos.

Completado automático
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usando la tecla TAB, obtenemos completado automático de código, normalmente
dependiente del contexto, es decir, que nos muestra el completado de
código dependiendo de lo escrito antes. Por ejemplo si tenemos un objeto
en memoria ``o``, simplemente escribiendo ``o.<tab>`` obtenemos
un listado de sus métodos y atributos. Pero si estamos escribiendo
una ruta dentro del sistema de ficheros -incluso aunque sea dentro
de una string- el autocompletado mostrara los ficheros o directorios
correspondientes. De igual manera, si importamos un módulo o paquete
podemos examinar rápidamente su contenido usando el autocompletado.

Explorar objetos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tecleando ``<objeto>?`` accedemos a un resumen de las características,
métodos, atributos y documentación del objeto. Como en Python
prácticamente todo es un objeto, podemos usar este sistema para
obtener información instantanea de casi todo. Para salir
de este sistema de ayuda, si fuera necesario, pulsar ``q``.

Funciones mágicas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python define una serie de funciones mágicas que se pueden invocar de la
misma manera que si fueran ordenes de la línea de comandos. Estas
funciones u ordenes mágicas empiezan con el caracter especial ``%``
seguido de su nombre, y pueden tambien aceptar argumentos, separados
por espacios, igual que si fuera una orden de línea de comandos. Hay
dos tipos de funciones, las que implican solo una linea (En cuyo caso
la orden viene precedida por un solo caracter ``%``) y las que
implican una "celula", (Que vienen precedidas por dos caracteres
``%``). Estas últimas se aplican a un bloque de código.

Por ejemplo, la funcion mágica ``#timeit``, similar a las funciones
de rendimiento que vimos en el módulo de la librería estándar del
mismo nombre, puede ser usada para que afecte a una sola línea::

    In [1]: import re
    In [2]: %timeit re.compile('foo|bar')
    1000000 loops, best of 3: 852 ns per loop

    In [3]:

O a un bloque::

    In [14]: %%timeit
    ...: x = range(1000)
    ...: max(x)
    ...:
    10000 loops, best of 3: 32.2 us per loop

    In [15]:

Algunas de las funciones mágicas disponibles son:

  - Funciones que actuan con al código:: ``%run``, ``%edit``,
    ``%save`` y ``%macro``, entre otras.

  - Funciones que afectan al interprete: ``%colors``, ``%xmode``,
    ``%autoindent``, etc.

  - Otras funciones, como ``%reset``, ``%timeit`` o ``%paste``.

Se puede obtener una explicacion del systema de llamadas mágicas
con ``%magic``, o usar tambien el mecanismo de ayuda ``?``, por
ejemplo::

    In [8] %run?

Podemos obtener un listado de todas las funciomes mágicas disponibles
con ``%lsmagic``.

Ejecutar y editar código
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La orden mágica ``%run`` nos permite ejecutar cualquier script de
Python y cargar todos sus datos directamente en nuestro interprete,
como si se hubiera tecleado a mano. Como el fichero es releido de
disco cada vez que hagamos un ``%run``, los cambios que se hagan en el
archivo se pueden ver reflejados inmediatemente, al contrario que los
módulos, que tiene que ser recargados de forma especifica con
``reload``. iPython también incluye la función ``dreload(),`` una
versión recursiva de ``reload``.

La orden %run tiene unos indicadores especiales para medir el tiempo
de ejecución del script: ``-t`` o para ejecutarlo bajo el control
de un debugger: ``-d`` o del profiler: ``-p``.

La orden %edit abre nuestro editor favorito (Hay que especificarlo en
los ficheros de configuración de iPython, en
``~/.ipython/profile_default`` o
``~/.config/ipython/profile_default``). Cuando salimos del editor, el
código se ejecuta como si lo hubieramos escrito directamente.

These will be placed in ~/.ipython/profile_default or ~/.config/ipython/profile_default, and contain comments explaining what the various options do.

Debugging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Después de que ocurra una excepción, se puede llamar a ``%debug`` para
ejecutar de inmediato el debugger (``pdb``) en modo análisis forense y
examinar el problema. Si ejecutamos ``%pdb``, entraremos en el
debugger en cuanto se produzca la primera excepción no capturada.

Historial
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

iPython almacena todas las ordenes que recibe, así como sus
resultados. Se puede acceder facilmente a este histórico de comando
pulsando las teclas de fecha arriba o abajo.

El historial se almacena en una variables llamadas ``In`` y ``Out``,
que pueden ser accedidas usando como índices los números de línea que
iPython proporciona automáticamente. Podemos acceder a las tres
últimas salidas usando las variables llamadas ``_``, ``__`` y ``___``.

Se puede usar la función mágica ``%history`` para examinar el
historico. Hay otras funciones mágicas que también acceden a este
histórico: ``%edit``, ``%rerun``, ``%recall``, ``%macro``, ``%save`` y
``%pastebin``. Podemos usar el formato habitual para referirnos a un
conjunto de líneas, e incluso referirnos a sesiones anteriores::

    %pastebin 3 18-20 ~1/1-5

La orden anterior tomará la línea 3 y las líneas 18 a la 20 de la sesión
actual, y las lineas 1 a la 5 de la sesión anterior, y las subirá
al servicio pastebin_, devolviendo la URL correspondiente.

Comandos del sistema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se puede ejecutar cualquier comando de la shell, simplemente añadiendo
el caracter ``!`` como prefijo, por ejemplo::

    In [1]: !uname
    Linux

    In [2]:

Se puede capturar la salida, por ejemplo, para obtener una lista de
los ficheros en el directorio actual podemos hacer ``files = !ls``. Para
pasar valores almacenados en variables python debemos prefijarlas
con ``$``, por ejemplo::

    In [1]: patron = "*.py"
    In [2]: files = !ls $patron
    In [3]: files
    Out[3]:
    ['comentarios.py',
     'Database.py',
     'endirecto.borrame.py',
     'en_directo.py',
     'Filters.py',
     'Form.py',
     'test_json.py']
    In [4]:

Con un doble dolar ``$$`` podemos pasar el símbolo de ``$`` literal a
la shell, para poder accedr a las variables de entorno como ``PATH``.

iPython notebook
-----------------------------------------------------------------------

IPython notebook permite usar todas las capacidades de IPython
pero sustitutendo el entorno en consola con una página web
acceisble desde cualquier browser.

La nueva interface permite, además de usar todas las capadicades de
iPython, incorporar al flujo de trabajo, ademas del código python,
textos, expresiones matemáticas, gráficos, vídeos y practicamente
cualquier contenido que un navegador modernos sea capaz de mostrar.

Podemos arrancar este entorno con la orden::

    $ ipython notebook

Se pueden salvar las sesiones de trabajo como documentos, que mantienen
todos estos elementos y que pueden ser almacenados en sistemas de control
de versiones, o enviados por correo electrónico o salvados como ficheros
HTML o PDF para imprimir o publicar estáticamente en la web. El formato
interno de almacenamiento es json, que puede ser manipulado
con facilidad para exportar a otros formatos.

    - Crear un notebook

    - Ejecutar un código Python

    - Introducir texto

    - Formulas matemáticas (http://www.mathjax.org/)

    - Celdas Python/texto (MarkDown)

    - Formulas matemáticas

    - numpy / matplob

    - Salvar como HTML/PDF (Estático)

    - Salvar como notebook



Python Image Library (PIL) Procesado de imágenes
-----------------------------------------------------------------------

numPy Trabajndo con datos numéricos
-----------------------------------------------------------------------


Matpltlib
-----------------------------------------------------------------------


Scipy
-----------------------------------------------------------------------


Panda
-----------------------------------------------------------------------


Networkx
-----------------------------------------------------------------------


Scrapy
-----------------------------------------------------------------------


PyX
-----------------------------------------------------------------------


Scikit Machine Learning con Python
-----------------------------------------------------------------------


Interfaz con C
-----------------------------------------------------------------------

Cython es un compilador estático optimizado para los lenguajes  Python
y el lenguaje extendido Cython (Basado en Pyrex). Permite escribir
extensiones para Python en C/C++ de forma tan fácil como  si fuera
Python.

El lenguaje Cython es un superconjunto de Python, que incorpora la
posibilidad de llamar a funciones en C y de declarar tipos de datos,
estructuras y, en el caso de C++, clases tal y como se hace en C/C++.
Esto permite al compilador generar un código C/C++ muy eficiente a partir
del código Cython. El código final en C/C++ se genera una sola vez y puede
luego compilarse con cualquiera de los principales compiladores de C/C++ y
producir un módulo CPython utilizable desde la versión 2.4 y
posteriores, incluyendo Python 3.x.

Waitress
-----------------------------------------------------------------------

Waitress is meant to be a production-quality pure-Python WSGI server with very
acceptable performance. It has no dependencies except ones which live in the
Python standard library. It runs on CPython on Unix and Windows under Python
2.6+ and Python 3.2+. It is also known to run on PyPy 1.6.0+ on UNIX. It
supports HTTP/1.0 and HTTP/1.1.

For more information, see the "docs" directory of the Waitress package or
http://docs.pylonsproject.org/projects/waitress/en/latest/ .


Ejemplo de uso de python embebido
========================================================================

Gimp
------------------------------------------------------------------------

Blender
------------------------------------------------------------------------

Inkscape
------------------------------------------------------------------------


Desarrollo dirigido por pruebas: TTD
========================================================================

Python one liners
========================================================================

.. _pastebin: http://pastebin.com/
