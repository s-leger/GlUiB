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


from . import GlUiCore


class GlWidget(GlUiCore.GlObject):
    def __init__(self):
        self._x = 0
        self._y = 0
        self._width = 300
        self._height = 100

    @property
    def x(self):
        """
        Return the x coordonates
        :return: int
        """
        return self._x

    def setX(self, x):
        """
        Set the x coordonate.
        :param x: int
        """
        self._x = x

    @property
    def y(self):
        """
        Return the x coordonates
        :return: int
        """
        return self._x

    def setY(self, y):
        """
        Set the y coordonate.
        :param y: int
        """
        self._y = y

    def move(self, x, y):
        """
        Set the coordonates with the given x and y coordonates.
        :param x: int
        :param y: int
        """
        self.setX(x)
        self.setY(y)

    @property
    def globalX(self):
        """
        Return the global x coordonate
        :return: int
        """
        parent = self.parent
        if parent is not None:
            return self.parent.globalX + self.x
        return self.x

    @property
    def globalY(self):
        """
        Return the global y coordonate
        :return: int
        """
        parent = self.parent
        if parent is not None:
            return self.parent.globalY + self.y
        return self.y

    @property
    def height(self):
        """
        Return the height.
        :return: int
        """
        return self._height

    def setHeight(self, h):
        """
        Set the height to the given height.
        :param h: int
        """
        self._height = max(0, h)

    @property
    def width(self):
        """
        Return the width.
        :return: int
        """
        return self._width

    def setWidth(self, w):
        """
        Set the width of the given width.
        :param w: int
        """
        self._width = max(0, w)

    def resize(self, w, h):
        """
        Change the size with the given width and height.
        :param w: int
        :param h: int
        """
        self.setWidth(w)
        self.setHeight(h)

    def transpose(self):
        """
        Swap the width and the height values.
        """
        self._width, self._height = self._height, self._width

    def setGeometry(self, x, y, w, h):
        """
        Set the coordonates with the given x and y coordonates.
        Set the size with the given width and height.
        :param x: int
        :param y: int
        :param w: int
        :param h: int
        """
        self.move(x, y)
        self.resize(w, h)