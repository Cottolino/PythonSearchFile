import glob
import sys

script, stringa = sys.argv
lista_file = []
file = "C:/Program Files/Ampps/www/NodeJsBackup/**/*.js"

for file_name in glob.iglob(file, recursive=True):
    if ((not("node_modules" in file_name))):
        lista_file.append(file_name)
for y in lista_file:
    with open(y) as f:
        if (stringa in f.read()):
            print(y)




