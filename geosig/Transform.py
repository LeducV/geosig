""" Module to transform Geometry object.

 Copyright 2020 Vincent Leduc

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
    http: // www.apache.org / licenses / LICENSE - 2.0

"""
import numpy as np
import geosig.Geometry as geom


def Affine2DTransform(collection, tx, ty, sx, sy, kx, ky):
    """
    Apply an affine transformation on 2d geometry.

    :param collection: List of 2d geometry.
    :param tx: Translation on x axis.
    :param ty: Translation on y axis.
    :param sx: Shear on x axis.
    :param sy: Shear on y axis.
    :param kx: Scale on x axis.
    :param ky: Scale on y axis.
    :return: : List of transformed 2d geometry.
    """
    newCollection = list()
    count = 0
    for geometry in collection:
        if isinstance(geometry, geom.Point):
            xy = geometry.getCoordinate()
            t = np.array([[tx], [ty]])
            a = np.array([[1+kx, sx], [sy, 1+ky]])
            xy = a.dot(xy) + t
            newCollection.append(geom.Point(xy))
        if isinstance(geometry, geom.Polygon):
            pointPolygon = list()
            for point in geometry:
                pointPolygon.append(Affine2DTransform(point, tx, ty, sx, sy, kx, ky))
        count += 1
    return newCollection
