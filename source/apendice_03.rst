=======================================================================
Apéndice 3: Version 2.7 frente a Versión 3.x
=======================================================================

La última versión de Python, a la hora de escribir esto es la 3.3.1,
estando en desarrollo la 3.4. Los cambios en la rama 3.x, como ya se
explicó, producen incompatibilidad hacia atrás; es decir, el código
escrito para las versiones anteriores no es directamente compatible
con la nueva versión. Esto no es tan grave como parece.

En primer lugar, los cambios no son tan dramáticos. Es verdad que hay
muchos más cambios de lo habitual en una nueva versión, y que algunos
de esos cambios son realmente importantes. Pero una vez analizados,
vemos que a fin de cuentas el lenguaje en si no ha cambiado tanto; la
mayor parte de los cambios se dirigen a eliminar pequeños defectos
bien conocidos, a la vez que se eliminaba algo del "polvo acumulado"
en el código.

Importar desde el futuro (con python se puede)
-----------------------------------------------------------------------

Python 2.7.x es la forma natural de migrar a Python 3k, ya que, con
ciertos mínimos ajustes, podemos conseguir que ejecute tanto código
Python 2.7 como Python 3.0. Para ello se usa una convención muy útil
que la comunidad Python ha venido usando desde hace tiempo: Importar
desde el futuro.

La costumbre es que cuando se prepara una nueva funcionalidad, antes
de publicarla oficialmente en una versión determinada, se incluye como
parte del modulo ``__future__``. De esta forma, los programadores
pueden aprender a usarla, advertir sobre errores, familiarizarse con
ella, etc... simplemente haciendo un ``import``.

Veremos algunos de las importaciones que tendremos que hacer en Python
2.7 para obtener un entorno similar a Python 3

.. note:: Todo o Nada

    Las sentencias ``from __future__ import xxx`` deben ser las primeras
    que se ejecutan dentro de un *script*; no está permitido ejecutarlas
    en medio del programa. Es una de esas situaciones todo o nada.


La función ``print``
------------------------------------------------------------------------

Este cambio es uno de los más drásticos, a nivel de sintaxis del
lenguaje, pero veremos que no es tan grave, porque los cambios que hay
que hacer para adaptar nuestro programas son triviales (Aunque, eso
si, puede que tengamos que cambiar muchas líneas de código).

Básicamente, se ha convertido la orden ``print``, que técnicamente era
una sentencia, en una llamada a una función. De forma que, siguiendo
las convenciones de llamada de funciones de Python, es obligatorio
usar paréntesis. En otras palabras, donde antes escribíamos::

    print "Hola, Mundo"

Ahora tenemos que escribir::

    print("Hola, Mundo")

Se usan parámetros por nombre para reemplazar la sintaxis especial de
la antigua sentencia `print`, veamos algunos ejemplos::

    Antes: print "La respuesta es:", 2*2
    Ahora: print("La respuesta es:", 2*2)

    Antes: print x,           # La coma final suprimía el salto de línea
    Ahora: print(x, end=" ")  # y lo sustituía por un espacio

    Antes: print              # Imprime un salto de línea
    Ahora: print()            # ¡Pero ahora es una función!

    Antes: print >>sys.stderr, "Error fatal"
    Ahora: print("Error fatal", file=sys.stderr)

Ahora también se puede definir el separador a usar, con el parámetro
``sep``, cuando imprimimos varios elementos (Si no se indica nada, se
asumirá que el separador es la cadena vacia, es decir, que no hay
separador)::

    >>> print("There are <", 2**32, "> possibilities!", sep="")
    There are <4294967296> possibilities!

La herramienta de conversión de código ``2to3`` realiza
automáticamente la transformación de sentencias ``print`` en llamadas
a la función ``print()``, para que este cambio no sea crítico para
proyectos grandes.

Para que nuestro codigo 2.7 utilice la función ``print``, pondremos al
principio la línea::

    from __future__ import print_function

Vistas e iteradores en vez de listas
-----------------------------------------------------------------------

