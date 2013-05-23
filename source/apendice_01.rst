=======================================================================
Apéndice 1: Para programadores con experiencia en otros lenguajes
=======================================================================

Python, como cualquier otro lenguaje, tiene sus formas particulares de
realizar algunas tareas, algunas de ellas pueden ser más sorprendentes
para programadores que provengan de otros lenguajes que para una
persona que empieze de cero. [Escena del titanic]

Vamos a ver algunas de estas modismos o costumbres
que pueden sorprender a los más experimentados.

Para definir bloques de código se usa el sangrado
-----------------------------------------------------------------------

Es decir, no hay marcas de principio y fin de bloque, como en Pascal,
Delphi (BEGIN, END) o C, Java, C# (Llaves de apertura y cierre { y }).
La indentación del código marca el principio del bloque (cuando
aumenta) y el fin del bloque (cuando desminuye). Esto parecerá extraño
a la mayoría de los programadores, que están acostumbrados a que los
espacios no sean significativos.

Sin embargo, tiene muchas ventajas:

 * La mayoría de los desarrolladores ya indentan el código de todas
   maneras.    Usar el indentado para marcar los límites de los bloques
   de código simplifica la escritura y, sobre todo, la lectura del
   mismo. Presentele un trozo de código java relativamente complejo y
   sin ninguna indentación a un programador y lo primero que hará
   este, en un 99% de los casos [#]_, es indentar el código a su gusto
   mientras lo lee para entender como funciona.

 * En otros lenguajes, el indentado solo tiene una función decorativa,
   es una forma de simplificar la lectura del mismo, pero no tiene
   ningún significado real; la estructura será la que indiquen los
   marcadores de principio y fin de código. Muchos programadores se
   han dejdo las pestañas intentando encontrar un error en el flujo
   del programa porque ha indentado mal (o ha indentado bien, pero se
   le han escapado un par de llaves, por ejemplo). Si el indentado y las
   marcas no concuerdan, puede ser un problema, porque es mucho más fácil
   leer el indentado que las marcas, sobre todo si el código es
   extenso.

 * No hay distintas formas de indentar código. En C y sus derivados hay tantas
   formas que incluso se agrupan por familias, según su semejanza. Casi podriamos
   decir que hay tantos estilos de indentación como desarrolladores. En Python
   solo hay que limitarse a decidir entre espacios y tabuladores --lo recomendado
   son espacios-- y en su caso, cuantos espacios usar para cada nivel de
   indentación --lo recomendado son 4 espacios--.

 * Además, nos ahorramos dos caracteres o palabras reservadas, que se pueden
   usar en otras partes.

 * De todas formas, ibas a indentar el código, ¿no?

No hay métodos ni propiedades privadas
-----------------------------------------------------------------------

En otros lenguajes orientados a objetos como C++ o java es
posible proteger determinados métodos o atributos de nuestras
clases, de forma que sea imposible usarlas y/o modificarlas. En Python
no se puede [#]_, todos los métodos y atributos son públicos. No
existe nada que sea "privado" en el sentido de Java o C++.

Existe la convenión de marcar los atributos y métodos internos con el
caracter subrayado. Esto no tiene ningún significado especial para el
lenguaje (Excepto en el caso de los módulos cuando se importa todo el
contenido con ``from module import *``, en cuyo caso no se importan
ningún nombre que empiece por el caracter subrayado). Nada
impide que accedas a un attributo o nombre que empiece por
``_``, pero ha de entenderse que es de uso interno, que no deberías
jugar con él a no ser que sepas muy bien lo que estás haciendo, y que
si en un futuro tu código deja de funcionar porque ese atributo o
método ha desaparecido, no podrás culpar a nadie más que a ti mismo.

Eso si, no es un fallo en el lenguaje, es una decisión  consciente y
forma parte del diseño del lenguaje. La documentación de Python lo
resume de la siguiente manera: "Aquí somos todos adultos". Algunos
consideramos que la misma idea de ocultar o esconder parte del código
es "poco pythonico". Así, ninguna clase ni ningún objeto puede
mantener sus mecanismos internos ajenos al resto de los
desarrolladores. Esto hace que la introspección sea sencilla y potente.

La filosofía es que Python confía en ti y en tus habilidades. Viene a
ser algo así: "Si consideras necesario meterte por los recovecos y
usar métodos que no están diseñados para el usuario final, adelante,
pensaremos que tienes una buena razón para hacerlo, pero no digas
luego que la culpa es nuestra. Aquí somos todos adultos y todos
conocemos las reglas del juego".

Perl tiene una filosofía similar que expresa de la siguiente forma:
"[Los modulos] de Perl prefieren que te mantengas fuera de su sala de
estar, pero que lo hagas porque no estás invitado, no porque tengas
una escopeta de cañones recortados."

Estructuras de datos integradas en el lenguaje
----------------------------------------------------------------------------

En otros lenguajes, hay estructuras de datos como pilas, colas, mapas
(hash), tuplas, etc... que, por su gran utilidad, están implementadas
como librerías. Python da un paso más alla, y estas estructuras de
datos, entre otras, forman parte nativa del lenguaje. Esto permite que
el lenguaje interactue con estas estructuras de forma mucho más
fluida.

El bucle ``for``, por ejemplo, está diseñado nativamente para que
itere sobre aquellas estructuras de datos que sean "iterables", de
las cuals la lista es el más habitual, pero no el único ni mucho menos.
Veamos lo que significa esto con un ejemplo: Para imprimir una lista de
nombres guardados en la variable ``lista``, en C, haríamos::

    include <stdio.h>

    void main(int argc, char *argv[]) {
        char * lista[] = {"hola", "mundo", "cruel"};
        int i, n = sizeof(l)/sizeof(char *);
        for (i=0; i<n; i++) {
            puts(l[i]);
            }
        }

en Python, sería::

    lista = ("hola", "mundo", "cruel")
    for s in lista:
        print s

El resultado es el mismo en los dos casos, pero la legibilidad es mucho
mayor en el segundo. No hay ni cálculo de tamaño, ni comprobaciones
para no superar el límite, ni incremento de variables auxiliares ni, ya
puestos, variables auxiliares. La magia no existe, la operaciones siguen
siendo necesarias, pero se hacen internamente, con más rápidez y menos
posibilidad de error [#]_.

Las Funciones pueden devolver más de resultado
----------------------------------------------------------------------------

En otros lenguajes, las funciones solo pueden devolver un único
resultado. En python, gracias al empaquetado y desempaquetado automático
de tuplas, las funciones pueden devolver más de una variable. Veamos un
ejemplo::

    def division_y_resto(dividendo, divisor):
        return dividendo // divisor, dividendo % divisor

    cociente, resto = division_y_resto(47, 9)
    print 'cociente:', cociente
    print 'resto:', resto

Este pequeño programa nos informa de que 47 dividido por 49 da cinco,
con resto dos, o dicho de otra manera, que (9 * 5) + 2 = 47

Las asignaciones pueden encadenarse
----------------------------------------------------------------------------

Gracias a la magia de las tuplas y al empaquetado y desempaquetado
automatico de las mismas, junto con algún que otro truco, las
expresiones siguientes son posibles::

    >>> a = b = c = d = 0

Y significan lo que uno podría esperarse, las variables ``a``, ``b``,
``c`` y ``d`` se inicializan a cero.

También podemos intercambiar los valores de dos variables sin necesidad
de recurrir a variables intermedias::

    >>> a,b = b,a

Las comparaciones también pueden escribirse de forma más legigle que en
otros lenguajes, por ejemplo, para comprobar que la variable ``a`` está
entre cero y cien, podemos expresarlo así::

    >>> if a > 0 and a < 100:
    ...     print 'OK'

o, más legible::

    >>> if 0 < a < 100:
    ...     print 'OK'


No hay necesidad de implementar funciones getters/setters
----------------------------------------------------------------------------

En algunos lenguajes, especialmente C++ y derivados, se considera una
mala práctica el acceder directamente a los atributos de una clase. Se
recomienda siempre definir, para cada atributo, dos funciones: una se
usará para asignar valores al atributo (*setter*) y la otra para leer el
valor del atributo (*getter*).  La mayor parte de los IDE permiten
incluso generar automáticamente estos métodos para simplificar el
trabajo al programador.

El razonamiento detrás de esta práctica es que no podemos predecir, a
medida que el programa crece o evoluciona, si un atributo no podrá
convertirse en algo más complejo; algo que requiera determinados
cálculos o que produzca efectos paralelos al ser leido o modificado. En
este caso, habría que buscar las referencias al atributo y cambiarlas
por las correspondientes llamadas a métodos, algo que puede convertirse
en una tarea titánica si el código es muy grande. Curándose es salud,
los programadores en estos lenguajes nunca acceden al atributo
directamente, sino que usan siempre los métodos correspondientes.

Supongamos, por ejemplo, que hemos definido una clase para guardar
información de los empleados, y que hemos reservado el atributo edad
para almacenar cuantos años tiene cada empleado. Un ejemplo de esta
clase podría ser::

    class Empleado:
        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def __str__(self):
            return self.nombre

    tyson = Empleado('Neil deGrasse Tyson', 54)

Nuestra clase es un éxito, y se empieza a usar en diferentes partes del
programa; por ejemplo, alguien de recursos humanos, seguramente con
aviesas intenciones, decide escribir una función para saber si un
empleado está cerca de su jubilación::

    def es_jubilable(empl):
        return empl.edad > 65

    es_jubilable(tyson) #--> False

Sin embargo, nuestro diseño tiene un fallo: es complicado mantener el
campo `edad`.  Es mucho más práctico almacenar la fecha de nacimiento:
contamos con más información -podemos felicitar automáticamente al
empleado en su cumpleaños, por ejemplo- y no tenemos que actualizar el
campo edad de todos los empleados cada año. Manos a la obra:

    import datetime

    class Empleado:
        def __init__(self, nombre, f_nacimiento):
            self.nombre = nombre
            self.f_nacimiento = f_nacimiento

        def get_edad(self):
            delta = datetime.date.today() - self.f_nacimiento
            return int(data.days // 365.25)

    tyson = Empleado('Neil deGrasse Tyson', datetime.date(1958, 10, 5))

Sin embargo, esto rompe el código recursos humanos, ya que el atributo edad
ha desaparecido.

Para evitar esto, un programar con un *background* de Java podría haber
previsto este problema, y creado la clase ``Empleado`` con sus correspondientes
*setters* y *getters*::

    class Empleado:
        def __init__(self, nombre, edad):
            self.set_nombre(nombre)
            self.set_edad(edad)

        def __str__(self):
            return self.get_nombre()

        def set_edad(self, edad):
            self._edad = edad

        def get_edad(self):
            return self._edad

        def set_nombre(self, nombre):
            self._nombre = nombre

        def get_nombre(self):
            return self._nombre

    tyson = Empleado('Neil deGrasse Tyson', 54)

El empleado de recursos humanos no habría accedido nunca a la
valiable interna ``_edad``, habría usado los métodos de acceso
correspondientes::

    def es_jubilable(empl):
        return empl.get_edad() > 65

    es_jubilable(tyson) #--> False

Con lo que, al hacer el cambio de edad for fecha de nacimiento, no se
rompe ningún código::

    class Empleado:
        def __init__(self, nombre, f_nacimiento):
            self.set_nombre(nombre)
            self.set_f_nacimiento(f_nacimiento)

        def __str__(self):
            return self.nombre

        def set_edad(self, edad):
            raise ValueError('No se puede asignar la edad; modifique la fecha de nacimiento')

        def get_edad(self):
            delta = datetime.date.today() - self.f_nacimiento
            return int(data.days // 365.25)

        def set_nombre(self, nombre):
            self._nombre = nombre

        def get_nombre(self):
            return self._nombre

        def set_f_nacimiento(self, f_nacimiento):
            self.f_nacimiento = f_nacimiento

        def get_f_nacimiento(self):
            return self.f_nacimiento

    tyson = Empleado('Neil deGrasse Tyson', datetime.date(1958, 10, 5))

El problema es que la clase se nos ha complicado innecesariamente; los
metodos get_nombre, `set_nombre`, `set_f_nacimiento` y `get_f_nacimiento` no
aportan nada. Es verdad que segurmanete el IDE las ha generado automáticamente
por nosotros, pero recuerdese que uno de los principios de diseño de Python
era que es preferible que el código sea fácil de leer, y no es el caso.

La solución "pythonica" pasa por el uso de propiedades, `property`_.
Esta funcion nos permite redefinir como se accede, modifica o borra un
atributo de un objeto, sin que el resto del código sea consciente de
que el atributo al que estaba accediendo ya no es un simple campo. En
el caso anterior, reescribiriamos  la clase `Empleado` así:

.. literalinclude:: ../ejemplos/empleado_05.py
    :language: python
    :lines: 6-25
    :emphasize-lines: 11-18

Las funciones son objetos
----------------------------------------------------------------------------

Las funciones son objetos en si mismo, es decir, que podemos hacer con ellas
cosas que en otros lenguajes serían imposibles. Por ejemplo, podemos tener un
array de funciones, o podemos pasar una función --ojo, no el resultado de una
función, sino la función en si-- como parámetro de otra función. Esto no
sorprenderá en absoluto a aquellos que hayan tenido experiencia con lenguajes
funcionales, pero si a aquellos que sólo estén acostumbrados a lenguajes
imperativos.

.. _property: http://docs.python.org/2/library/functions.html#property

.. rubric:: Footnotes

.. [#] Si perteneces al 99% te extrañará que exista siquiera ese 1%. Hay gente
   para todo.

.. [#] En realidad si se puede, porque en Python se puede hacer casi todo, pero
   es poco pythonico, la sintaxis es confusa y las razones de uso casi siempre
   inexistentes.

.. [#] En C uno de los errores más frecuentes era acceder con un puntero a
   direcciones de memoria posteriores a las que ocupaba una variable,
   provocando todo tipo de fallos. Eran tantos los errores de este tipo que
   incluso recibieron un nombre: *buffer overrun* o desbordamiento de buffer.

