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


import bpy

from . import GlUiWidgets

from .GlUiGl import GPU_Quad
from.GlUiCore import GlArea


class GlWindow(GlUiWidgets.GlWidget):
    def __init__(self, context):
        super(GlWindow, self).__init__()
        self._childrens = []
        self._context = context
        self._close = False

        self._header = GPU_Quad(self)
        self._header_height = 30
        self._frame = GPU_Quad(self)

    def add_widget(self, widget):
        self._childrens.append(widget)

    def draw(self):
        panel_color = bpy.context.preferences.themes['Default'].view_3d.space.panelcolors
        min_x, max_x, min_y, max_y = GlArea.getSize(self._context,
                                                    "VIEW_3D",
                                                    self.x,
                                                    self.y
                                                    )
        self._header.vertices = (
            (min_x, min_y),
            (min_x + self.width, min_y),
            (min_x, min_y - self._header_height),
            (min_x + self.width, min_y - self._header_height)
        )
        self._header.color = panel_color.header

        self._frame.vertices = (
            (min_x, min_y - self._header_height),
            (min_x + self.width, min_y - self._header_height),
            (min_x, min_y - self.height),
            (min_x + self.width, min_y - self.height),
            )
        self._frame.color = panel_color.back

        self._header.draw()
        self._frame.draw()

    @property
    def is_closed(self):
        return self._close

    def close(self):
        self._close = True