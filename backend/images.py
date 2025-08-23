import os

def get_image_paths(root_directory: str) -> list[str]:
    """
    Recorre los subdirectorios de una ruta dada y retorna una lista 
    con las rutas de todos los archivos de imagen encontrados.
    """
    all_image_paths = []
    
    # os.walk() recorre todos los directorios y subdirectorios.
    for root, dirs, files in os.walk(root_directory):
        # Para cada archivo en el directorio actual
        for filename in files:
            # Construye la ruta completa al archivo usando os.path.join
            full_path = os.path.join(root, filename)
            
            # Normaliza la ruta para usar barras diagonales (/) como en tu ejemplo
            normalized_path = full_path.replace(os.sep, '/')
            
            all_image_paths.append(normalized_path)
            
    return all_image_paths

# --- Ejemplo de Uso ---
if __name__ == "__main__":
    # Define el directorio base donde están las carpetas de imágenes
    # Puedes cambiar esta ruta a la de tu proyecto.
    base_dir = "C:/Users/jerem/Documents/py/full-stack-e-commerce/src/images/"
    
    # Llama a la función para obtener todas las rutas
    product_image_paths = get_image_paths(base_dir)

    # Imprime las rutas para verificar
    for path in product_image_paths:
        print(path)

    print(f"\nSe encontraron {len(product_image_paths)} rutas de imágenes.")