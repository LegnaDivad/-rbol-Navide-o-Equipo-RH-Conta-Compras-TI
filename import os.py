import os

def rename_images(folder_path):
    # Extensiones válidas
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    
    # Obtener lista de archivos en la carpeta
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(valid_extensions)]
    
    # Ordenar archivos alfabéticamente (opcional)
    files.sort()
    
    # Renombrar archivos
    for index, filename in enumerate(files, start=1):
        old_path = os.path.join(folder_path, filename)
        new_name = f"{index}.jpg"  # Puedes cambiar el formato aquí
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renombrado: {filename} -> {new_name}")

# Ruta de la carpeta con imágenes
folder = "images"  # Cambia esto a tu ruta
rename_images(folder)
