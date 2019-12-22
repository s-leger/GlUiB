# -*- coding:utf-8 -*-

# GlUiD module for Blender
# Copyright (C) 2018 Legigan Jeremy AKA Pistiwique
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# <pep8 compliant>


from .GlUiCore import GlObject


class GlWidget(GlObject):
    def __init__(self, parent=None):
        GlObject.__init__(self)
        self._parent = parent
        self.top = 0
        self.left = 0
        self.width = 300
        self.height = 100

    @property
    def bottom(self):
        """
        Property that return the y coordonates relative to the parent
        :return: int
        """
        return self.top - self.height

    @bottom.setter
    def bottom(self, val):
        """
        Set the y coordonate relative to the parent with the given y.
        :param val: int
        """
        self.top = val + self.height

    @property
    def right(self):
        """
        Property that return the y coordonates relative to the parent
        :return: int
        """
        return self.left + self.width

    @right.setter
    def right(self, val):
        """
        Set the y coordonate relative to the parent with the given y.
        :param val: int
        """
        self.left = val - self.width

    @property
    def coords(self):
        """
        Property that return the 2D coordonates relative to the parent.
        :return: tuple of int
        """
        return (self.top, self.left)

    @coords.setter
    def coords(self, coords):
        """
        Set the coordonates relative to the parent with the given x and y.
        :param coords: tuple (int, int)
        """
        self.top, self.left = coords
    
    @property
    def global_left(self):
        """
        Return global left coordonate.
        :return: int
        """
        if self._parent is not None:
            return self._parent.left + self.left
        return self.left
    
    @global_left.setter
    def global_left(self, val):
        """
        Set global left coordonate.
        """
        if self._parent is not None:
            self.left = val - self._parent.left
        else:
            self.left = val
    
    @property
    def global_top(self):
        """
        Return global top coordonate.
        :return: int
        """
        if self._parent is not None:
            return self._parent.top + self.top
        return self.top
    
    @global_top.setter
    def global_top(self, val):
        """
        Set global top coordonate.
        """
        if self._parent is not None:
            self.top = val - self._parent.top
        else:
            self.top = val
    
    @property
    def height(self):
        """
        Property that return the height of the widget.
        :return: int
        """
        return self._height

    @height.setter
    def height(self, h):
        """
        Set the height with the given height value.
        :param h: int
        """
        self._height = max(0, h)

    @property
    def width(self):
        """
        Property that return the width of the widget.
        :return: int
        """
        return self._width

    @width.setter
    def width(self, w):
        """
        Set the width with the given width value.
        :param w: int
        """
        self._width = max(0, w)

    def resize(self, w, h):
        """
        Change the size of the widget with the given width and height values.
        :param w: int
        :param h: int
        """
        self.width, self.height = w, h

    def transpose(self):
        """
        Swap the width and the height values of the widget.
        """
        self.width, self.height = self.height, self.width

    def setGeometry(self, x, y, w, h):
        """
        Set the coordonates with the given x and y coordonates.
        Set the size with the given width and height.
        :param x: int
        :param y: int
        :param w: int
        :param h: int
        """
        self.coords = x, y
        self.resize(w, h)