Algunas de las API más usadas ya no devuelven listas:

 *  Los métodos de los diccionarios ``keys()``, ``items()`` y
    ``values()`` devuelven "vistas" en vez de listas.  (Una vista es
    como un iterador especial que sigue vinculada con el objeto a
    partir del cual se creó, de forma que las modificaciones en el
    objeto original afectan a la vista). Por ejemplo, el siguiente
    código fallará::

        >>> d = {'uno':1, 'dos':2}
        >>> k = d.keys()
        >>> k.sort()
        >>>

    Mejor usar ``sorted`` (Funciona desde la versión 2.5 y
    es más eficiente)::

        >>> d = {'uno':1, 'dos':2}
        >>> k = sorted(d)
        >>>

    Los métodos ``iterkeys()``, ``iteritems()`` e ``itervalues()`` ya
    no son soportados.

 *  ``map()`` y ``filter()`` devuelven iteradores. Si se necesita
    una lista, la solución más rápida es::

        >>> list(map(...))
        >>>

    Pero quizá convenga ver si se pueden sustituir todo el código
    con comprensión de listas, especialmente si en el código
    original había expresiones lambda.

 *  la función ``range()`` se comporta como solia hacerlo ``xrange()``.
    Esta última, por tanto, desaparece.

 * La función ``zip()`` devuelve un iterador.

La división de enteros
------------------------------------------------------------------------

En python 2.7, la división de un entero por un entero produce, a su
vez, un entero. Podemos probarlo en Python 2.7::

    >>> print 7/2
    3

En python 3k, la división de un entero por un entero produce un número
en coma flotante, más parecido a lo que estamos acostumbrados. Podemos
probarlo en Python 3::

    >>> print(7/2)
    3.5

