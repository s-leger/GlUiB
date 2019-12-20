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
    @property
    def parent(self):
        if hasattr(self, "_parent"):
            return self._parent
        return None

class GlArea:
    @staticmethod
    def getArea(context, area_type):
        for area in context.screen.areas:
            if area.type == area_type:
                return area
        return None

    @staticmethod
    def view_3dSize(context, area, margin_x, margin_y):
        w = area.width
        h = area.height
        min_x = 0 + margin_x
        min_y = h - margin_y
        max_x = w
        max_y = 0
        system = context.preferences.system

        for region in area.regions:
            if system.use_region_overlap:
                if region.type == 'TOOLS':
                    min_x += region.width
                if region.type == 'UI':
                    max_x -= region.width
            if region.type == 'HEADER':
                min_y -= region.height

        return min_x, max_x, min_y, max_y

    @classmethod
    def getSize(cls, context, area_type, margin_x, margin_y):
        area = cls.getArea(context, area_type)
        if area is not None:
            return getattr(cls, f"{area_type.lower()}Size")(context,
                                                            area,
                                                            margin_x,
                                                            margin_y)

        raise AttributeError(f"{area_type} not found")