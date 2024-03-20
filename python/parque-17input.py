class Parque:
    def __init__(self):
        self.niños = []
        self.id_auto_incremental = 1

    def registrar_niño(self):
        print("\nRegistro de Niño(a):")
        nombre = input("1. Nombre del niño(a): ")
        apellido = input("2. Apellido del niño(a): ")
        estatura = float(input("3. Estatura del niño(a) en cms (mínimo 125 cms): "))
        if estatura < 125:
            print("Lo sentimos, la estatura mínima para montarse en los juegos es de 125 cms.")
            return

        atraccion = input("4. Nombre de la atracción: ")
        veces_montarse = int(input("5. Cantidad de veces que quiere montarse: "))
        responsable = input("6. Nombre del mayor de edad responsable: ")
        telefono_responsable = input("7. Número de teléfono del responsable: ")
        eps = input("8. EPS del niño(a): ")
        tiene_documento = input("9. ¿El adulto trajo el documento de identidad? (Sí/No): ").lower() == "sí"
        monto_ticket = float(input("10. Monto del ticket: "))
        personas_familia = int(input("11. Cantidad de personas que vienen por familia: "))
        almuerzo = input("12. ¿Compra almuerzo? (Sí/No): ").lower() == "sí"
        cantidad_almuerzos = int(input("13. Cantidad de almuerzos: "))
        total_compra = float(input("14. Valor total de la compra: "))

        self.niños.append({
            "id": self.id_auto_incremental,
            "nombre": nombre,
            "apellido": apellido,
            "estatura": estatura,
            "atraccion": atraccion,
            "veces_montarse": veces_montarse,
            "responsable": responsable,
            "telefono_responsable": telefono_responsable,
            "eps": eps,
            "tiene_documento": tiene_documento,
            "monto_ticket": monto_ticket,
            "personas_familia": personas_familia,
            "almuerzo": almuerzo,
            "cantidad_almuerzos": cantidad_almuerzos,
            "total_compra": total_compra
        })

        self.id_auto_incremental += 1

    def menu_principal(self):
        print("\n¡Bienvenido al Parque Los Deseos de los Niños!")
        while True:
            print("\nMenú:")
           
            print("1. Registrar cantidad de adultos")
            print("2. Registrar cantidad de niños (as), menores de 12 años.")
            print("3. Registrar nombre del adulto")
            print("4. Registrar apellido del adulto")
            print("5. Registrar documento de identidad del adulto, (debe mostrarlo sino no puede entrar)")
            print("6. Registrar Niño(a)")
            print("7.ingrese el nombre del niño(a)")
            print("8.ingrese el apellido del niño(a)")
            print("9.ingrese la estatura del niño(a), tener mayor 125 cms para subir a los juegos")
            print("10.ingrese numero tarjeta de identidad del niño(a),(debe mostrarlo sino no puede entrar")
            print("11.ingrese el nombre de la atraccion")
            print("12.ingrese la cantidad de veces que quiere subir")
            print("13.En caso de emergencia: ingrese el nombre del responsable mayor de edad del niño")
            print("14.ingrese el numero de telefono del responsable")
            print("15.ingrese la eps")
            print("16.ingrese el monto del ticket ()")
            print("17.Pago Total-Factura.ingrese cantidad de personas (grupo familiar)")
            print("18.ingrese si compra almuerzo")
            print("19.ingrese cantidad personas que compran almuerzo")
            print("20. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.registrar_niño()
            elif opcion == "2":
                print("\nMuchas gracias por confiar en nosotros. ¡Que disfruten y los esperamos nuevamente!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")


parque = Parque()
parque.menu_principal()
