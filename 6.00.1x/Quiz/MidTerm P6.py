# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 22:57:32 2016

@author: lantao
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for i in L:
        i.reverse()
    L.reverse()