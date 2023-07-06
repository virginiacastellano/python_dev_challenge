from products import is_product_available

def main():
    """
    Función principal para solicitar el nombre del producto y la cantidad deseada al usuario,
    y verificar si el producto está disponible en la cantidad solicitada.
    """
    while True:
        product_name = input("Ingrese el nombre del producto (o 'q' para salir): ")
        if product_name.lower() == "q":
            break

        try:
            quantity = int(input("Ingrese la cantidad deseada: "))

            if is_product_available(product_name, quantity):
                print(f"El producto '{product_name}' está disponible en la cantidad solicitada.")
                break
            else:
                print(f"El producto '{product_name}' no está disponible en la cantidad solicitada. Intente nuevamente.")

        except ValueError:
            print("Error: La cantidad ingresada no es válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
