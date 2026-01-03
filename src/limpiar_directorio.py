import os
import sys

def eliminar_ficheros_cero_bytes(ruta: str) -> None:
    """
    Busca y elimina ficheros con 0 bytes en un directorio y sus subcarpetas.

    :param ruta: Ruta del directorio donde buscar.
    """
    for root, dirs, files in os.walk(ruta):
        for file in files:
            ruta_file = os.path.join(root, file)
            try:
                if os.path.getsize(ruta_file) == 0:
                    os.remove(ruta_file)
                    print(f"Eliminado fichero '{ruta_file}' con 0 bytes")
            except Exception as e:
                print(f"Error al procesar {ruta_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: python {sys.argv[0]} <ruta_directorio>")
        sys.exit(1)

    ruta_directorio = sys.argv[1]
    if not os.path.isdir(ruta_directorio):
        print(f"'{ruta_directorio}' no es un directorio válido")
        sys.exit(2)

    eliminar_ficheros_cero_bytes(ruta_directorio)
