from discounts import validate_discount_code

def main():
    discount_code = input("Ingrese el código de descuento: ")

    # Validación de entrada inválida
    if not discount_code:
        print("Error: El código de descuento no puede estar vacío.")
        return

    # Otra validación personalizada, como longitud mínima y máxima, caracteres permitidos, etc.
    if len(discount_code) < 5:
        print("Error: El código de descuento debe tener al menos 5 caracteres.")
        return

    if validate_discount_code(discount_code):
        print("El código de descuento es válido.")
    else:
        print("El código de descuento no es válido.")

if __name__ == "__main__":
    main()
