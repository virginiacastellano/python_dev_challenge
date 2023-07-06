from products import ProductManager

def main():
    product_manager = ProductManager()

    # Solicitar al usuario el nombre del producto y la cantidad deseada
    product_name = input("Ingrese el nombre del producto: ")
    quantity = input("Ingrese la cantidad deseada: ")

    # Validar que la cantidad sea un número entero positivo
    if not quantity.isdigit() or int(quantity) <= 0:
        print("La cantidad ingresada no es válida. Por favor, ingrese un número entero positivo.")
        return

    quantity = int(quantity)

    # Verificar si el producto está disponible en la cantidad solicitada y mostrar el resultado
    if product_manager.is_product_available(product_name, quantity):
        print(f"El producto '{product_name}' está disponible en la cantidad solicitada.")
    else:
        print(f"El producto '{product_name}' no está disponible en la cantidad solicitada.")

if __name__ == "__main__":
    main()