Podemos usar una doble barra de división para obtener un resultado
entero, truncado. Esta capacidad existe desde hace años, al menos
desde la versión 2.2::

    >>> print(7//2)
    3

Para que nuestro codigo 2.7 utilice la nueva división, pondremos al
principio la línea::

    from __future__ import division

Unicode por defecto
------------------------------------------------------------------------

Este es uno de los cambios más importantes. Prácticamente todo lo que
se refiere a variables de texto cambia. Python 3.0 trabaja con dos
conceptos: Cadenas de texto unicode y datos binarios (mientras que
python 2.7 trabaja con cadenas de texto unicode y cadenas de texto de
8 bits).

En 3.x todo el texto es Unicode_; cualquier texto codificado se
considera ahora datos binarios. El Tipo de datos usado para texto es
``str``, y el usado para datos es ``byte``. La mayor diferencia con la
versión 2.x es que cualquier intento de mezclar texto y datos provoca
un error de tipo ``TypeError``. En la versión anterior, la mezcla de
los dos tipos podía funcionar o no: si teníamos la suerte de que las
cadenas de texto de 8 bits solo contuvieran texto ASCII de 7 bits
(Tambien llamado ASCII puro, básico o estándar) entonces funcionaba.
Si no, nos lanzaba un ``UnicodeDecodeError``. Este tipo de error ha
repartido mucha tristeza en estos años.

A consecuencia de estos cambios, casi todo el código que trabaje con
unicode, texto codificado y datos binarios tendrá que cambiar. El
cambio es para mejor, ya que el el mundo 2.x muchisimos errores tenían
que ver con estas mezclas de texto codificado con texto sin codificar.
Para prepararse para el paso a Python 3k, lo mejor es empezar a usar
texto unicode para cualquier texto que no tenga que estar codificado, y
reservar el tipo ``str```solo para textos codificados y datos binarios.
Haciendolo así la herramienta automática ``2to3`` podrá realizar la
mayor parte del trabajo por nosotros.

Ya no se podrá usar la forma u"..." para indicar literales en unicode,
porque ya no hará falta. Al contrario, tendremos que marcar con b"..."
para inidicar texto codificado o datos binarios.

Como los tipos ``str`` y ``bytes`` ya no se pueden mezclar, habrá que
realizar las conversiones explicitamente, ya sea usando los métodos
``encode()``y ``decode()`` de los tipos ``str`` y ``bytes``
respectivamente, o usando las funciones ``bytes(s, encoding=...)`` o
``str(b, encoding=...)``.

Tanto los tipos ``str`` como ``bytes`` son inmutables. Hay un tipo
diferente, llamado ``bytearray`` que si es mutable, y que podemos
usar para para mantener buffers de datos binarios.

Los archivos abiertos en modo texto (Que sigue siendo el modo por defecto
de ``open()``) siempre utilizarán algún tipo de codificación para mapear
entre los datos (bytes) guardados en disco y las cadenas de texto
(``string``) en memoria. Esto implica que si se abre un archivo con
un modo incorrecto o una codificacion erronea, se producirá un error
y se elevará la correspondiente excepción, que siempre es mejor que
empezar a emitir datos incorrectos como si no pasara nada (Los errores
nunca deberían dejarse pasar silenciosamente). También significa que
los usuarios de unix tendrán que empezar a abrir los archivos con los
que trabajen con el modo correcto: texto o binario. Hay una codificación
por defecto, que enlas plataformas unix se determinara por la variable
de entorno ``LANG``. En muchos casos, pero no siempre, la codificación
por defecto será ``utf-8``.

Como efecto adicional, los nombres de las variables tambien se codificarán
en python 3.x con unicode; esto significa que podemos tener variables
con nombres como ``árbol``, ``temporada_otoño`` e incluso ``Å``. Yo
personalmente seguire usando ASCII puro para mis variables, ya que no
creo que esto aporte muchas más legibilidad y si creo que puede aumentar
los errores.

Para que nuestro codigo 2.7 utilice literales unicode, pondremos al
principio la línea::

    from __future__ import unicode_literals

Importaciones relativas / absolutas
------------------------------------------------------------------------

La importación de módulos funciona buscando, en una serie de directorios
habilitados para ello, un fichero que corresponda con el nombre del modulo
a importar. Para estructurar mejor el código, los paquetes permiten definir
una estructura de módulos, organizados en forma de árbol. Esto funciona
muy bien, pero presentaba dos problemas:

    # En los paquetes con muchos niveles, las sententcias
      ``import`` podian acabar siendo bastante largas

    # Las importaciones podían ser ambigüas en combinación con los
      paquetes; dentro de un paquete, no quedaba claro si, al hacer
      ``import foo``, el programador se  refería a un módulo dentro
      del paquete o a un módulo fuera de este.

La solución para este segundo problema paso por hacer que todos
las importaciones sean absolutas por defecto (Es decir, que se buscará
solo en los directorios indicados por ``sys.path``), y se
usará una sintaxis especial (anteponiendo puntos) para acceder
a los módulos internos del paquete. Un único punto precediendo
al nombre del módulo significa una importación relativa, en el
mismo nivel que el actual. Dos o más puntos indican una importación
relativa con respecto a los padres del paquete actual, un nivel
por cada punto después del primero.

Veamos un ejemplo, si tenemos la siguiente estructura dentro
de un paquete::

    paquete/
    __init__.py
    subpaquete1/
        __init__.py
        moduloX.py
        moduloY.py
    subpaquete2/
        __init__.py
        moduloZ.py
    moduloA.py

Si suponemos que estamos trabajando con ``moduloX`` dentro del
``subpaquete1``, las siguientes importaciones relativas
serían todas válidas::

    from . import moduloY
    from .moduloY import spam
    from ..subpaquete1 import moduloY
    from ..subpackage2 import moduloZ
    from ..subpaquete2.moduloZ import eggs
    from .. import moduloA

las importaciones relativas siempre tienen que ser de la
forma ``from <> import <>``; la forma ``import <>`` siempre
será absoluta.

Para que python 2.7 funcione con este nuevo sistema de importaciones,
tenemos que incluir al principio de nuestro programa la línea::

    from __future__ import absolute_import


.. _Unicode: http://es.wikipedia.org/wiki/Unicode