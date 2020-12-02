""" Module of mathematic algorithm.

 Copyright 2020 Vincent Leduc

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
    http: // www.apache.org / licenses / LICENSE - 2.0

"""
import numbers
import collections


def NumberLimit(array):
    """
    Converter python binary approximation around zero to zero.

    :param array: A number or an array of number.
    :return: Corrected array or number.
    """
    if not isinstance(array, collections.Iterable) and isinstance(array, numbers.Number):
        array = round(array, 15)
        return array
    for i in range(len(array)):
        if isinstance(array[1], numbers.Number):
            array[i] = round(array[i], 15)
    return array
