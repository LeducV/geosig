""" Package pour l'utilisation de données géospatiale.

Contenue :

    geosig.toGML : Module comportant les fonctions permettants d'écrire un fichier xml - geosig.

 Copyright 2020 Vincent Leduc

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http: // www.apache.org / licenses / LICENSE - 2.0
"""
name = "geosig"

# Vérification que les librairies requisent sont installées.
try:
    import lxml.etree
except ImportError:
    print("lxml librairy is required")
    print("Please install lxml:")
    print("     pip install lxml")
    raise
try:
    import numpy
except ImportError:
    print("numpy librairy is required")
    print("Please install numpy:")
    print("     pip install numpy")
    raise
