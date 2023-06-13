from pathlib import Path

# Renombrar nombre de carpeta
#path = Path('test')
#path.rename('nuevo_test')

# Renombrar archivo dentro de una carpeta
#path = Path('nuevo_test/gastos.txt')
#nuevoNombrePath = path.with_name('gastos-diciembre.txt')
#path.rename(nuevoNombrePath)

#Obtener path de los subdirectorios inmediatos
# carpeta = Path('2023')
# for path in list(carpeta.iterdir()):
#     print(path)

# Obtener path de todos los subdirectorios
# carpeta = Path('./nuevo_test')
#
# # paths = carpeta.glob('**/*')
# # for path in paths:
# #     print(path)
# paths = carpeta.glob('**/*')
#
# for path in paths:
#      if path.is_file():
#          print(path)
#      else:
#          print('No hay archivo')


folder = Path('extensiones')

# Pasar de txt a csv
# for path in list(folder.iterdir()):
#     print(path)
#     if path.suffix == '.txt':
#         nuevoNombreExtension = path.with_suffix('.csv')
#         path.rename(nuevoNombreExtension)

# Pasar de csv a txt
for path in folder.glob('**/*.csv'):
    print(path)
    nuevoNombreExtension = path.with_suffix('.txt')
    path.rename((nuevoNombreExtension))