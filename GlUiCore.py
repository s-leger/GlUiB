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


class GlObject:
    def __init__(self):
        self._is_hover = False

    @property
    def is_hover(self):
        return self._is_hover

    def setIsHover(self, event, x, y, w, h):
        self._is_hover = (
                0 < event.mouse_region_x - x < w and
                y > event.mouse_region_y > y - h)


class GlArea:
    def __init__(self):
        self._min_x = 0
        self._min_y = 0
        self._max_x = 0
        self._max_y = 0

    @property
    def min_x(self):
        return self._min_x

    @property
    def max_x(self):
        return self._max_x

    @property
    def min_y(self):
        return self._min_y

    @property
    def max_y(self):
        return self._max_y

    def getArea(self, context, area_type):
        for area in context.screen.areas:
            if area.type == area_type:
                return area
        return None

    def view_3dSize(self, context, area):
        w = area.width
        h = area.height
        self._min_x = 0
        self._min_y = h
        self._max_x = w
        self._max_y = 0
        system = context.preferences.system

        for region in area.regions:
            if system.use_region_overlap:
                if region.type == 'TOOLS':
                    self._min_x += region.width
                if region.type == 'UI':
                    self._max_x -= region.width
            if region.type == 'HEADER':
                self._min_y -= region.height

    def getSize(self, context, area_type):
        area = self.getArea(context, area_type)
        if area is not None:
            getattr(self, f"{area_type.lower()}Size")(context, area)