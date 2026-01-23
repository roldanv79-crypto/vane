# Proyecto: Simulador de cesta de compra en Python

def simulador_cesta():

    cesta_productos = ["manzana", "pera", "durazno" ]
    cesta_precios = [10, 15, 20]
    

    print(" ¡Bienvenido al Simulador de Cesta de Compra! ")
    print("--------------------------------------------------")

    
    while True:
        
        print("\n MENÚ PRINCIPAL ")
        print("1️⃣. AGREGAR un nuevo elemento ")
        print("2️⃣. MOSTRAR el contenido de la cesta ")
        print("3️⃣. ELIMINAR un elemento ")
        print("4️⃣. CALCULAR el total de la compra ")
        print("5️⃣. RENUNCIAR (Salir) ")
        
        opcion = input("\n Elige una opción (1-5): ")

        # --- OPCIÓN 1: AGREGAR ---
        if opcion == "1":
            producto = input("Nombre del producto: ")
            try:
                precio = float(input(f"Precio de '{producto}': $"))
                cesta_productos.append(producto)
                cesta_precios.append(precio)
                print(f" ¡{producto} agregado correctamente!")
            except ValueError:
                print(" Error: Por favor ingresa un precio numérico válido.")

        # --- OPCIÓN 2: MOSTRAR ---
        elif opcion == "2":
            print("\n --- TU CESTA DE COMPRA --- ")
            if len(cesta_productos) == 0:
                print("   (La cesta está vacía )")
            else:
                
                for prod, prec in zip(cesta_productos, cesta_precios):
                    print(f"   • {prod}: ${prec:.2f}") 
            print("------------------------------")

        # --- OPCIÓN 3: ELIMINAR ---
        elif opcion == "3":
            producto_a_borrar = input("¿Qué producto deseas eliminar?: ")
            
            if producto_a_borrar in cesta_productos:
                
                indice = cesta_productos.index(producto_a_borrar)
                cesta_productos.pop(indice)
                cesta_precios.pop(indice)
                print(f" {producto_a_borrar} eliminado de la cesta.")
            else:
                print(f" El producto '{producto_a_borrar}' no está en tu cesta.")

        # --- OPCIÓN 4: CALCULAR TOTAL ---
        elif opcion == "4":
            total = sum(cesta_precios)
            print(f"\n El TOTAL a pagar es: ${total:.2f}")
            print("--------------------------------")

        # --- OPCIÓN 5: SALIR ---
        elif opcion == "5":
            print("\n ¡Gracias por tu compra! Que tengas buen día.")
            break 

        # --- OPCIÓN INVÁLIDA ---
        else:
            print(" Opción no válida. Por favor escribe un número del 1 al 5.")


if __name__ == "__main__":
    simulador_cesta()


# Tarea de Programación Interactiva

def jugar():
    print("--- 🌲 BIENVENIDO AL BOSQUE SUSURRANTE 🌲 ---")
    print("Caminas por un sendero oscuro y encuentras dos objetos en el suelo.")
    
    # Nivel 1: El Inicio
    decision1 = input("¿Prefieres recoger el FÓSFORO o la LINTERNA?: ").lower().strip()

    # --- CAMINO DEL FÓSFORO ---
    if decision1 == "fósforo" or decision1 == "fosforo":
        print("\nCoges el fósforo y lo enciendes 🔥. El bosque se ilumina un segundo... ¡y ves un oso grizzly!")
        
        # Nivel 2 (Fósforo)
        decision2 = input("¿Quieres CORRER o ESCONDERTE detrás de un árbol?: ").lower().strip()
        
        if decision2 == "correr":
            print("\nCorres tan rápido que llegas a un barranco.")
            # Nivel 3 (Fósforo -> Correr) - 3 OPCIONES
            decision3 = input("¿Prefieres SALTAR al río, BUSCAR un puente o VOLVER atrás?: ").lower().strip()
            
            if decision3 == "saltar":
                print("\n🌊 ¡El agua está helada pero te lleva a una aldea segura! GANASTE.")
            elif decision3 == "buscar":
                print("\n🌉 Encuentras un puente de cuerda viejo... ¡y se rompe! FIN DEL JUEGO.")
            elif decision3 == "volver":
                print("\n🐻 El oso te estaba esperando. Mala idea. FIN DEL JUEGO.")
            else:
                print("Te quedaste congelado por la duda y el oso te atrapó. Opción no válida.")

        elif decision2 == "esconderte":
            print("\nTe ocultas tras un roble centenario. El oso se aleja, pero ves un brillo en las raíces.")
            # Nivel 4 (Fósforo -> Esconderte)
            decision4 = input("¿Quieres CAVAR en la tierra o SEGUIR al oso en silencio?: ").lower().strip()
            
            if decision4 == "cavar":
                print("\n💎 ¡Has encontrado un tesoro antiguo enterrado! GANASTE.")
            elif decision4 == "seguir":
                print("\n🐾 El oso te lleva a su cueva... y no eres invitado a cenar. FIN DEL JUEGO.")
            else:
                print("El miedo te paralizó. Opción no válida.")
        else:
            print("Esa no era una opción. El oso no tiene tanta paciencia.")

    # --- CAMINO DE LA LINTERNA ---
    elif decision1 == "linterna":
        print("\nEnciendes la linterna 💡 y ves un camino iluminado. De pronto, oyes un ruido entre los arbustos.")
        
        # Nivel 5 (Linterna) - 3 OPCIONES
        decision5 = input("¿Quieres SEGUIR el camino, BUSCAR el ruido o APAGAR la luz?: ").lower().strip()
        
        if decision5 == "seguir":
            print("\nLlegas a una cabaña acogedora con humo en la chimenea.")
            # Nivel 6 (Linterna -> Seguir)
            decision6 = input("¿Prefieres ENTRAR, RODEAR la casa o LLAMAR a la puerta?: ").lower().strip()
            
            if decision6 == "entrar":
                print("\n🏠 Es la casa de un mago que te ofrece chocolate caliente. GANASTE.")
            elif decision6 == "rodear":
                print("\n🕸️ Caes en una trampa para lobos en el jardín trasero. FIN DEL JUEGO.")
            elif decision6 == "llamar":
                print("\n🚪 Nadie responde, pero un duende te roba la linterna y te pierdes. FIN DEL JUEGO.")
            else:
                print("Te quedaste fuera bajo la lluvia. Opción no válida.")

        elif decision5 == "buscar":
            print("\n¡Es un pequeño robot perdido que proyecta un mapa holográfico!")
            # Nivel 7 (Linterna -> Buscar) - 3 OPCIONES
            decision7 = input("¿Quieres REPARARLO, DEJARLO o PEDIRLE ayuda?: ").lower().strip()
            
            if decision7 == "repararlo":
                print("\n🤖 El robot se vuelve tu guía y te saca del bosque. GANASTE.")
            elif decision7 == "dejarlo":
                print("\n🌑 Te quedas solo y las baterías de tu linterna se agotan. FIN DEL JUEGO.")
            elif decision7 == "pedirle":
                print("\n⚡ El robot se asusta y lanza una descarga eléctrica. FIN DEL JUEGO.")
            else:
                print("El robot se autodestruye por tu indecisión.")
                
        elif decision5 == "apagar":
            print("\nTe quedas a oscuras... y una voz susurra: 'Gracias por no molestar'. FIN DEL JUEGO.")
        else:
            print("El bosque no perdona a los indecisos.")

    # Manejo de respuesta inválida inicial
    else:
        print("⚠️ Opción no válida. Debes elegir FÓSFORO o LINTERNA para comenzar.")

# Ejecutar el juego
jugar()


