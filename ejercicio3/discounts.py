_AVAILABLE_DISCOUNT_CODES = ["Primavera2021", "Verano2021", "Navidad2x1", "heladoFrozen"]

def validate_discount_code(discount_code):
    """
    Valida si un código de descuento es válido comparándolo con una lista de códigos vigentes.
    
    Args:
        discount_code (str): El código de descuento ingresado por el cliente.
    
    Returns:
        bool: True si el código de descuento es válido, False de lo contrario.
    """
    discount_code = discount_code.lower()  # Convertir a minúsculas para una comparación sin distinción de mayúsculas
    for code in _AVAILABLE_DISCOUNT_CODES:
        code = code.lower()  # Convertir a minúsculas para una comparación sin distinción de mayúsculas
        diff_count = sum(char1 != char2 for char1, char2 in zip(discount_code, code))
        if diff_count < 3:
            return True
    return False
