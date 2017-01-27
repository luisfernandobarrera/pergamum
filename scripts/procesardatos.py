import os
import glob
import tablib
import datetime
import pymongo

TYPES = {'txt', 'png', 'wmv', 'rtf', 'pps', 'jpg', 'wma', 'mdi', 'doc', 'pptx', 'pdf', 'xls', 'htm', 'docx', 'gif'}
TEXT_TYPES = ['txt', 'rtf', 'doc', 'pdf', 'htm', 'docx', 'pps', 'pptx','xls']
DATA_TYPES = []
MEDIA_TYPES = ['png', 'wmv', 'jpg', 'gif', 'wma', 'mdi',]

data = tablib.Dataset(headers=[])

archivos = [file for file in glob.glob("articledb/**/*", recursive=True) if os.path.isfile(file)]
nombre_archivo = ["".join(archivo.split('/')[-1].split('.')[0:-1]) for archivo in archivos]
extensiones = [archivo.split('.')[-1].lower() for archivo in archivos]
carpetas = ["/".join(archivo.split('/')[1:-1]) for archivo in archivos]
created = [datetime.datetime.fromtimestamp(os.stat(archivo).st_mtime) for archivo in archivos]

data.append_col(nombre_archivo, header='filename')
data.append_col(extensiones, header='ext')
data.append_col(carpetas, header='folder')
data.append_col(archivos, header='path')
data.append_col(archivos, header='created')

data.headers = ['filename', 'ext', 'folder', 'path', 'created']


def write_to_csv(data):
    with open("archivos.csv", "w") as db:
        db.write(data.csv)


def save_in_mongo(data):
    with pymongo.MongoClient('mongodb://localhost:27017/') as db:
        archivo = db.archivo
        archivo.drop_collection('articulos')
        articulos = archivo.articulos
        for articulo in data.dict:
            articulos.insert(articulo)


if __name__ == "__main__":
    save_in_mongo(data)
    with pymongo.MongoClient('mongodb://localhost:27017/') as db:
        print(db.archivo.articulos.count())
