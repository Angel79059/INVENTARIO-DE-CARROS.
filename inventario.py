bienvenida = """ 
                Bienvenido a este inventario de modelos de autos. 
                Tenemos en exhibición los siguientes modelos: 
                
                """

inventario = ['Porshe 911', 'Chevrolet Camaro 2024', 'Ford GT 40', 'Ferrari LaFerrari', 'Lamborghini Veneno']
fallos_modelos = {modelo: [] for modelo in inventario} 

opciones = """
              Dispones de las siguientes opciones a realizar en el inventario:
              1) Ingresa el número 1 para añadir un nuevo modelo.
              2) Ingresa el número 2 para eliminar un modelo.
              3) Ingresa el número 3 para listar el inventario.
              4) Ingresa el número 4 para obtener un resumen de los fallos en los modelos.
              5) Ingresa el número 5 para salir del programa. 
           """
              
opcion_no_valida = """
                  Ingresaste una opción no válida. 
                  Asegúrate de elegir una opción válida.
                  """

print(bienvenida)
print(inventario)

while True: 
    
    comandos = input(opciones)

    if comandos == '1':
        modelo = input('Agrega un nuevo modelo.')
        inventario.append(modelo)
        print('Modelo agregado.')

    elif comandos == '2':
        eliminar_modelo = input('Introduce el nombre del modelo a borrar:')
        if eliminar_modelo in inventario:
         inventario.remove(eliminar_modelo)
         print('Modelo eliminado.')
        else: 
            print('Modelo no encontrado.')

    elif comandos == '3':
        print('Inventario de modelos:', inventario)

    elif comandos =='4':
           
        print("\nResumen de fallos de los modelos en exhibición:")
        for modelo, fallos in fallos_modelos.items():
            if fallos:
                print(f"- {modelo}: {', '.join(fallos)}")
            else:
                print(f"- {modelo}: No se han registrado fallos.")

        agregar_fallo = input("\n¿Deseas registrar un fallo en algún modelo? (sí/no): ").strip().lower()
        if agregar_fallo == "sí":
            modelo_fallo = input("Ingresa el nombre del modelo: ")
            if modelo_fallo in fallos_modelos:
                nuevo_fallo = input("Describe el fallo: ")
                fallos_modelos[modelo_fallo].append(nuevo_fallo)
                print(f"Fallo agregado al modelo {modelo_fallo}.")
            else:
                print("El modelo no está en el inventario.")
                break
    elif comandos == '5':
        print('Salir del inventario.')
        break
    else: 
       print(opcion_no_valida)
       
