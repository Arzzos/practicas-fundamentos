# =====================================================================
# RECETARIO - VERSION BASICA
# ---------------------------------------------------------------------
# Leyenda de comentarios:
#    TECNICO -> explicacion de funciones y sintaxis.
#    SIMPLE  -> explicacion abstracta de conceptos utilizados.
#
# NOTA SOBRE LOS f-STRINGS (aparecen varias veces en el codigo):
# ---------------------------------------------------------------------
# TECNICO: Un f-string (o "formatted string literal") es una cadena
#    de texto que empieza con la letra f antes de las comillas, por
#    ejemplo: f"Hola {nombre}". Sirve para INSERTAR el valor de una
#    variable dentro del texto usando llaves { }. Antes de existir los
#    f-strings (Python < 3.6) habia que usar .format() o concatenar con
#    +, lo cual era mas largo y mas propenso a errores. Los f-strings
#    son mas legibles, mas rapidos y permiten incluso expresiones como
#    f"{precio * 1.16}".
#
# SIMPLE: Un f-string es como una "plantilla magica" de texto. Si
#    escribes f"Hola {nombre}", Python reemplaza {nombre} por lo que
#    tenga guardada la variable nombre. Es como un hueco en la frase
#    donde metes el dato. La "f" al inicio le dice a Python "ojo, esto
#    no es texto normal, aqui voy a meter variables con { }".
# =====================================================================


# TECNICO: f-string con triple comilla ('''...''' o """...""") permite
#    imprimir texto en varias lineas y ademas interpolar variables. Se
#    usa aqui para decorar visualmente la salida. Como no hay variables
#    dentro de las llaves (no hay llaves), la "f" es opcional en este
#    print.
# SIMPLE: Esto es como poner un letrero grande que dice "Recetario de
#    comida" con rayitas arriba y abajo para que se vea bonito. La "f"
#    aqui no hace nada especial porque no metemos variables, es solo
#    costumbre.
print(f'''===================
Recetario de comida
===================''')


# TECNICO: input() lee una linea desde la entrada estandar y la
#    devuelve como str. Aqui solo pedimos el nombre de la receta; no
#    validamos que este vacio ni que tenga un formato especifico.
# SIMPLE: Le preguntamos al usuario "como se llama tu receta?" y
#    guardamos la respuesta en una cajita llamada nombre_receta.
nombre_receta = input('Ingrese el nombre de la receta: ')


# TECNICO: Se solicita una cadena que se espera este separada por
#    comas. No se procesa con split() ni se valida; se guarda el texto
#    crudo tal cual lo escriba el usuario.
# SIMPLE: Preguntamos "que ingredientes lleva?" y el usuario los
#    escribe separados con comas. Guardamos todo el texto en una cajita
#    llamada ingredientes.
ingredientes = input('Ingrese los ingredientes de la receta (Separados por comas ","): ')


# TECNICO: int(...) convierte la cadena a entero. ESTA es la unica
#    validacion que exite en este programa: si el usuario escribe algo que
#    no es un numero (por ejemplo "diez"), Python lanza ValueError y el
#    programa se detiene abruptamente.
# SIMPLE: Preguntamos "cuantos minutos tarda?" y convertimos lo que
#    escriba en un numero. Si escribe letras en vez de un numero, el
#    programa se "rompe".
tiempo_de_preparacion = int(input('Indique el tiempo de preparacion (min): '))


# TECNICO: Se pide la dificultad como texto libre. NO se valida que el
#    usuario escriba exactamente "Facil", "Medio" o "Dificil"; puede
#    escribir cualquier cosa y se almacenara igual.
# SIMPLE: Preguntamos "es facil, medio o dificil?" y guardamos lo que
#    responda, aunque escriba otra cosa.
dificultad = input('Ingrese la dificultad de preparacion (Facil / Medio / Dificil): ')


# TECNICO: Aqui SI se usa un f-string de verdad, porque el texto tiene
#    llaves { } con nombres de variables dentro. Lo que hace Python es:
#      1) recorre el texto,
#      2) cuando encuentra {nombre_receta}, lo reemplaza por el VALOR
#         de esa variable (por ejemplo "Tacos"),
#      3) cuando encuentra {ingredientes}, lo reemplaza por lo que el
#         usuario haya escrito,
#      4) y asi con cada llave. El resultado final es un unico string
#         ya "rellenado" que es lo que imprime print().
#    Sin la "f" al inicio, Python imprimiria literalmente
#    "{nombre_receta}" en lugar del valor. Por eso la "f" es la clave.
# SIMPLE: Es como armar una tarjeta final. El texto entre comillas es
#    la plantilla. La "f" le dice a Python "por favor, cambia cada { }
#    por lo que tenga guardado esa cajita". Si no pusieramos la "f",
#    saldria la palabra {nombre_receta} escrita tal cual, en vez del
#    nombre real que escribio el usuario.
print(f'''==========================================
Nombre de la receta: {nombre_receta}
Ingredientes: {ingredientes}
Tiempo de preparacion: {tiempo_de_preparacion}
Dificultad de receta {dificultad}
===========================================''')