import os

fichero_dir = 'C:/Users/mpala/Downloads'

with os.scandir(fichero_dir) as ficheros:
    for fichero in ficheros:
        print(fichero.name)
