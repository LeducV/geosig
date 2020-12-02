""" Test file.

 Copyright 2020 Vincent Leduc

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
    http: // www.apache.org / licenses / LICENSE - 2.0

"""
import numpy as np
import geosig.Geometry as geom
from geosig import Transform

if __name__ == "__main__":

    # gml.toGML("geosig/test.xml", data=1)
    p1 = geom.Point([1, 3])
    p2 = geom.Point([7, 2])
    p3 = geom.Point([2, 3])
    liste = list()
    liste.append(p1)
    liste.append(p2)

    poly1 = geom.Polygon()
    poly1.setCoordinate([p1, p2, p3, p1])
    liste = Transform.Affine2DTransform(liste, 2, 3, 1, 1, 1, 1)
