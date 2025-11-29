import os
import shutil

downloads_folder = f"{__file__}".replace("Diretorio do codigo", "Diretorio da pasta downloads")

for file in os.listdir(downloads_folder):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]
    
    folder_organizer = f"{downloads_folder}/{file_extension}"
    
    if not os.path.isdir(folder_organizer):
        os.mkdir(folder_organizer)
    
    shutil.move(f"{downloads_folder}/{file}", f"{folder_organizer}/{file}")