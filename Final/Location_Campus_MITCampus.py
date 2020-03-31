# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 17:14:36 2017

@author: jialilei
"""

### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)
        
class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        Campus.__init__(self, center_loc)
        self.tents = [tent_loc]
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        if all([new_tent_loc.dist_from(t)>=0.5 for t in self.tents]):
            self.tents.append(new_tent_loc)
            return True
        return False
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        if tent_loc not in self.tents:
            raise ValueError()
        self.tents.remove(tent_loc)
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        def mergeSort(l):            
            result = []
            if len(l)<=1:
                return l            
            half = len(l)//2
            lhs = mergeSort(l[:half])
            rhs = mergeSort(l[half:])
            while len(lhs)>0 and len(rhs)>0:
                if lhs[0].getX() <= rhs[0].getX():
                    result.append(lhs[0])
                    lhs.pop(0)
                else:
                    result.append(rhs[0])
                    rhs.pop(0)
            if len(lhs)>0:
                result+=lhs
            if len(rhs)>0:
                result+=rhs
            return result
        return [l.__str__() for l in mergeSort(self.tents)]