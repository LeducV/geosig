""" Module use for creating a xml-gml document object.

 Copyright 2020 Vincent Leduc

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
    http: // www.apache.org / licenses / LICENSE - 2.0

"""

# Importation de librairie.
import lxml.etree as et


def toGML(filepath, data):
    # Écrit le fichier xml de résultat sous format geosig.
    #
    # Paramètres:
    #   filepath: Le lien vers le fichier vidéo.
    #   data: Données à écrire.
    if data is None:
        print("Aucune données enregirstrés")
        return

    # Création du namespace geosig.
    XHTML_NAMESPACE = "http://www.opengis.net/gml"
    XHTML = "{%s}" % XHTML_NAMESPACE
    NSMAP = {"geosig": XHTML_NAMESPACE}
    root = et.Element(XHTML + "FeatureCollection", nsmap=NSMAP)
    # Création du bbox.
    bbox = et.SubElement(root, XHTML + "boundedBy")
    box = et.SubElement(bbox, XHTML + "Box")
    coord_bbox = et.SubElement(box,  XHTML + "coordinates", decimal='.', cs=',', ts=' ').text = "0 0 300 300"

    # Création de la structure de piétons.
    feature_member = et.SubElement(root, XHTML + "featureMember")
    pieton = et.SubElement(feature_member, "Pieton")
    et.SubElement(pieton, "id").text = "1"
    et.SubElement(pieton, "epoque").text = "1"
    coord_img = et.SubElement(pieton, "coord_image")
    multi_img = et.SubElement(coord_img,  XHTML + "MultiPoint")
    member_img = et.SubElement(multi_img,  XHTML + "pointMember")
    point_img = et.SubElement(member_img,  XHTML + "Point")
    et.SubElement(point_img, XHTML + "pos").text = "1 1"
    coord_trn = et.SubElement(pieton, "coord_terrain")
    multi_trn = et.SubElement(coord_trn,  XHTML + "MultiPoint")
    member_trn = et.SubElement(multi_trn,  XHTML + "pointMember")
    point_trn = et.SubElement(member_trn,  XHTML + "Point")
    et.SubElement(point_trn, XHTML + "pos").text = "2 4 0"

    # Sauvegarde du fichier.

    tree = et.ElementTree(root)
    tree.write(filepath, encoding="UTF-8", xml_declaration=True, method="xml", pretty_print=True, )
