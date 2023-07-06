import pandas as pd

# DataFrame con la información de los productos y su cantidad en stock
_PRODUCT_DF = pd.DataFrame({
    "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
    "quantity": [3, 10, 0, 5]
})

def is_product_available(product_name, quantity):
    """
    Verifica si un producto está disponible en la cantidad solicitada.

    Args:
        product_name (str): Nombre del producto.
        quantity (int): Cantidad deseada.

    Returns:
        bool: True si el producto está disponible en la cantidad solicitada, False en caso contrario.
    """
    product_name_lower = product_name.lower()  # Convertir el nombre del producto a minúsculas
    product_data = _PRODUCT_DF[_PRODUCT_DF["product_name"].str.lower() == product_name_lower]
    if not product_data.empty:
        available_quantity = product_data.iloc[0]["quantity"]
        return available_quantity >= quantity
    return False
