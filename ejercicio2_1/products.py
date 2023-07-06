import pandas as pd

class ProductManager:
    def __init__(self):
        # Crear el DataFrame con la información de los productos y su cantidad
        self.product_df = pd.DataFrame({
            "product_name": ["Chocolate", "Granizado", "Limon", "Dulce de Leche"],
            "quantity": [3, 10, 0, 5]
        })

    def is_product_available(self, product_name, quantity):
        """
        Verifica si un producto está disponible en la cantidad solicitada.

        Args:
            product_name (str): Nombre del producto.
            quantity (int): Cantidad deseada.

        Returns:
            bool: True si el producto está disponible en la cantidad solicitada, False en caso contrario.
        """
        # Buscar el producto en el DataFrame (ignorando mayúsculas y minúsculas)
        product_data = self.product_df[self.product_df["product_name"].str.lower() == product_name.lower()]

        # Verificar si el producto está disponible en la cantidad solicitada
        if product_data.empty:
            return False
        available_quantity = product_data.iloc[0]["quantity"]
        return available_quantity >= quantity
