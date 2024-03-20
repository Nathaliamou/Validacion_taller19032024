# Funcionalidad del Código SQL

## Bloque A: Declaración de Variables
'''
- Variables creadas:
    - numero_niños: Almacena el número de niños que ingresarán al parque.
    - numero_adultos: Almacena el número de adultos que ingresarán al parque.
    - fruta_id: Identificador de la fruta.

## Bloque B: Funciones de Bienvenida y Cantidad de Personas

- Función: bienvenida()
    - Descripción: Imprime un mensaje de bienvenida al parque.

- Función: ingresar_cantidad_personas()
    - Descripción: Permite al usuario ingresar la cantidad de niños y adultos que ingresarán al parque mediante entrada estándar.

## Bloque C: Ingreso de Datos de Niños

- Función: ingresar_datos_niños()
    - Descripción: Permite al usuario ingresar los datos de cada niño que ingresará al parque, incluyendo su nombre, si compra almuerzo y la cantidad de almuerzos que compra.

## Bloque D: Cálculo del Valor Total

- Función: calcular_valor_total()
    - Descripción: Calcula el valor total de la compra, sumando el costo total de los almuerzos de los niños y el costo total de los almuerzos de los adultos.

## Bloque E: Mostrar Total de la Compra y Mensaje de Despedida

- Función: mostrar_total_compra()
    - Descripción: Muestra el valor total de la compra en la consola.

- Función: mostrar_mensaje_despedida()
    - Descripción: Imprime un mensaje de despedida al finalizar la interacción con el programa.

## Entrada y Salida de Datos

- Datos de Entrada:
    - Cantidad de niños y adultos que ingresarán al parque.
    - Nombre de cada niño.
    - Opción de compra de almuerzo para cada niño.
    - Cantidad de almuerzos comprados por cada niño.

- Datos de Salida:
    - Valor total de la compra.

'''

class Menu:
     # Parte A: Declaración de variables
    def __init__(self):
        self.numero_niños = 0  # Asignación: inicializa el número de niños en 0
        self.numero_adultos = 0  # Asignación: inicializa el número de adultos en 0
        self.niños = []  # Asignación: crea una lista vacía para almacenar datos de niños
        self.adultos = []  # Asignación: crea una lista vacía para almacenar datos de adultos
        self.personas = {}  # Asignación: crea un diccionario vacío para almacenar todos los datos de las personas
  # Función bienvenida
    def bienvenida(self):
        print("Bienvenido al Parque Los Deseos de los Niños.")
  # Función para ingresar la cantidad de personas
    def ingresar_cantidad_personas(self):
        self.numero_niños = int(input("Ingrese la cantidad de niños que entrarán al parque: "))
        self.numero_adultos = int(input("Ingrese la cantidad de adultos que entrarán al parque: "))

    def ingresar_datos_niños(self):
        for i in range(self.numero_niños):
            print(f"\nDatos del niño #{i+1}:")
            nombre = input("Ingrese el nombre del niño(a): ")
            compra_almuerzo = input("¿Compra almuerzo? (s/n): ")
            cantidad_almuerzos = 0
            valor_total_compra = 0
            if compra_almuerzo.lower() == 's':
                cantidad_almuerzos = int(input("Ingrese cuántos almuerzos compra: "))
                valor_total_compra += cantidad_almuerzos * 5  # Suponiendo que el almuerzo de niño cuesta $5
            self.niños.append({
                'nombre': nombre,
                'compra_almuerzo': compra_almuerzo,
                'cantidad_almuerzos': cantidad_almuerzos
            })

    def calcular_valor_total(self):
        total_niños = sum(niño['cantidad_almuerzos'] for niño in self.niños)
        total_adultos = self.numero_adultos * 10  # Suponiendo que el almuerzo de adulto cuesta $10
        return total_niños + total_adultos

    def mostrar_total_compra(self):
        valor_total = self.calcular_valor_total()
        print(f"El valor total de la compra es: ${valor_total}")

    def mostrar_mensaje_despedida(self):
        print("Muchas gracias por confiar en nosotros. ¡Que disfruten y los esperamos nuevamente!")

if __name__ == "__main__":
    menu = Menu()
    menu.bienvenida()
    menu.ingresar_cantidad_personas()
    menu.ingresar_datos_niños()

    opcion = input("\n¿Desea conocer el total de la compra? (s/n): ")
    if opcion.lower() == 's':
        menu.mostrar_total_compra()

    menu.mostrar_mensaje_despedida()
