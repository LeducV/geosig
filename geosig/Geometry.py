""" Module to create Geometry object.

 Copyright 2020 Vincent Leduc

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
    http: // www.apache.org / licenses / LICENSE - 2.0

"""
# Import librairy
import numbers
import math
import numpy as np

# Color code for error message.
color_red = "\033[31m"
color_white = "\033[0m"


class Point(object):
    """
    Point object.

    :method Rotation(self, axis, angle) Perform a rotation around an axis.
    :method getCoordinate(self) Return coordinate as a numpy array.
    :method setCoordinate(self, x, y, z) Set coordinate of point.

    """
    x = None
    y = None
    z = None

    def __init__(self, array):
        self.setCoordinate(array)

    def __abs__(self):
        # Overloading absolute operator.
        try:
            if self.z is None:
                return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
            else:
                return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))
        except Exception:
            raise

    def __add__(self, array):
        # Overloading + operator.
        try:
            if self.z is None:
                if len(array) != 2 or len(array) == 0:
                    raise Exception("Numerical exception")
                x = self.x + array[0]
                y = self.y + array[1]
                return Point([x, y])
            else:
                if len(array) != 3 or len(array) == 0:
                    raise Exception("Numerical exception")
                x = self.x + array[0]
                y = self.y + array[1]
                z = self.z + array[2]
                return Point([x, y, z])
        except Exception:
            print(color_red +
                  "Warning: Must add a vector to a point. [x, y] or [x, y, z] to apply a transformation." +
                  color_white)
            raise

    def __eq__(self, other):
        # Overloading is equal operator.
        try:
            if not isinstance(other, Point):
                raise Exception("Comparison exception.")
            if self.z is None and other.z is None:
                if self.x == other.x and self.y == other.y:
                    return True
                else:
                    return False
            elif self.z is not None and other.z is not None:
                if self.x == other.x and self.y == other.y and self.z == other.z:
                    return True
                else:
                    return False
            else:
                raise ComparisonException
        except Exception:
            print(color_red +
                  "Warning: Must compare a point to a point." +
                  color_white)
            raise
        except ComparisonException:
            print(color_red +
                  "Warning: Must compare a point to a point of the same dimension." +
                  color_white)
            raise

    def __floordiv__(self, array):
        # Overloading floor division operator.
        try:
            if self.z is None:
                if len(array) != 2 or len(array) == 0:
                    raise Exception("Numerical exception")
                x = selx.x // array[0]
                y = selx.y // array[1]
                return Point([x, y])
            else:
                if len(array) != 3 or len(array) == 0:
                    raise Exception("Numerical exception")
                x = self.x // array[0]
                y = self.y // array[1]
                z = self.z // array[2]
                return Point([x, y, z])
        except Exception:
            print(color_red +
                  "Warning: Must divide a vector to a point. [x, y] or [x, y, z] to apply a transformation." +
                  color_white)
            raise

    def __getitem__(self, item):
        # Overloading getitem operator.
        try:
            if item == 0 or item == "x":
                return self.x
            elif item == 1 or item == "y":
                return self.y
            elif item == 2 or item == "z":
                return self.z
            else:
                raise Exception("IndexError")
        except Exception:
            print(color_red +
                  'Warning: Index error, use 0, 1, 2, "x", "y" or "z".' +
                  color_white)
            raise

    def __len__(self):
        # Overloading len()
        try:
            if self.z is None:
                return 2
            else:
                return 3
        except Exception:
            raise

    def __mod__(self, array):
        # Overloading modulo operator.
        try:
            if self.z is None:
                if len(array) != 2 or len(array) == 0:
                    raise Exception("Numerical exception")
                x = selx.x % array[0]
                y = selx.y % array[1]
                return Point([x, y])
            else:
                if len(array) != 3 or len(array) == 0:
                    raise Exception("Numerical exception")
                x = self.x % array[0]
                y = self.y % array[1]
                z = self.z % array[2]
                return Point([x, y, z])
        except Exception:
            print(color_red +
                  "Warning: Must divide a vector to a point. [x, y] or [x, y, z] to apply a transformation." +
                  color_white)
            raise

    def __mul__(self, array):
        # Overloading * operator.
        try:
            if isinstance(array, int):
                if self.z is None:
                    x = selx.x * array
                    y = selx.y * array
                    return Point([x, y])
                else:
                    x = self.x * array
                    y = self.y * array
                    z = self.z * array
                    return Point([x, y, z])
            if isinstance(array, np.ndarray):
                return np.array([[self.x], [self.y], [self.z]]) * array

        except Exception:
            print(color_red +
                  "Warning: Must multiply a vector to a point. [x, y] or [x, y, z] to apply a transformation." +
                  color_white)
            raise

    def __pow__(self, array):
        # Overloading power operator.
        try:
            if self.z is None:
                if len(array) != 2 or len(array) == 0:
                    raise Exception("Numerical exception")
                x = selx.x ** array[0]
                y = selx.y ** array[1]
                return Point([x, y])
            else:
                if len(array) != 3 or len(array) == 0:
                    raise Exception("Numerical exception")
                x = self.x ** array[0]
                y = self.y ** array[1]
                z = self.z ** array[2]
                return Point([x, y, z])
        except Exception:
            print(color_red +
                  "Warning: To use a vector for power operation to a point to apply a transformation." +
                  "Vectoc: [x, y] or [x, y, z]" +
                  color_white)
            raise

    def __str__(self):
        # Defining print string.
        if self.z is None:
            return "[{0}, {1}]".format(self.x, self.y)
        else:
            return "[{0}, {1}, {2}]".format(self.x, self.y, self.z)

    def __sub__(self, array):
        # Overloading - operator.
        try:
            if self.z is None:
                if len(array) != 2 or len(array) == 0:
                    raise Exception("Numerical exception")
                x = self.x - array[0]
                y = self.y - array[1]
                return Point([x, y])
            else:
                if len(array) != 3 or len(array) == 0:
                    raise Exception("Numerical exception")
                x = self.x - array[0]
                y = self.y - array[1]
                z = self.z - array[2]
                return Point([x, y, z])
        except Exception:
            print(color_red +
                  "Warning: Must substract a vector to a point. [x, y] or [x, y, z] to apply a transformation." +
                  color_white)
            raise

    def __truediv__(self, array):
        # Overloading / operator.
        try:
            if self.z is None:
                if len(array) != 2 or len(array) == 0:
                    raise Exception("Numerical exception")
                x = selx.x / array[0]
                y = selx.y / array[1]
                return point(x, y)
            else:
                if len(array) != 3 or len(array) == 0:
                    raise Exception("Numerical exception")
                x = self.x / array[0]
                y = self.y / array[1]
                z = self.z / array[2]
                return Point([x, y, z])
        except Exception:
            print(color_red +
                  "Warning: Must divide a vector to a point. [x, y] or [x, y, z] to apply a transformation." +
                  color_white)
            raise

    def getCoordinate(self):
        """
        Return the coordinate of the point.

        :rtype: np.ndarray

        """
        if self.z is None:
            return [self.x, self.y]
        else:
            return [self.x, self.y, self.z]

    def setCoordinate(self, array):
        """
        Set the coordinate of the point.

        :param array: Array of coordinate.
        """
        x = array[0]
        y = array[1]
        z = None
        if len(array) == 3:
            z = array[2]
        if isinstance(x, np.ndarray):
            x = x[0]
        if isinstance(y, np.ndarray):
            y = y[0]
        if isinstance(z, np.ndarray):
            z = z
        if isinstance(x, numbers.Number):
            self.x = x
        if isinstance(y, numbers.Number):
            self.y = y
        if isinstance(z, numbers.Number):
            self.z = z


class Polygon(object):
    points = []

    def __init__(self, points=None):
        """
        Initialize the geometry Polygon.

        :param points: Array of Point geometry.
        """
        if points is not None:
            self.setCoordinate(points)

    def __len__(self):
        """
        Overloading len() method.

        :return: Number of point in the polygone.
        """
        count = -1
        count += len(self.points)
        return count

    def setCoordinate(self, points):
        """
        Set coordinate of the Polygon.

        :param points: Array of Point geometry.
        """
        try:
            p1 = None
            p2 = None
            count = 0
            length = len(points)

            for point in points:
                if isinstance(point, Point):
                    self.points.append(point)
                    count += 1
                    if count == 1:
                        p1 = point
                    if length == count:
                        p2 = point
                else:
                    raise Exception("Polygon must be formed by points.")
            if p1 != p2:
                raise Exception("A polygon must close on the first point.")
        except Exception:
            raise

    def getCoordinate(self):
        coord = []
        for point in self.points:
            coord.append(point.getCoordinate())
        return coord

