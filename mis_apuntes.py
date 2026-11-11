
# Herramienta print()
print("jmmm")
#concatenar


# Herramienta type()

# Herramienta input()

# Variables

# Tipado dinamico = define el tipo de dato de una variable automaticamente, segun su contenido


# OPERACIONES
numero_uno = 10
numero_dos = 3

# Suma  +
suma = numero_uno + numero_dos
print("Resultado Suma: ", suma)

# Resta  -
resta = numero_uno - numero_dos
print("Resultado Resta: ", resta)

# Multiplicacion  *
multiplicacion = numero_uno - numero_dos
print("Resultado Multiplicacion: ", multiplicacion)


# Division 1 (normal = con decimal)  /

# Division 2 (entera = redondea abajo)  //

# Modulo o Residuo de Division  %
division_modulo = numero_uno % numero_dos
print("Resultado division Modulo: ", division_modulo)

# Potenciación  **
potencia = numero_uno ** numero_dos
print("Resultado Potenciacion: ", potencia)

# JERARQUIA DE OPERACIONES
# En este orden: primero (* o /) y luego (+ o -) y de izq a derecha lo que este primero
jo=20-10*5/2+4*2
jo=20-50/2+4*2
jo=20-25+4*2
jo=20-25+8
jo=-5+8
jo=3

# cuando aplica, se resulven primero los parentesis, con las reglas de jerarquia
cp=(20-10)*5/(2+4*2)
cp=10*5/10
cp=50/10
cp=5

#ej notas
notas= (5.0+3.0+2.0+4.0)/4
notas= 14/4
notas= 3.5



# ERRORES
# ValueError: Ocurre cuando una función recibe un argumento que tiene el tipo de dato correcto, pero un valor inválido, osea que Python entiende qué tipo de información se le pasa, pero ese contenido específico no es válido para la operación que se intenta realizar.
# TypeError: Ocurre cuando se intenta realizar una operación con un objeto que no es del tipo de dato adecuado para esa acción. A diferencia del ValueError (donde el tipo está bien pero el contenido está mal), en el TypeError el tipo de dato está completamente equivocado para lo que se quiere hacer.
