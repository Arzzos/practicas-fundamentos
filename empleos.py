# ============================================================
# SISTEMA DE EMPLEADOS
# ============================================================
# Este programa hace tres cosas, en este orden:
#   1. Muestra un titulo en pantalla.
#   2. Pide cuatro datos del empleado por teclado.
#   3. Muestra esos datos ordenados en pantalla.
#
# COMO LEER ESTE ARCHIVO:
#   Todo lo que empieza con el simbolo numeral (#) es un
#   COMENTARIO: Python lo ignora al ejecutar. Sirve solo para
#   que las personas entiendan o dejar notas / asignaciones a otras personas.
#   El codigo "real" es lo que NO tiene # delante.
# ============================================================


# ------------------------------------------------------------
# PASO 1: MOSTRAR EL TITULO
# ------------------------------------------------------------
# print(...)  -> Funcion que ya trae Python. Muestra en la
#                pantalla lo que le pasemos entre parentesis.
#
# f''' ... ''' -> Es un "f-string" (texto formateado).
#    - La letra f delante de las comillas significa "formatted".
#      Sirve para poder INSERTAR variables dentro del texto
#      escribiendo su nombre entre llaves: {variable}.
#      Si quitas la f, Python escribiria literalmente la palabra
#      "variable" en vez de su valor. En este print en concreto
#      no hay variables, pero se deja la f por costumbre y para
#      que el estilo sea igual al del print final (donde SI es
#      obligatoria).
#    - Las TRES comillas (''' o """) permiten escribir un texto
#      que ocupa VARIAS lineas tal cual lo ves, sin tener que
#      pegar todo en una sola linea con \n.
#
print(f'''====================
Sistema de empleados
====================''')
# Los signos "=" son solo decoracion visual del titulo.


# ------------------------------------------------------------
# PASO 2: PEDIR LOS DATOS
# ------------------------------------------------------------
# input('texto') -> Muestra 'texto' en pantalla y ESPERA a que
#                   el usuario escriba algo y presione Enter.
#                   IMPORTANTE: input() SIEMPRE devuelve TEXTO
#                   (string), aunque el usuario escriba numeros.
#
# POR QUE HAY UN ESPACIO AL FINAL DEL TEXTO DEL INPUT?
#   input('Nombre del empleado: ')
#                               ^ ese espacio
#   Es puramente estetico. Si no lo pusieras, lo que el usuario
#   escribe quedaria pegado a los dos puntos:
#       Nombre del empleado:Juan
#   Con el espacio queda separado y se lee mejor:
#       Nombre del empleado: Juan
#   Ese espacio forma parte del texto que se muestra, no afecta
#   al valor que se guarda en la variable.
#
nombre_empleado = input('Nombre del empleado: ')
# 'nombre_empleado' es una VARIABLE: una caja con nombre donde
# guardamos un valor para usarlo mas tarde.
# El simbolo = es ASIGNACION ("guarda esto en la caja").
# NO significa "igual que" (para comparar se usa ==, lo veras
# mas abajo).

edad_del_empleado = int(input('Edad del empleado: '))
# Aqui hay dos funciones anidadas (una dentro de otra).
# Se ejecuta primero la de dentro:
#   1. input(...) -> pide la edad y la devuelve como TEXTO.
#   2. int(...)   -> convierte ese texto en un NUMERO ENTERO
#                    (sin decimales) para poder hacer cuentas
#                    con el mas adelante.
# Si el usuario escribe letras en vez de numeros, Python lanza
# un error (ValueError) y el programa se detiene.

salario = float(input('Ingrese el salario del empleado: '))
# float(...) convierte el texto en un NUMERO DECIMAL (con
# punto/coma), por ejemplo 1500.50. Se usa float y no int
# porque un salario puede tener centavos.

es_jefe_de_departamento = input('Es jefe de departamento (Si/No)? ')
# Aqui NO convertimos nada: guardamos el texto tal cual lo
# escriba el usuario. Lo convertiremos a True/False abajo.
# El espacio despues del "?" al final del texto es por la misma
# razon estetica explicada arriba.


# ------------------------------------------------------------
# PASO 3: CONVERTIR LA RESPUESTA A UN VALOR LOGICO (True/False)
# ------------------------------------------------------------
# El usuario puede escribir "Si", "si", "SI", "No", "no", etc.
# Necesitamos que el programa entienda todas esas variantes como
# un booleano (True = verdadero / False = falso).
#
# EXPLICACION DE CADA METODO, DE IZQUIERDA A DERECHA:
#   .strip()  -> elimina los ESPACIOS que el usuario haya puesto
#                al principio o al final. "  Si  " -> "Si".
#   .lower()  -> convierte TODO el texto a minusculas.
#                "Si" -> "si", "SI" -> "si".
#   == "si"   -> COMPARA: preguntar "esto es igual a 'si'?".
#                Devuelve True si coincide, False si no.
#
# OJO: el simbolo == (dos iguales) es COMPARAR.
#       el simbolo =  (uno solo) es GUARDAR.
#
es_jefe_de_departamento = es_jefe_de_departamento.strip().lower() == "si"


# ------------------------------------------------------------
# PASO 4: MOSTRAR LOS DATOS DEL EMPLEADO
# ------------------------------------------------------------
# Aqui el f-string SI es obligatorio: cada {variable} sera
# reemplazado por el valor real que tenga esa variable.
# Si quitaramos la f, la pantalla mostraria literalmente
# "{nombre_empleado}" en vez del nombre del empleado.
#
print(f'''===== DATOS DEL EMPLEADO =====
Nombre: {nombre_empleado}
Edad: {edad_del_empleado}
Salario: {salario}
Es jefe de departamento? {es_jefe_de_departamento}''')