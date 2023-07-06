from weather import GeoAPI

def main():
    """
    Programa principal que verifica si hace calor en Pehuajó utilizando la clase GeoAPI.
    """
    if GeoAPI.is_hot_in_pehuajo():
        print("Hace calor en Pehuajó.")
    else:
        print("No hace calor en Pehuajó.")

if __name__ == "__main__":
    main()
