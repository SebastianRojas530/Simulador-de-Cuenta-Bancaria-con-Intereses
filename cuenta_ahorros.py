saldo = 0.0
opcion = 0
tasa_interes = 0.015 

print("=== SIMULADOR DE CUENTA BANCARIA CON INTERESES ===")

while opcion != 5:
    print("\n--- MENÚ ---")
    print("1. Consultar saldo")
    print("2. Consignar dinero")
    print("3. Retirar dinero")
    print("4. Aplicar intereses del mes")
    print("5. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print(f"\nTu saldo actual es: ${saldo:.2f}")

    elif opcion == 2:
        consignacion = float(input("Ingresa el valor a consignar: "))
        if consignacion > 0:
            saldo += consignacion
            print(f"Consignación exitosa. Nuevo saldo: ${saldo:.2f}")
        else:
            print("Valor no válido.")

    elif opcion == 3:
        retiro = float(input("Ingresa el valor a retirar: "))
        if retiro <= 0:
            print("Valor inválido.")
        elif retiro > saldo:
            print("Fondos insuficientes.")
        else:
            saldo -= retiro
            print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")

    elif opcion == 4:
        intereses = saldo * tasa_interes
        saldo += intereses
        print(f"\nIntereses aplicados: ${intereses:.2f}")
        print(f"Nuevo saldo: ${saldo:.2f}")

    elif opcion == 5:
        print("Saliendo del sistema...")

    else:
        print("Opción no válida. Intenta de nuevo.")
