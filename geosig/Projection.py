""" Module for projection algorithm and visualisation.

 Copyright 2020 Vincent Leduc

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
    http: // www.apache.org / licenses / LICENSE - 2.0

"""
import matplotlib.pyplot as plt


class Map(object):
    fig, ax = plt.subplots()
    geometry = []

    def Add(self, geometry):
        if not isinstance(array, collections.Iterable):
            self.geometry.append(geometry)
        for geom in geometry.getCoordinate():
            self.geometry.append(geom)

    def Show(self):
        plt.show()
