import pandas as pd
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1' #primera versión ":)"
PACKAGE_NAME = 'TablaPeso' 
AUTHOR = 'Gabriela González' 
AUTHOR_EMAIL = 'gon21922@uvg.edu.gt' 
URL = 'https://github.com/JavierMencos/POO_proyecto2.git' #Originalmente creado para ser parte de un proyecto

LICENSE = 'MIT' #Tipo de licencia
DESCRIPTION = 'Archivo csv de tabla de pesos, útil en diversas aplicaciones ' #Descripción corta
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') #Referencia al documento README con una descripción más elaborada
LONG_DESC_TYPE = "text/markdown"


#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
      'pandas'
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)