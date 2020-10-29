""" Package pour l'utilisation de données géospatiale.

Contenue :

    geosig.toGML : Module comportant les fonctions permettants d'écrire un fichier xml - geosig.

 Copyright 2020 Vincent Leduc

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http: // www.apache.org / licenses / LICENSE - 2.0
"""

# Vérification que les librairies requisent sont installées.
try:
    import lxml.etree
except ImportError:
    print("La librairie gmt requiert lxml")
    print("Pour l'installer, utiliser la commande:")
    print("     pip install lxml")
    raise
