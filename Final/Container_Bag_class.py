# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:19:06 2017

@author: jialilei
"""

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        if e in self.vals.keys():
            self.vals[e]-=1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        if e in self.vals.keys():
            return self.vals[e]
        return 0
    
    def __add__(self, other):
        """
        self, other: object of Bags
        return the union of the two bags
        """
        new = Bag()
        for e in self.vals.keys():
            new.vals[e] = self.vals[e]
        for e in other.vals.keys():
            if e not in new.vals.keys():
                new.vals[e] = other.vals[e]
            else:
                new.vals[e] += other.vals[e]
        return new
        
class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        if e in self.vals.keys():
            del(self.vals[e])

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        if e in self.vals.keys():
            return True
        return False